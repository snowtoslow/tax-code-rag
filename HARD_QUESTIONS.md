# Hard RAG question bank

41 challenge questions grounded in the local `page.md` snapshot. These are tests of the document, not current legal guidance. No live failures have been measured yet.

Expected answers are review rubrics. Automated fact checks are approximate and do not establish complete correctness.

## 1. treaty_exception

Title I · exception

Un tratat fiscal diferă de Cod. Se aplică automat tratatul inclusiv când rezidentul partenerului este folosit de un terț neeligibil pentru facilități?

**Expected:** Tratatul are prioritate în general, dar art.4 alin.(2) exclude cazul rezidentului folosit de un terț neeligibil.

**Source:** [page.md:1773–1783](src/docling_pdf/output/page.md#L1773)

## 2. resident_183

Title I · boundary

O persoană fără domiciliu permanent aici stă exact 183 de zile în Moldova într-un an fiscal, fără statut diplomatic sau alte excepții. Îndeplinește criteriul de rezidență bazat pe durată?

**Expected:** Da: cel puțin 183 de zile, nu mai mult de 183.

**Source:** [page.md:1796–1808](src/docling_pdf/output/page.md#L1796)

## 3. resident_student_exception

Title I · rule_vs_exception

Un străin fără domiciliu permanent în Moldova se află aici 200 de zile exclusiv la învățătură. Regula celor 183 de zile îl face automat rezident fiscal?

**Expected:** Nu; art.5 pct.6 lit.a include excepția șederii exclusiv la învățătură.

**Source:** [page.md:1808–1824](src/docling_pdf/output/page.md#L1808)

## 4. permanent_establishment_boundary

Title I · strict_boundary

Un șantier al unui nerezident durează exact șase luni și nu există alte criterii de reprezentanță permanentă. Este suficientă durata pentru a constitui reprezentanță permanentă?

**Expected:** Nu; criteriul este mai mare de șase luni, iar activitatea care nu depășește șase luni este exceptată în condițiile pct.15¹.

**Source:** [page.md:1840–1855](src/docling_pdf/output/page.md#L1840), [page.md:1855–1870](src/docling_pdf/output/page.md#L1855)

## 5. farmer_vs_company

Title II · similar_rates

Au aceeași cotă de impozit pe venit o persoană juridică în regim general și o gospodărie țărănească? Indică ambele cote.

**Expected:** Nu: persoana juridică 12%, gospodăria țărănească 7%, din venitul impozabil.

**Source:** [page.md:2360–2375](src/docling_pdf/output/page.md#L2360)

## 6. personal_exemption_equal_limit

Title II · strict_boundary

Un rezident are venit anual impozabil de exact 360000 lei, fără venituri de la art.90¹ și fără statut pentru scutirea majorată. Primește scutirea personală obișnuită de 29700 lei?

**Expected:** Nu; art.33 alin.(1) cere venit mai mic de 360000 lei, nu egal.

**Source:** [page.md:2912–2920](src/docling_pdf/output/page.md#L2912)

## 7. dependent_equal_limit

Title II · inclusive_boundary

Copilul întreținut îndeplinește condiția de rudenie și are exact 12400 lei venit anual luat în calcul. Este depășit plafonul și care este scutirea anuală obișnuită?

**Expected:** Plafonul nu este depășit: nu depășește 12400; scutire obișnuită 9900 lei.

**Source:** [page.md:2940–2962](src/docling_pdf/output/page.md#L2940)

## 8. spouse_cross_reference

Title II · cross_reference

Soția mea este persoană cu dizabilități severe din categoria art.33 alin.(2), dar beneficiază deja de scutire personală. Pot primi și scutirea pentru soție de 21780 lei?

**Expected:** Nu: art.34 alin.(2) cere ca soțul/soția să nu beneficieze de scutire personală.

**Source:** [page.md:2920–2946](src/docling_pdf/output/page.md#L2920)

## 9. education_shared_cap

Title II · aggregate_limit

Am plătit 15000 lei pentru învățământul meu și 15000 lei pentru copilul întreținut, la instituții eligibile. Pot deduce 30000 lei potrivit art.35² alin.(6)?

**Expected:** Nu: plafon cumulativ de 20000 lei pentru toate tipurile și toți beneficiarii, nu per persoană.

**Source:** [page.md:2970–2978](src/docling_pdf/output/page.md#L2970)

## 10. capital_gain_calculation

Title II · multi_step_calculation

O persoană fizică rezidentă vinde un activ de capital impozabil cu 150000 lei, cu bază valorică de 100000 lei. Fără pierderi, scutiri ori regimuri speciale, calculează creșterea brută, suma inclusă conform art.40 alin.(7) și impozitul la cota art.15 lit.a.

**Expected:** Creștere 50000; includere 50%=25000; impozit 12%=3000 lei.

**Source:** [page.md:3025–3056](src/docling_pdf/output/page.md#L3025), [page.md:2360–2366](src/docling_pdf/output/page.md#L2360)

## 11. car_capital_exception

Title II · exception_to_exception

Regula de nerecunoaștere a creșterii de capital pentru autoturismul deținut cel puțin trei ani se aplică și unui autovehicul de colecție de interes istoric?

**Expected:** Nu: autovehiculele de colecție de interes istoric sau etnografic sunt exceptate de la această nerecunoaștere.

**Source:** [page.md:3035–3044](src/docling_pdf/output/page.md#L3035)

## 12. vat_exact_threshold

Title III · strict_boundary

O firmă obișnuită are exact 1,7 milioane lei livrări relevante în 12 luni consecutive, fără alte temeiuri. Numai această valoare impune înregistrarea obligatorie TVA conform art.112 alin.(1)?

**Expected:** Nu; livrările trebuie să depășească 1,7 milioane. Înregistrarea voluntară este altă regulă.

**Source:** [page.md:5362–5370](src/docling_pdf/output/page.md#L5362)

## 13. vat_registration_two_dates

Title III · different_clocks

Firma obișnuită depășește pentru prima dată plafonul relevant TVA pe 15 mai. Fără alte excepții, până când se înregistrează și din ce dată este considerată înregistrată?

**Expected:** Până la ultima zi din mai; considerată înregistrată de la 1 iunie.

**Source:** [page.md:5362–5366](src/docling_pdf/output/page.md#L5362)

## 14. vat_voluntary_registration

Title III · false_premise

Dacă sunt sub plafonul obligatoriu TVA, Codul îmi interzice să mă înregistrez voluntar, chiar dacă preconizez livrări impozabile?

**Expected:** Nu: art.112 alin.(2) permite înregistrarea pentru livrări impozabile preconizate.

**Source:** [page.md:5366–5370](src/docling_pdf/output/page.md#L5366)

## 15. vat_import_earlier_event

Title III · earliest_event

Un antreprenor neînregistrat TVA achită un serviciu importat pe 10 martie, iar importul serviciului are loc în aprilie. Conform art.115 alin.(2) lit.b, care este termenul TVA, fără ajustări pentru zile nelucrătoare?

**Expected:** 25 aprilie: se folosește evenimentul mai timpuriu, plata din martie.

**Source:** [page.md:5438–5450](src/docling_pdf/output/page.md#L5438)

## 16. vat_restaurant_alcohol

Title III · category_exception

Cota redusă de 8% pentru alimentele și băuturile servite în activități din secțiunea I include automat și producția alcoolică?

**Expected:** Nu: producția alcoolică este exceptată explicit din această prevedere.

**Source:** [page.md:4680–4686](src/docling_pdf/output/page.md#L4680)

## 17. repealed_excise_article

Title IV · repealed_rule

Enumeră obligațiile încă în vigoare din articolul 128 privind administrarea accizelor, exact cum apar în document.

**Expected:** Articolul 128 este abrogat; nu inventa obligații din titlul capitolului.

**Source:** [page.md:6100–6104](src/docling_pdf/output/page.md#L6100)

## 18. caviar_cider_change

Title IV · multi_row_year_comparison

Compară cota accizelor din 2024 cu cea din 2026 pentru caviar și pentru cidru de mere și de pere. Care s-a modificat și cu cât?

**Expected:** Caviar 25% în ambii ani, neschimbat. Cidru 1,80→2,00 lei/litru, +0,20 lei/litru.

**Source:** [page.md:6108–6116](src/docling_pdf/output/page.md#L6108)

## 19. limitation_distinction

Title V · multi_article_distinction

Sunt identice termenul obișnuit pentru determinarea obligațiilor fiscale și cel pentru executarea lor silită? Precizează duratele și de când curg, conform art.264 și 265.

**Expected:** Determinare: de regulă 4 ani de la ultima dată de declarare/plată. Executare: 6 ani după determinare; reguli diferite și excepții/suspendări.

**Source:** [page.md:9917–9929](src/docling_pdf/output/page.md#L9917), [page.md:9933–9940](src/docling_pdf/output/page.md#L9933)

## 20. limitation_no_return

Title V · exception_limit

Dacă nu am prezentat darea de seamă fiscală, SFS poate extinde perioada supusă controlului fără nicio limită de timp?

**Expected:** Nu; art.264 alin.(3) permite extinderea, dar nu peste 6 ani de la ultima dată stabilită pentru prezentare.

**Source:** [page.md:9929–9932](src/docling_pdf/output/page.md#L9929)

## 21. appeal_deadline_and_extension

Title V · three_clocks

Distinge termenul pentru depunerea contestației fiscale, termenul obișnuit de examinare și prelungirea maximă a examinării. De la ce eveniment curge fiecare termen inițial?

**Expected:** Depunere: 30 zile de la comunicare/notificare; examinare: 30 zile de la primire; prelungire: cel mult încă 30 zile.

**Source:** [page.md:9993–9998](src/docling_pdf/output/page.md#L9993), [page.md:10005–10010](src/docling_pdf/output/page.md#L10005)

## 22. appeal_third_party

Title V · standing

Pot contesta în nume propriu decizia fiscală emisă pentru vecinul meu, fără să fiu vizat sau reprezentantul lui? Cine trebuie să dovedească incorectitudinea deciziei?

**Expected:** Nu; terții neeligibili rămân neexaminați. Sarcina probei revine persoanei care contestă.

**Source:** [page.md:9981–9992](src/docling_pdf/output/page.md#L9981)

## 23. late_refund_exception

Title V · exception_to_deadline

După expirarea celor șase ani, o cerere de restituire este întotdeauna imposibil de acceptat, chiar dacă există dovezi că termenul nu a putut fi respectat?

**Expected:** Nu: SFS poate repune în termen și accepta cererea dacă sunt prezentate dovezi ale imposibilității respectării termenului.

**Source:** [page.md:9963–9978](src/docling_pdf/output/page.md#L9963)

## 24. residential_minimum_not_fixed

Title VI · minimum_vs_fixed_rate

Pentru locuințe, cota de 0,05% este întotdeauna cota concretă obligatorie în toate localitățile? Cine stabilește cota concretă?

**Expected:** Este cota minimă; cota concretă se stabilește anual de autoritatea reprezentativă și deliberativă locală.

**Source:** [page.md:10217–10228](src/docling_pdf/output/page.md#L10217)

## 25. property_missing_local_decision

Title VI · fallback_rule

Dacă decizia locală privind cotele impozitului imobiliar este anulată prin hotărâre judecătorească definitivă, ce cote se aplică pentru anul fiscal următor?

**Expected:** Cotele minime, potrivit art.280 alin.(1²).

**Source:** [page.md:10235–10245](src/docling_pdf/output/page.md#L10235)

## 26. wealth_cumulative_conditions

Title VI1 · and_vs_or

Locuințele mele au în total 119 m² și valoare estimată de 250 salarii medii lunare. Doar depășirea valorii declanșează impozitul pe avere conform art.287³ alin.(1)?

**Expected:** Nu: condițiile sunt cumulative; suprafața trebuie să fie cel puțin 120 m².

**Source:** [page.md:10546–10554](src/docling_pdf/output/page.md#L10546)

## 27. wealth_exact_boundaries

Title VI1 · inclusive_double_boundary

O persoană fizică deține locuințe cu exact 120 m² și exact 200 salarii medii lunare valoare estimată, fără terenuri. Sunt îndeplinite ambele praguri ale impozitului pe avere?

**Expected:** Da: cel puțin 200 salarii și 120 m² sau mai mult, ambele praguri inclusive.

**Source:** [page.md:10546–10554](src/docling_pdf/output/page.md#L10546)

## 28. wealth_three_dates

Title VI1 · multi_section_dates

Pentru impozitul pe avere, distinge data situației patrimoniale, termenul avizului și termenul plății. Cine calculează impozitul?

**Expected:** Situația la 1 noiembrie; SFS calculează și prezintă avizul până la 10 decembrie; plata până la 25 decembrie.

**Source:** [page.md:10568–10577](src/docling_pdf/output/page.md#L10568)

## 29. small_business_local_deadline

Title VII · conditional_deadline

Un întreprinzător individual neplătitor TVA are exact cinci salariați medii anual. Poate folosi darea de seamă unificată pentru taxele locale și până când declară și achită? Menționează excepția din art.292 alin.(1).

**Expected:** Da; până la 25 martie anul următor, exceptând taxa de la art.291 lit.n¹.

**Source:** [page.md:10784–10790](src/docling_pdf/output/page.md#L10784)

## 30. it_local_rate_increase

Title VII · cross_title_override

Consiliul local mărește taxele locale. Crește din acest motiv și impozitul unic al rezidentului parcului IT? Explică legătura dintre cele două.

**Expected:** Nu: taxele locale sunt incluse în impozitul unic; modificarea lor locală nu schimbă mărimea acestuia.

**Source:** [page.md:10820–10836](src/docling_pdf/output/page.md#L10820)

## 31. water_bottling_distinction

Title VIII · similar_categories

Compară taxa pe m³ pentru firma care extrage și îmbuteliază apă potabilă cu firma care îmbuteliază apă potabilă extrasă de alt subiect. Sunt 16 lei în ambele cazuri?

**Expected:** Nu: extragere și îmbuteliere 16 lei/m³; apă extrasă de alt subiect, utilizată la îmbuteliere, 15,7 lei/m³.

**Source:** [page.md:11164–11178](src/docling_pdf/output/page.md#L11164)

## 32. hydropower_unit_calculation

Title VIII · unit_conversion

O hidrocentrală utilizează 100 m³ de apă taxabilă, fără înlesniri. Ce taxă rezultă din Anexa nr.1 la titlul VIII? Ai grijă la unitatea cotei.

**Expected:** 0,06 lei per 10 m³; 100/10 × 0,06 = 0,60 lei, nu 6 lei.

**Source:** [page.md:11166–11172](src/docling_pdf/output/page.md#L11166)

## 33. water_fire_intermediary

Title VIII · indirect_supply_exception

Apa extrasă este livrată printr-un agent economic pentru stingerea incendiilor. Intermediarul face să dispară înlesnirea taxei pentru apă?

**Expected:** Nu; art.306 lit.c include livrarea directă sau prin agenți economici pentru stingerea incendiilor.

**Source:** [page.md:11074–11090](src/docling_pdf/output/page.md#L11074)

## 34. natural_resources_no_object

Title VIII · reporting_exception

Dacă nu există obiect al impunerii pentru taxele pe resurse naturale, art.301 cere totuși depunerea unei dări de seamă cu zero?

**Expected:** Nu: în lipsa obiectului impunerii, darea de seamă nu se prezintă.

**Source:** [page.md:11016–11032](src/docling_pdf/output/page.md#L11016)

## 35. road_tax_transfer

Title IX · two_part_negation

Vând mașina după achitarea integrală a taxei rutiere pentru anul curent. Cumpărătorul plătește încă o dată, iar eu primesc restituirea pentru lunile rămase?

**Expected:** Nu la ambele: noul posesor nu achită din nou, iar fostului posesor nu i se restituie taxa.

**Source:** [page.md:11330–11338](src/docling_pdf/output/page.md#L11330)

## 36. road_failed_inspection

Title IX · different_refund_cases

Am plătit taxa rutieră, dar mașina nu a trecut inspecția tehnică. Primesc taxa înapoi? O achit iar la inspecția repetată în aceeași perioadă fiscală?

**Expected:** Nu se restituie pentru inspecția eșuată și nu se achită din nou la repetarea în aceeași perioadă fiscală.

**Source:** [page.md:11340–11349](src/docling_pdf/output/page.md#L11340)

## 37. it_minimum_calculation

Title X · multi_article_minimum

Rezidentul IT are într-o lună venit din vânzări 100000 lei și doi angajați care au lucrat fiecare cel puțin o zi. Pentru acest exercițiu salariul mediu prognozat este 15000 lei. Care este impozitul unic: procentul sau minimul?

**Expected:** 7%=7000 lei; minimul 2 × 30% × 15000=9000 lei; se achită 9000 lei.

**Source:** [page.md:11937–11950](src/docling_pdf/output/page.md#L11937)

## 38. it_seventy_percent_exception

Title X · temporary_noncompliance

Un rezident IT scade sub indicatorul activității principale în două luni calendaristice, dar atinge 70% pe întregul an relevant. Este obligatoriu o încălcare doar din cauza celor două luni?

**Expected:** Nu; cel mult două luni sunt tolerate dacă indicatorul 70% este asigurat pe perioada relevantă.

**Source:** [page.md:11929–11936](src/docling_pdf/output/page.md#L11929)

## 39. it_excluded_taxes

Title X · inclusion_vs_exclusion

Impozitul unic IT include taxele locale, TVA și accizele în aceeași măsură? Clasifică explicit fiecare dintre cele trei.

**Expected:** Taxele locale sunt incluse; TVA și accizele nu sunt incluse.

**Source:** [page.md:11957–11987](src/docling_pdf/output/page.md#L11957)

## 40. missing_private_tax_balance

Title V · unanswerable_private_data · expected refusal

Care este soldul exact al restanțelor fiscale al firmei SRL TEST_RAG_847291 la data de azi? Folosește doar documentul.

**Expected:** Nu se poate determina: Codul nu conține soldul fiscal individual al firmei fictive.

**Source:** No individual account records are present in the document.

## 41. missing_future_caviar_rate

Title IV · unanswerable_future_year · expected refusal

Care va fi cota exactă a accizelor pentru caviar în anul 2099? Nu extrapola cotele din alți ani.

**Expected:** Documentul oferă coloanele 2024–2026, nu cota pentru 2099. Nu extrapola 25%.

**Source:** [page.md:6108–6112](src/docling_pdf/output/page.md#L6108)
