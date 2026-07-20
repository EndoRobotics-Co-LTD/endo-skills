> 이 파일은 상세 사전/예시다. 확정 운영규칙·가드레일은 상위 `SKILL.md`가 우선한다.
> 특히 SKILL.md가 override 하는 것:
> 1. 정량 임계치(cv·%·문단당 N개)는 방향 참고일 뿐 **추종 금지** — 판정은 낭독 테스트로 한다(수치 목표를 좇으면 인공 burstiness라는 새 AI 티가 생긴다).
> 2. 원문에 없는 **수치·고유명사·건수 창작 금지** — 복구 가능한 것만 넣고, 없으면 `[근거/수치 필요]` flag(의료기기 데이터 무결성).
> 3. **단일 출현은 감점 아님** — 군집·빈도·저버스티니스일 때만 신호(em-dash·삼단나열·번역투 단독 판정 금지).

# AI 티(tells) 검증 Taxonomy — 영문 비즈니스/보고서 레지스터

de-ai-editor 스킬의 **탐지(detect) → 진단(diagnose) → 재작성(rewrite) → 적대적 재검증(adversarial re-check)** 패스에 바로 물릴 수 있도록, 4개 층위 × tell별로 정리했다. 각 tell은 실제 근거(실증 연구 / 담론 합의 / 맥락 의존)를 구분 표기하고 before(AI)→after(사람) 재작성 예시를 붙였다.

## 확신도 범례

| 표기 | 의미 | 근거 성격 |
|---|---|---|
| ◎ 실증 | 대규모 코퍼스·피어리뷰 연구로 빈도 급증 확인 | Kobak et al. PubMed 1,420만 초록(2010–2024) — "delve" 25.2배, "underscores" 9.1배, "showcasing" 9.2배 급증. 2024년 초록 최소 10%가 LLM 처리 추정 |
| ○ 합의 | 편집자·탐지 담론에서 광범위하게 문서화, 정식 통계는 부분적 | Wikipedia:Signs of AI writing, 다수 편집 가이드 |
| △ 맥락 | **개별 사용은 AI 증거 아님**. 빈도·패턴·군집일 때만 신호. 단독 판정 금지 | em-dash 논쟁 등 |

핵심 원칙: **AI 티는 "단어 하나"가 아니라 "동시 출현(co-occurrence)과 균일함(low burstiness)"에서 드러난다.** 아래 tell들이 3개 층위 이상에서 겹칠 때만 강한 신호로 취급하라.

---

## 층위 1 — 어휘(Lexical)

| # | Tell (신호) | 설명 (KR) | Before (AI) | After (사람) | 확신도 |
|---|---|---|---|---|---|
| L1 | 추상 과장 동사: *delve (into), underscore, leverage, harness, utilize, streamline, showcase, foster, garner, boast* | 훈련데이터의 격식 편향으로 평범한 동사(use, show, help, cut) 대신 "고급" 동사를 기본값으로 씀. 실증 상위 급증어 대부분이 여기 속함 | "This report will **delve into** the root causes and **leverage** our test data to **underscore** the risk." | "This report traces the root causes and **uses** our test data to **show** the risk." | ◎ |
| L2 | 인플레 형용사: *robust, comprehensive, crucial, pivotal, seamless, innovative, cutting-edge, meticulous, significant(ly), key, vital* | 내용 없는 강조. 근거·수치로 대체 가능한 자리를 형용사가 메움 | "We ran a **comprehensive** validation with **robust** results and **significant** improvement." | "We ran 42 validation cycles; the failure rate dropped from 3.1% to 0.4%." | ◎ (crucial·comprehensive·pivotal·meticulous 실증 / robust·seamless 합의) |
| L3 | 위세·은유 명사: *tapestry, landscape, realm, ecosystem, testament, cornerstone, beacon, synergy, insights* | 구체 대상 대신 추상적 "격"을 부여하는 명사. 비즈니스 문서에 특히 부자연 | "Our QMS is a **testament** to quality across the regulatory **landscape**." | "Our QMS passed the 2025 MFDS and FDA audits with zero major findings." | ○ (insights 실증 / tapestry·testament·landscape 합의) |
| L4 | 헤지·군말 오프너: *It's worth noting, It's important to note, Importantly, Notably, Particularly* | 문장 앞에 붙는 무게잡기. 정작 뒤 내용이 평범 | "**It's worth noting that** the deadline is Q4. **Importantly,** the team is aligned." | "The deadline is Q4, and the team is aligned." | ○ (Notably·Particularly 실증 ten-word 목록) |
| L5 | 신호어·접속 부사 남발: *Moreover, Furthermore, Additionally, In conclusion, Overall* | 문장마다 접속 부사로 관계를 명시 — 사람은 흐름으로 처리 | "**Furthermore,** costs rose. **Additionally,** yield fell. **In conclusion,** margins are tight." | "Costs rose and yield fell, so margins are tight." | ◎ (Additionally 실증 ten-word 목록) |

---

## 층위 2 — 구문(Syntactic)

| # | Tell | 설명 (KR) | Before (AI) | After (사람) | 확신도 |
|---|---|---|---|---|---|
| S1 | 부정 병렬/대조: *not just X, but Y / It's not about X, it's about Y / not only… but also* | LLM이 문단마다 하나씩 심는 대표 리듬. 통찰처럼 보이지만 공허 | "This **isn't just** a process fix, **it's** a culture shift." | "This is a process fix that also changes how the team works day to day." | ○ |
| S2 | 코퓰라 회피(격상 동사): *serves as, stands as, functions as, represents, marks* — "is/are" 기피 | 단순 서술 자리를 격상 동사로 부풀림 | "The PLM **serves as** the single source of truth and **stands as** a milestone." | "The PLM **is** our single source of truth." | ○ |
| S3 | 삼단 나열(rule of three): "*fast, reliable, and scalable*" 식 3항 반복 | 사람도 쓰지만 AI는 거의 모든 문장·불릿을 3항으로 맞춤 → **빈도가 신호** | "The tool is **fast, intuitive, and powerful**, offering **speed, clarity, and control**." | "The tool is fast, and users find it obvious to navigate." | △ (개별 3항≠AI, 반복 군집일 때만) |
| S4 | 의미 없는 분사 꼬리: *…, highlighting the importance of… / …, ensuring… / …, reflecting…* | 문장 끝에 "-ing" 절로 억지 의의 부여(피상 분석) | "Yield improved, **highlighting the importance of** process control." | "Yield improved because we tightened the humidity spec." | ○ (highlighting·showcasing 실증) |
| S5 | 균일한 문장 길이·리듬(low burstiness) | 사람 글은 문장 길이가 들쭉날쭉("drunk EKG"), AI는 교과서 히스토그램처럼 균일 | (모든 문장이 18–22단어로 매끈하게 이어짐) | (3단어 단문과 40단어 장문을 의도적으로 섞음) | ○ (탐지 담론의 핵심 통계 신호) |
| S6 | em-dash(—) 사용 | **미신 주의.** em-dash 존재 자체는 AI 증거가 **아님**(숙련 필자·출판물이 정상 사용). AI는 *빈도·기계적 삽입 패턴*이 다를 뿐 | — | — | △ 맥락 (단독 판정 금지 / 문단당 여러 개 + 다른 tell 동반일 때만 감점) |

---

## 층위 3 — 구조(Structural)

| # | Tell | 설명 (KR) | Before (AI) | After (사람) | 확신도 |
|---|---|---|---|---|---|
| T1 | 과도한 볼드·불릿화 | 핵심어마다 기계적으로 **볼드**, 산문으로 될 것도 전부 불릿 | "**Goal:** ship. **Owner:** DJ. **Risk:** high. **Impact:** major." (5줄 연속) | "DJ owns the ship date; the main risk is the supplier lead time." | ○ |
| T2 | 이모지 헤더/장식 이모지 | 섹션 제목에 🚀✨🔑 등, 비즈니스 레지스터에 부적합 | "🚀 Next Steps / ✨ Key Wins / 🔑 Takeaways" | "Next steps / What worked / Takeaways" | ○ |
| T3 | 섹션 동형성(isomorphism) + 상투 헤더 | 모든 섹션이 동일 골격(정의→장점→도전과제), "Challenges and Future Directions" 같은 캔형 제목 | 4개 섹션 모두 "Overview / Benefits / Challenges / Future Directions" 반복 | 각 섹션이 그 내용에 맞는 고유 제목·길이·형태를 가짐 | ○ |
| T4 | 서론-본론-결론 상투 프레임 강제 | 짧은 메모·메일에도 "Introduction… In conclusion…" 삼단 틀 | (반 페이지 메일에 서론 문단 + 결론 문단) | 첫 줄이 결론(BLUF), 나머지는 근거 | ○ |
| T5 | Title Case 제목 / 굽은 따옴표(" ") | 약한 신호. 스타일 가이드·에디터 자동변환으로도 발생 | — | — | △ 맥락 (보조 지표만) |

---

## 층위 4 — 수사(Rhetorical)

| # | Tell | 설명 (KR) | Before (AI) | After (사람) | 확신도 |
|---|---|---|---|---|---|
| R1 | 입장 없는 양비론 요약 | "장점도 있고 단점도 있다"로 판단 회피 | "**While** this approach has benefits, it **also** presents challenges to consider." | "Take this approach — the lead-time risk is worth the 20% cost cut." | ○ |
| R2 | 추상적 일반론(구체·숫자 회피) | 검증 가능한 수치·고유명사 대신 뜬 개념 | "This will **greatly enhance efficiency** and **drive value** across the organization." | "This cuts the release review from 5 days to 2." | ○ |
| R3 | 뻔한 것 과잉 설명 / 헛기침 | 독자가 아는 배경을 장황히 서두에 깖 | "In order to understand the results, it's first important to understand what testing is…" | (바로 결과로 진입) | ○ |
| R4 | 마무리 상투구: *In today's fast-paced world / By doing so / At the end of the day / the possibilities are endless* | 콘텐츠 밀 없는 클로징 | "**In today's fast-paced world,** quality matters. **By doing so,** we win." | "We win on quality — reliably, every batch." | ○ |
| R5 | 모호한 출처: *Experts argue / Studies show / Industry reports suggest* | 근거를 익명 권위로 대체 | "**Studies show** early testing reduces cost." | "Our 2025 line data: defects caught at DV cost 6× less than at PV." | ○ (wiki 확인) |
| R6 | 의의 인플레: *is a testament to / plays a pivotal role / marks a significant milestone* | 성과를 과장 수사로 포장 | "This launch **marks a significant milestone** and **is a testament to** our team." | "This is our first FDA-cleared device." | ○ |

---

## 정직하게 표기하는 "미신 / 맥락 의존" (skill이 과잉 감점하지 않도록)

| 항목 | 흔한 주장 | 검증된 실제 | skill 처리 |
|---|---|---|---|
| em-dash(—) | "em-dash = AI" | **거짓.** 숙련 필자·편집 출판물이 원래 애용. WaPo·Rolling Stone·The Ringer 등 다수가 반박. 실제 신호는 밑에 깔린 *리듬·빈도* | 단독 감점 금지. 다른 tell 2개 이상 동반 + 문단당 다수일 때만 |
| 삼단 나열(rule of three) | "3항 나열 = AI" | 부분 참. 수사학 기본기라 사람도 상시 사용. AI는 *거의 모든 문장에* 적용 → 빈도가 신호 | 개별 허용, 문서 전반 반복 시 감점 |
| 굽은 따옴표·Title Case | "= AI" | 약함. 워드/에디터 자동변환으로도 발생 | 보조 지표만 |
| "delve" 등 특정 단어 | "delve 있으면 AI" | 맥락 의존. delve는 2023–24 정점 후 2025 급감(모델이 학습해 회피). 단어 목록은 *상시 갱신 필요*, 고정 블랙리스트로 쓰면 오탐 | 목록은 버전 관리, 군집으로 판정 |
| 완벽한 문법·오타 없음 | "너무 깨끗하면 AI" | 근거 약함. 좋은 편집 결과와 구별 불가 | 신호로 쓰지 않음 |

---

## skill 파이프라인에 물리는 방식 (권고)

1. **Detect** — 4층위 tell을 스캔해 위치·개수 태깅. 단일 tell이 아니라 **층위 교차 군집**과 **문장길이 분산(burstiness) 저하**를 점수화.
2. **Diagnose** — tell별로 "왜 AI 티인지 / 무엇을 잃었는지(구체성·입장·리듬)" 한 줄 진단. 미신 항목은 감점하지 않음.
3. **Rewrite** — 위 after 원칙 적용: 격상어→평이어, 추상→수치·고유명사, 양비론→입장, 균일→길이 변주, 접속부사·헤지·클로징 제거.
4. **Adversarial re-check** — 재작성본을 **다시 detect에 통과**시켜 "아직 AI 같은가" 재판정. 특히 재작성이 새 tell(과교정으로 인한 단조로움, 억지 구어체)을 만들지 않았는지 검사. 통과 못하면 재루프.

**Voice-fingerprint 슬롯(이번 범위 밖):** 3단계 Rewrite에서 "평이·구체·입장 있는 문장"으로 되돌린 뒤, 박동진 본인 샘플에서 추출한 어휘·문장길이·연결어 선호를 적용하는 층을 **이 지점에** 삽입하도록 인터페이스만 남겨둔다(현재는 "중립 사람 레지스터"가 기본값). de-ai-editor는 저자 위조가 아니라 품질·가독성 향상이 목적이며, 규제 제출물은 RQA 사람 검토·서명이 최종 게이트임을 스킬 설명에 명시.

---

## 출처

- [Kobak et al., "Delving into ChatGPT usage in academic writing through excess vocabulary" (arXiv 2406.07016)](https://arxiv.org/html/2406.07016v1) — 실증 어휘 급증 데이터 (◎ 근거)
- [PMC: "Delving Into PubMed Records: How AI-Influenced Vocabulary has Transformed Medical Writing since ChatGPT"](https://pmc.ncbi.nlm.nih.gov/articles/PMC12679996/) — 의학 글쓰기 대상 후속 검증
- [FSU News: "Why Does ChatGPT 'Delve' So Much?"](https://news.fsu.edu/news/science-technology/2025/02/17/why-does-chatgpt-delve-so-much-fsu-researchers-begin-to-uncover-why-chatgpt-overuses-certain-words/) — RLHF 기원 가설
- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) — 구문·구조·수사 tell 커뮤니티 taxonomy (○ 근거)
- [Duey AI: The Em-Dash Myth](https://www.duey.ai/post/em-dash-ai-writing) / [Washington Post](https://www.washingtonpost.com/technology/2025/04/09/ai-em-dash-writing-punctuation-chatgpt/) / [The Ringer](https://www.theringer.com/2025/08/20/pop-culture/em-dash-use-ai-artificial-intelligence-chatgpt-google-gemini) — em-dash 미신 반박 (△ 맥락 근거)
- [Plus AI: The most overused ChatGPT words](https://plusai.com/blog/the-most-overused-chatgpt-words/) / [Embryo: words AI overuses](https://embryo.com/blog/list-words-ai-overuses/) — 어휘 목록 교차 확인