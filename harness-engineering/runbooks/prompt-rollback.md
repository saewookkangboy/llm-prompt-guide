# 프롬프트 롤백

## 증상

배포 후 골든셋 통과율 급락, 스키마 검증 실패 증가, 재작업률 상승.

## 즉시 조치 (5분 이내)

1. 현재 활성 버전 확인
   ```bash
   grep -A3 "stage: active" harness/prompts/registry.yaml
   ```
2. 직전 버전으로 되돌린다
   ```bash
   make promote PROMPT_ID=sys.orchestrator STAGE=active   # 직전 버전 파일 지정
   ```
   프롬프트 파일은 버전마다 남아 있으므로 롤백에 배포가 필요 없다.
3. 롤백 후 스모크 확인
   ```bash
   make eval-smoke
   ```

## 원인 확인

```bash
python scripts/replay_trace.py --since 2h --status halted --group-by halt_reason
```

가장 흔한 두 가지:
- 출력 계약 인클루드 누락 → 스키마 실패 급증
- 지시 추가로 컨텍스트 예산 초과 → `budget_exceeded` 급증

## 복구

원인을 고친 새 버전을 `candidate`로 올리고 스모크 통과 후 `active`로 승격한다.
문제가 된 버전은 `deprecated`로 두되 **파일은 삭제하지 않는다** — 그 버전으로
실행된 트레이스를 재현해야 한다.

## 사후 조치

실패 케이스를 `evals/datasets/regression/`에 추가한다.
