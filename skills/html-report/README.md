# html-report — EndoRobotics 표준 HTML 보고서 빌더

> AI가 EndoRobotics 표준 디자인으로 **HTML 보고서**를 만들어주는 Claude Code Skill.
> 도메인이 무엇이든(참관기·리서치·분석·제안·결과 보고) **같은 포맷·같은 품질**이 자동 적용되고, 검증된 디자인 시스템 하나(`assets/template.html`)에서 시작해 내용만 채웁니다.

---

## 목차

1. [한 줄 요약](#한-줄-요약)
2. [사전 요구사항](#-사전-요구사항)
3. [설치 (1회)](#-설치-1회)
4. [첫 보고서 만들기](#-첫-보고서-만들기)
5. [무엇이 들어있나 — 디자인 시스템](#-무엇이-들어있나--디자인-시스템)
6. [이미지 인라인 (단일 파일 만들기)](#-이미지-인라인-단일-파일-만들기)
7. [structured-writing 와 함께 쓰기](#-structured-writing-와-함께-쓰기)
8. [업데이트](#-업데이트)
9. [문제 해결](#-문제-해결)
10. [관리자용 (디자인 표준 변경)](#-관리자용-디자인-표준-변경)
11. [문의](#-문의)
12. [라이센스](#-라이센스)

---

## 한 줄 요약

```bash
npx skills add EndoRobotics-Co-LTD/endo-skills -s html-report
```

→ Claude Code 재시작 → **"이 자료로 보고서 만들어줘"** 라고 하면 표준 디자인으로 HTML 보고서가 나옵니다.

- 기본 동작: **현재 폴더의 `.claude/skills/html-report/` 에 설치** (project-local).
- 모든 프로젝트에서 쓰려면 `-g` 추가.
- **보고서 작성 자체는 추가 의존성 없음.** 단, 로컬 이미지를 단일 파일로 인라인하려면 Python 3.x 필요 (→ [6번 항목](#-이미지-인라인-단일-파일-만들기)).

---

## 📋 사전 요구사항

| 항목 | 버전/조건 |
|---|---|
| **OS** | 무관 (Windows / macOS / Linux) |
| **Claude Code** | 최신 버전 |
| **Python** | (선택) 3.x — 로컬 이미지를 base64 인라인할 때만. 보고서 작성만 하면 불필요 |
| **브라우저** | 결과 .html 을 열어볼 크롬/엣지 등 (렌더 확인용) |
| **GitHub 접근권** | `EndoRobotics-Co-LTD/endo-skills` (public, 인증 불필요) |
| **언어** | 한국어 보고서 전용 (Pretendard, `word-break:keep-all`) |

---

## ⚡ 설치 (1회)

### 방법 A — `npx skills add` (가장 표준)

```bash
npx skills add EndoRobotics-Co-LTD/endo-skills -s html-report
```

- 기본: 현재 폴더의 `.claude/skills/html-report/` 에 설치 (project-local).
- 글로벌은 `-g` 추가.
- 보고서 작성에는 별도 패키지 설치가 필요 없습니다.

### 방법 B — 수동 (자동이 실패하면)

```powershell
# 1) 임시 폴더에 repo 클론
$temp = Join-Path $env:TEMP "endo-skills-clone"
git clone --depth 1 https://github.com/EndoRobotics-Co-LTD/endo-skills.git $temp

# 2) html-report 만 정확한 위치로 이동 (project-local 예시)
New-Item -ItemType Directory -Force .\.claude\skills | Out-Null
Move-Item "$temp\skills\html-report" ".\.claude\skills\html-report"
Remove-Item -Recurse -Force $temp
```

### 설치 후 한 번

**Claude Code를 한 번 종료했다가 다시 실행하세요.** 그래야 새 스킬이 인식됩니다.

> ✅ 확인: `.claude/skills/html-report/assets/template.html` 이 있으면 OK.

---

## 🎬 첫 보고서 만들기

설치 후 자연어로 요청하면 자동 발동합니다 ('보고서'라는 단어가 없어도 참관기·정리·분석 문서면 발동).

```
어제 컨퍼런스 참관 내용으로 보고서 만들어줘
```

```
이 미팅 전사록과 소개서를 합쳐서 깔끔한 HTML 보고서로 정리해줘
```

```
이 분석 결과를 예쁜 리포트로 만들어줘. 결론이 위에서 한눈에 보이게.
```

**Claude의 동작:**
1. 먼저 글의 '한 문장'(핵심 결론)을 잡고 — `structured-writing` 원칙으로 — 점진적 공개 구조로 배치.
2. `assets/template.html` 을 복사해 시작 (디자인을 새로 짜지 않음).
3. 표지·한 줄 결론·섹션·핵심 강조·펼침 카드·도식·표 등 컴포넌트를 골라 채움.
4. 브라우저로 렌더 확인 → 필요 시 이미지 인라인 → 단일 파일 완성.

---

## 🎨 무엇이 들어있나 — 디자인 시스템

핵심 자산은 검증된 **템플릿 하나**: [`assets/template.html`](assets/template.html). 디자인을 새로 짜지 않고 여기서 시작해 내용만 채웁니다.

| 구성요소 | 설명 |
|---|---|
| 표지 + 한 줄 결론(`.verdict`) | 첫 화면에서 결론이 바로 보이게 (점진적 공개) |
| sticky 목차(`nav.toc`) | 긴 보고서 네비게이션 |
| eyebrow 섹션 + 핵심 강조(`.core`) | 한 섹션 한 메시지, 핵심 한 줄을 주인공으로 |
| 펼침 카드(`details.s`) | 요약은 접고, 상세는 펼침 |
| 시각 컴포넌트 | SVG 도식(`figure.diagram`)·인터랙티브 타임라인(`.tl`)·구조 카드(`.silos`/`.pillars`/`.tracks`) |
| 콜아웃·표·부록 | 강조(`.call`)·데이터 표·출처/신뢰도(`.method`) |
| 이미지 라이트박스 | 모든 이미지 클릭 → 모달 확대 + 스크롤 줌 (자동) |

**디자인 원칙**: 절제된 팔레트(잉크 네이비 + 인디고 + 앰버 한 점) · 넉넉한 여백 · 관계·흐름·일정은 글이 아니라 그림으로 · 단일 자체완결 파일 · print/반응형/접근성. 상세는 [`SKILL.md`](SKILL.md).

> ⚠️ **`<style>`·라이트박스 `<script>`·print 규칙은 검증된 값이라 건드리지 않습니다.** 내용(`<body>`)만 채웁니다.

---

## 🖼 이미지 인라인 (단일 파일 만들기)

보고서에 로컬 이미지(사진·캡처)를 넣었다면, 파일 하나만 공유해도 이미지가 보이도록 base64로 인라인할 수 있습니다. **이 단계에서만 Python이 필요**합니다.

```bash
python scripts/inline_images.py report.html              # 같은 파일에 덮어쓰기
python scripts/inline_images.py report.html --out out.html
```

- `<img src="...">` 의 로컬 경로를 base64 data URI 로 치환 (UTF-8 고정, 한글 안전).
- `data:` / `http(s):` / `//` 로 시작하는 src 는 건드리지 않음.
- 외부 이미지·SVG 도식만 쓴 보고서는 이 단계가 필요 없습니다 (이미 단일 파일).

---

## 🤝 structured-writing 와 함께 쓰기

`html-report` 는 **"담는 그릇"**, [`structured-writing`](../structured-writing/) 은 **"쓰는 법"** 입니다. 보고서의 문장·단락 구성(핵심 한 문장·대조·쉬운 말·군더더기 제거)은 `structured-writing` 원칙을 따릅니다. **둘을 같이 설치**하면 디자인과 글이 한 번에 잡힙니다.

```bash
npx skills add EndoRobotics-Co-LTD/endo-skills -s html-report -s structured-writing
```

---

## 🔄 업데이트

템플릿·컴포넌트가 갱신되면 **재설치** 하면 됩니다:

```bash
# 기존 제거 후 다시 import
rm -rf ./.claude/skills/html-report      # 또는 ~/.claude/skills/html-report
npx skills add EndoRobotics-Co-LTD/endo-skills -s html-report
```

Claude Code 재시작 → 새 버전 적용. 배포 안내는 전사 공지 또는 [GitHub Releases](https://github.com/EndoRobotics-Co-LTD/endo-skills/releases).

---

## 🛠 문제 해결

| 증상 | 해결 |
|---|---|
| 스킬이 자동 발동 안 함 | Claude Code 완전 종료 후 재시작. `.claude/skills/html-report/SKILL.md` 존재 확인. |
| 이미지가 안 보임 (파일 공유 후) | `python scripts/inline_images.py report.html` 로 인라인 후 공유. |
| 폰트가 평소와 다르게 보임 | Pretendard CDN 미접속 시 시스템 폰트로 폴백 — 정상. 오프라인에서도 레이아웃은 유지됨. |
| 휴대폰 사진이 눕는다(회전) | EXIF 방향 정보 때문. 픽셀을 실제로 회전(보통 CW 90°)해 저장 후 재삽입. |
| `python` 명령을 못 찾음 | 이미지 인라인을 쓸 때만 Python 필요. https://python.org 에서 설치하거나, 외부 이미지/도식만 사용. |
| 렌더가 깨져 보임 | `<style>`/`<script>` 를 건드리지 않았는지 확인. 템플릿에서 새로 시작 권장. |
| git clone 시 `Authentication failed` | public 리포라 인증 불필요. 그래도 막히면 전략기획팀 이은상에게 문의. |

---

## 🔧 관리자용 (디자인 표준 변경)

회사 표준 보고서 디자인을 바꿀 때:

1. [`assets/template.html`](assets/template.html) 의 `<style>`(CSS 변수·컴포넌트) 또는 컴포넌트 마크업을 수정.
2. 새 시각 컴포넌트를 추가하면 [`SKILL.md`](SKILL.md) 의 컴포넌트 표도 함께 갱신.
3. 데모 섹션("시각화 컴포넌트 예시")으로 시각 QA.
4. Git push → 전사 공지 → 직원은 재설치로 받음.

> 색·여백·타이포는 검증된 값입니다. 임의 변경 대신 PR 리뷰로 표준을 바꾸세요.

---

## 📞 문의

| 종류 | 연락처 |
|---|---|
| 사용 문의 / 버그 리포트 | 전략기획팀 이은상 (eunsang.lee@endorobo.com) |
| 디자인 표준 변경 요청 | GitHub Issues 또는 전략기획팀 |
| 기여 (PR) | GitHub PR |

---

## 📜 라이센스

EndoRobotics 사내용 — 외부 배포 금지.
