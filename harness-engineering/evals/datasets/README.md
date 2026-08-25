# datasets/

| 디렉터리 | 규모 | 갱신 주기 | 통과 기준 |
|---|---|---|---|
| `golden/` | 120건 | 분기 | ≥ 90% |
| `regression/` | 누적 | 실패 발생 즉시 | **100%** |
| `adversarial/` | 60건 | 월 | ≥ 95% |

회귀 셋은 100%가 아니면 배포하지 않는다. 한 번 고친 버그의 재발은
새 버그보다 신뢰를 크게 깎는다.

## 케이스 추가 경로

실패한 실행 → `scripts/replay_trace.py --to-case` → `regression/`
사람이 직접 작성 → `golden/`
보안 리뷰 → `adversarial/`
