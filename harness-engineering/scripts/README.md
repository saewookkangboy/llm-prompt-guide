# scripts/ — 운영 스크립트

| 스크립트 | 용도 |
|---|---|
| `run_eval.py` | 스위트 실행, 리포트 생성 |
| `replay_trace.py` | 트레이스 조회·리플레이·평가 케이스 변환 |
| `promote_prompt.py` | 프롬프트 상태 승격 (레지스트리 수정의 유일한 경로) |
| `seed_fixtures.py` | 로컬 개발용 픽스처 적재 |

스크립트는 `harness/`를 import 하되, `harness/`는 스크립트를 import 하지 않는다.
