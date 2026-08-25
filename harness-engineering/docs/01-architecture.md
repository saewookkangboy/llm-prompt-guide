# 01. 아키텍처 — 레이어 경계

## 의존 방향

```
config ← context ← orchestration → tools
             ↑          ↓            ↓
          prompts   guardrails   observability
```

규칙 하나: **하위 레이어는 상위 레이어를 import 하지 않는다.**
`tools/`가 `orchestration/`을 참조하기 시작하면 툴을 단독으로 테스트할 수 없고,
계약 테스트가 무의미해진다.

## 레이어별 책임과 금지사항

### `harness/context/`
- **한다**: 검색 결과 랭킹, 메모리 요약, 토큰 예산 배분, 컨텍스트 직렬화
- **안 한다**: 모델 호출, 툴 실행
- 핵심 결정: 컨텍스트는 "많이"가 아니라 "정확히"다. 예산 초과 시 잘라내는
  순서는 `budget.py`에 명시적으로 정의한다 — 암묵적 truncation 금지.

### `harness/prompts/`
- **한다**: 프롬프트 텍스트 파일, 버전 레지스트리, 재사용 파셜
- **안 한다**: 로직. `.md` 안에 조건 분기를 넣지 말고 오케스트레이션에서 고른다.

### `harness/tools/`
- **한다**: JSON Schema 정의, 외부 API 어댑터, 권한 정책
- **안 한다**: 프롬프트 문자열 보유. 툴 설명은 스키마의 `description`에만.
- 어댑터는 순수 함수처럼 다룬다 — 같은 입력이면 같은 요청을 보낸다.

### `harness/orchestration/`
- **한다**: 라우팅, 상태 전이, 루프 종료 조건, 워크플로 조립
- **안 한다**: HTTP 호출 직접 수행 (어댑터에 위임)
- 루프는 반드시 종료 조건 3개를 갖는다: 성공, 최대 반복, 예산 초과.

### `harness/guardrails/`
- **한다**: 입력 차단, 출력 스키마 검증, 정책 평가
- **안 한다**: 조용한 수정. 차단하거나 통과시키되, 결과를 트레이스에 남긴다.

### `harness/observability/`
- **한다**: 트레이스 수집, 비용 집계, 메트릭 방출
- **안 한다**: 비즈니스 로직 분기. 관측이 동작을 바꾸면 관측이 아니다.

## 상태 모델

에이전트 실행 상태는 `orchestration/state.py` 한 곳에서만 정의한다.
레이어마다 자기 상태를 들고 있으면 루프 재시작 시 복원이 불가능해진다.

```python
RunState = {
    "run_id", "trace_id",
    "goal", "context_bundle", "scratchpad",
    "iteration", "tokens_used", "cost_usd",
    "status",  # planning | acting | reflecting | done | halted
}
```
