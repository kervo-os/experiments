# H5 flywheel re-run — pre-registration

Written 2026-07-07, **before the volume gate fired** (standing at
sessions 2/10, judged write-backs 3/10 at registration time). English
first; the Korean original follows verbatim.

This file's SHA-256 is anchored via OpenTimestamps at registration time
(`PREREG.md.ots` in this directory), so "the protocol predates the
results" is verifiable by a third party, not asserted by the authors.

## Prior hypothesis

**After the write-back flywheel has run under real production use —
volume gate: ≥ 10 artifact-present sessions and ≥ 10 judged write-backs
on the adopted repository — the artifact-only arm answers the original
5-question onboarding basis at ≥ 8.5/10 with ≤ 2 tool calls.**

Anchors already on record (not part of this run):

- Original eval (2026-07-06): artifact-only **5.5/10** at 1 tool call /
  21.2k tokens / 48s; full exploration **10/10** at 19 calls / 33.7k
  tokens / 184s.
- Mechanism pilot (2026-07-06): after 2 targeted captures, **9.5/10** —
  explicitly *not* the pre-registered re-run (2 questions, unblinded,
  same day).

## Trigger

The gate is mechanical, not calendrical: `gate.py` in this directory,
rules in `GATE.md`. Pinned at registration:

```
ee9b49aad6f1cefdadb7a429c1d7f2d503e3795737487f6df5892ff7214306c8  gate.py
29ff9a9a1697c9441b18083a5bf568ced32a59ca1286bee953fafb6ce8fb4d9d  GATE.md
```

The run executes at the first `FIRE` output; the counts at fire time are
reported verbatim.

## Design

1. **Same question basis**: the original eval's 5 onboarding questions,
   reused verbatim (held in the private workspace's eval notes; their
   SHA-256 is declared in the run report so reuse is checkable).
2. **Arm A (measured)**: a fresh consumer session receives the current
   compiled artifact only — no repository access, no conversation
   history. One session per question set.
3. **Reference points**: the 2026-07-06 artifact-only baseline (5.5/10)
   and exploration ceiling (10/10) serve as historical controls; the
   exploration arm is **not** re-run (its cost profile is not under
   test).
4. **Judging**: same rubric and ground truth as the original eval; the
   judge is a fresh agent session, blind to the hypothesis and to which
   artifact version produced the answers.

## Declared metrics and criteria

- **Primary**: mean score across the 5-question basis (0–10), plus tool
  calls used.
- **Pass**: mean ≥ 8.5/10 **and** tool calls ≤ 2.
- **Reject**: mean ≤ 6.5/10.
- Otherwise: partial support.
- **Secondary** (reported, not gating): hallucination count (must be 0
  to claim the trust mechanism held), token cost, wall time.

## Declared honesty notes

- The accumulated knowledge includes captures deliberately targeted at
  2 of the 5 questions during the pilot. This is not leakage; it is the
  product working as designed — the flywheel exists precisely to turn
  observed gaps into captured answers. It is declared so readers weigh
  it.
- Agent-judged (the human-grading replication kit remains unexecuted,
  as in H4). Single repository. Historical-control comparison, not
  re-randomized.

---

## 원문 (Korean original, verbatim)

# H5 플라이휠 재실행 — 사전 등록 (2026-07-07, 게이트 발화 전 작성)

등록 시점 게이트: 세션 2/10, 판정된 write-back 3/10. 이 파일의 SHA-256은
등록 시점에 OpenTimestamps로 앵커됨(`PREREG.md.ots`) — "프로토콜이 결과보다
먼저"를 저자 주장이 아니라 제3자 검증 가능한 사실로 만든다.

## 사전 가설

**write-back 플라이휠이 실운영에서 볼륨 게이트(입양 레포 기준 artifact 동반
세션 ≥ 10 + 판정된 write-back ≥ 10)만큼 돌고 난 뒤, artifact 단독 암은
원래의 5문항 온보딩 기준을 도구 호출 ≤ 2회로 평균 ≥ 8.5/10에 답한다.**

기준점(기록됨, 본 런 아님): 원 평가 artifact 단독 5.5/10 (1콜/21.2k
토큰/48초), 전체 탐색 10/10 (19콜/33.7k/184초); 기제 파일럿 9.5/10
(2문항 표적 캡처 후, 비블라인드 — 사전등록 재실행이 아님을 명시).

## 트리거

달력이 아니라 기계: 이 디렉토리의 `gate.py`(규칙은 `GATE.md`), 위 해시로
고정. 첫 `FIRE` 출력 시 실행, 발화 시점 카운트는 그대로 보고.

## 설계

1. **같은 문항**: 원 평가의 온보딩 5문항 그대로 재사용(비공개 워크스페이스
   평가 노트에 보관, 해시는 런 보고서에 선언).
2. **A 암(측정 대상)**: 신선한 소비자 세션에 현재 컴파일된 artifact만 제공
   — 레포 접근·대화 이력 없음.
3. **참조점**: 2026-07-06의 artifact 단독 5.5/10과 탐색 상한 10/10을 역사적
   대조군으로 사용; 탐색 암은 재실행하지 않음(그쪽 비용 프로파일은 검증
   대상이 아님).
4. **채점**: 원 평가와 같은 루브릭·정답 기준; 심판은 가설과 artifact 버전을
   모르는 신선한 에이전트 세션.

## 선언된 지표·기준

- **주지표**: 5문항 평균(0–10) + 사용 도구 호출 수
- **통과**: 평균 ≥ 8.5/10 그리고 호출 ≤ 2 / **기각**: 평균 ≤ 6.5 / 그 외 부분 지지
- **부지표**(보고용): 환각 수(신뢰 기제 주장엔 0이어야 함), 토큰, 시간

## 정직성 선언

- 축적된 지식엔 파일럿 때 5문항 중 2문항을 표적으로 한 의도적 캡처가
  포함된다. 이는 누출이 아니라 설계된 제품 동작(플라이휠은 관찰된 공백을
  캡처된 답으로 바꾸라고 존재한다)이며, 독자가 가중하도록 선언해 둔다.
- 에이전트 채점(사람 채점 복제 킷은 H4와 마찬가지로 미실행). 단일 레포.
  역사적 대조군 비교(재무작위화 아님).
