# structured-writing — EndoRobotics 구조적 글쓰기

> AI가 한국어 글(보고서·제안문·발표문·회의록·공지·이메일)을 **"논지가 분명히 서고 잘 읽히게"** 다듬어주는 Claude Code Skill.
> 누가 쓰든 같은 원칙 — 한 단위 한 메시지, 대조('A가 아니라 B'), 쉽지만 정확한 말, 군더더기 제거 — 으로 글의 뼈대를 잡습니다.

---

## 목차

1. [한 줄 요약](#한-줄-요약)
2. [사전 요구사항](#-사전-요구사항)
3. [설치 (1회)](#-설치-1회)
4. [어떻게 쓰나 — 자동 발동](#-어떻게-쓰나--자동-발동)
5. [무엇을 해주나](#-무엇을-해주나)
6. [html-report 와 함께 쓰기](#-html-report-와-함께-쓰기)
7. [업데이트](#-업데이트)
8. [문제 해결](#-문제-해결)
9. [문의](#-문의)
10. [라이센스](#-라이센스)

---

## 한 줄 요약

```bash
npx skills add EndoRobotics-Co-LTD/endo-skills -s structured-writing
```

→ Claude Code 재시작 → 평소처럼 **"이 글 다듬어줘"** / **"보고서 써줘"** 라고 하면 자동 적용.

- 기본 동작: **현재 폴더의 `.claude/skills/structured-writing/` 에 설치** (project-local).
- 모든 프로젝트에서 쓰려면 `-g` 추가.
- **추가 의존성 없음.** 순수 방법론 스킬이라 설치 즉시 동작합니다 (Python·패키지 불필요).

---

## 📋 사전 요구사항

| 항목 | 버전/조건 |
|---|---|
| **OS** | 무관 (Windows / macOS / Linux) |
| **Claude Code** | 최신 버전 |
| **추가 런타임** | 없음 — 콘텐츠 전용 스킬 |
| **GitHub 접근권** | `EndoRobotics-Co-LTD/endo-skills` (public, 인증 불필요) |
| **언어** | 한국어 글쓰기 전용 |

---

## ⚡ 설치 (1회)

### 방법 A — `npx skills add` (가장 표준)

```bash
npx skills add EndoRobotics-Co-LTD/endo-skills -s structured-writing
```

- 기본: 현재 폴더의 `.claude/skills/structured-writing/` 에 설치 (project-local).
- 글로벌은 `-g` 추가: `npx skills add EndoRobotics-Co-LTD/endo-skills -s structured-writing -g`

### 방법 B — 수동 (자동이 실패하면)

```powershell
# 1) 임시 폴더에 repo 클론
$temp = Join-Path $env:TEMP "endo-skills-clone"
git clone --depth 1 https://github.com/EndoRobotics-Co-LTD/endo-skills.git $temp

# 2) structured-writing 만 정확한 위치로 이동 (project-local 예시)
New-Item -ItemType Directory -Force .\.claude\skills | Out-Null
Move-Item "$temp\skills\structured-writing" ".\.claude\skills\structured-writing"
Remove-Item -Recurse -Force $temp
```

### 설치 후 한 번

**Claude Code를 한 번 종료했다가 다시 실행하세요.** 그래야 새 스킬이 인식됩니다.

> ✅ 별도 패키지 설치가 없으므로 설치 = 끝. 확인은 `.claude/skills/structured-writing/SKILL.md` 파일이 있으면 OK.

---

## 🎬 어떻게 쓰나 — 자동 발동

설치 후엔 **그냥 평소처럼** 글쓰기·편집을 요청하면 됩니다. '구조'라는 단어를 안 써도 글쓰기 작업이면 자동으로 발동합니다.

```
이 보고서 다듬어줘
```

```
경영진 보고용으로 핵심이 서게 정리해줘
```

```
이 제안서 설득력 있게 고쳐줘. 장황한 것 같아.
```

```
회의록 결정·액션이 한눈에 들어오게 써줘
```

발동 트리거 예: "구조 잡아줘", "논리적으로/체계적으로", "다듬어줘", "핵심이 안 산다", "장황하다", "설득력 있게", 그리고 보고서/제안서/발표자료/회의록/공지 작성.

---

## 🧭 무엇을 해주나

글을 **나열**이 아니라 **하나의 메시지를 박아넣는 구조**로 다시 세웁니다. 핵심 7원칙:

| 원칙 | 한 줄 |
|---|---|
| 1. 하나의 메시지 | 글 전체에 한 문장, 단락마다 한 메시지. 기억에 남는 '구절'로 주조해 반복. |
| 2. 대조로 날 세우기 | 핵심을 'A가 아니라 B' 꼴로, 따옴표로 두 축을 시각 분리. |
| 3. 핵심 문장 주인공화 | 단락 핵심은 한 문장으로 강조, 부연·근거는 아래로 강등. |
| 4. 쉽게, 그러나 정확하게 | 무조건 풀지 말고 *가장 명확히 가리키는 표현*을 고른다. |
| 5. 하나의 구체로 착지 | 추상 → 구체(숫자·예시 하나) → 더 날카로운 주장. |
| 6. 수렴하고 끌어올린다 | 글 전체를 한 문장으로 결정화, 시선을 사람·목적으로. |
| 7. 덜어낸다 | 과정 서술·헤지·일반론·중복 삭제. *단, 장르를 본다* (회고·설득 글은 목적 있는 곁말 허용). |

형식별(보고서·제안문·발표문·회의록·에세이)로 배치를 달리 적용하며, 복잡한 관계·일정은 **글 대신 시각화**(→ `html-report`)를 권합니다.

상세 원칙·Before/After 예시·체크리스트는 [`SKILL.md`](SKILL.md) 참고.

---

## 🤝 html-report 와 함께 쓰기

이 스킬은 **"쓰는 법"**, [`html-report`](../html-report/) 는 **"담는 그릇"** 입니다. HTML 보고서를 만들 때 두 스킬이 짝으로 동작합니다 — `html-report` 가 디자인·컴포넌트를, `structured-writing` 이 문장·단락 구성을 책임집니다.

```bash
# 보고서 작업을 자주 한다면 둘 다 설치 권장
npx skills add EndoRobotics-Co-LTD/endo-skills -s structured-writing -s html-report
```

---

## 🔄 업데이트

원칙이 갱신되면 **재설치** 하면 됩니다:

```bash
# 기존 제거 후 다시 import
rm -rf ./.claude/skills/structured-writing      # 또는 ~/.claude/skills/structured-writing
npx skills add EndoRobotics-Co-LTD/endo-skills -s structured-writing
```

Claude Code 재시작 → 새 버전 적용. 배포 안내는 전사 공지 또는 [GitHub Releases](https://github.com/EndoRobotics-Co-LTD/endo-skills/releases).

---

## 🛠 문제 해결

| 증상 | 해결 |
|---|---|
| 스킬이 자동 발동 안 함 | Claude Code 완전 종료 후 재시작. `.claude/skills/structured-writing/SKILL.md` 존재 확인. |
| 영어 글에 적용하려는데 안 맞음 | 이 스킬은 **한국어 전용**. 영어 글은 대상이 아님. |
| "더 덜어내라"는데 회고/에세이라 곁말을 살리고 싶다 | 정상 — 원칙 7의 *장르 예외*. "이건 에세이야, 목소리 살려줘"라고 명시. |
| git clone 시 `Authentication failed` | public 리포라 인증 불필요. 그래도 막히면 전략기획팀 이은상에게 문의. |

---

## 📞 문의

| 종류 | 연락처 |
|---|---|
| 사용 문의 / 버그 리포트 | 전략기획팀 이은상 (eunsang.lee@endorobo.com) |
| 원칙 변경 제안 | GitHub Issues 또는 전략기획팀 |
| 기여 (PR) | GitHub PR |

---

## 📜 라이센스

EndoRobotics 사내용 — 외부 배포 금지.
