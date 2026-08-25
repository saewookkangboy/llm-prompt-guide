# 비용 급증

## 증상

`atlas.cost_per_run_usd`가 기준선의 2배 이상, 또는 일일 예산 알림.

## 즉시 조치

1. 실행별 비용 상위 확인
   ```bash
   python scripts/replay_trace.py --since 24h --sort cost --top 20
   ```
2. 반복 횟수 분포 확인 — 루프가 도는 것이 대개의 원인이다
   ```bash
   python scripts/replay_trace.py --since 24h --metric loop_iterations --histogram
   ```
3. 필요하면 환경 설정에서 한도를 임시로 조인다
   ```yaml
   # harness/config/environments/prod.yaml
   budget: {max_cost_usd_per_run: 1.00}
   ```

## 원인 확인

| 신호 | 원인 |
|---|---|
| 반복 횟수 평균 상승 | 자기평가가 계속 fail — 프롬프트 또는 루브릭 문제 |
| 입력 토큰 급증 | 컨텍스트 절삭 미작동, 검색 청크 과다 |
| deep 티어 비중 상승 | 라우팅 규칙 변경 또는 폴백 반복 발생 |
| 툴 호출 급증 | 재시도 루프 — 어댑터 실패가 모델 재시도를 유발 |

## 복구

원인 항목을 하나만 되돌린다. 여러 개를 동시에 조정하면 무엇이 효과였는지
알 수 없어 다음 급증 때 같은 조사를 반복하게 된다.

## 사후 조치

비용을 유발한 케이스를 회귀 셋에 추가하고, 해당 스위트에 `max_cost_usd` 임계를 건다.
