"""Provider adapters for answer generation; retrieval stays provider-independent."""

import os
import sys
import time
from typing import Protocol


class AnswerClient(Protocol):
    def generate(self, *, contents: str, system_prompt: str) -> str: ...


class GeminiClient:
    def __init__(self, client, model: str, fallback_model: str | None = None):
        self.client = client
        self.models = list(dict.fromkeys(filter(None, (model, fallback_model))))

    def generate(self, *, contents: str, system_prompt: str) -> str:
        from google.genai import errors, types

        config = types.GenerateContentConfig(
            system_instruction=system_prompt, temperature=0.2,
        )
        last_error = None
        for model in self.models:
            for attempt in range(4):
                try:
                    response = self.client.models.generate_content(
                        model=model, contents=contents, config=config,
                    )
                    if not response.text or not response.text.strip():
                        raise RuntimeError("Gemini returned no answer text")
                    return response.text
                except errors.ServerError as error:
                    last_error = error
                    if attempt < 3:
                        wait = 2**attempt
                        print(f"[{model}] {error.code}; retrying in {wait}s...", file=sys.stderr)
                        time.sleep(wait)
        raise RuntimeError("Gemini is unavailable on all configured models") from last_error


class CohereClient:
    def __init__(self, client, model: str):
        self.client = client
        self.model = model

    def generate(self, *, contents: str, system_prompt: str) -> str:
        # The SDK handles transient-error retries. Authentication and invalid-model
        # errors propagate to the caller rather than silently switching providers.
        response = self.client.chat(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": contents},
            ],
            temperature=0.2,
        )
        text = "\n".join(
            block.text for block in (response.message.content or [])
            if block.type == "text" and block.text
        )
        if not text.strip():
            raise RuntimeError("Cohere returned no answer text")
        return text


def _required(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value:
        raise ValueError(f"Set {name} for the selected answer provider")
    return value


def create_client() -> AnswerClient:
    """Read configuration at call time, after the application loads its settings."""
    provider = os.getenv("LLM_PROVIDER", "gemini").strip().lower()
    if provider == "gemini":
        model = _required("GEMINI_MODEL")
        from google import genai

        return GeminiClient(
            genai.Client(), model, os.getenv("GEMINI_FALLBACK_MODEL") or None,
        )
    if provider == "cohere":
        api_key = _required("COHERE_API_KEY")
        model = _required("COHERE_MODEL")
        import cohere

        return CohereClient(cohere.ClientV2(api_key=api_key), model)
    raise ValueError(f"Unsupported LLM_PROVIDER {provider!r}; use gemini or cohere")
