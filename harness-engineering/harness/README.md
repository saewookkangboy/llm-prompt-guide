# harness/ — 런타임 코드

6개 레이어. 의존 방향은 단방향(`docs/01-architecture.md`)이며, 새 파일을 놓을
자리가 애매하면 각 하위 디렉터리 README의 "넣는 것 / 넣지 않는 것"이 기준이다.

```
config/          모델·환경 설정        (모두가 읽음, 아무도 수정 안 함)
context/         컨텍스트 조립
prompts/         프롬프트 자산
tools/           툴 스키마·어댑터·권한
orchestration/   루프와 워크플로
guardrails/      차단과 검증
observability/   트레이스·비용·메트릭
```

## 새 기능을 추가할 때 건드리는 순서

1. `prompts/` — 지시를 파일로 작성, 레지스트리에 `draft`로 등록
2. `tools/` — 필요한 툴 스키마와 어댑터, `policy.yaml` 등록
3. `orchestration/workflows/` — 단계 정의
4. `evals/datasets/golden/` — 이 기능의 정답 케이스 최소 5건
5. `make eval-smoke` — 통과 후 프롬프트를 `candidate`로 승격
