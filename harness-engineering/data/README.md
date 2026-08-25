# data/

```
raw/         원본 (커밋하지 않음)
processed/   가공물·트레이스 (커밋하지 않음)
fixtures/    테스트용 소량 샘플 (커밋함)
```

## 규칙

- 실제 고객 데이터는 `raw/`에도 두지 않는다. 마스킹 후 반입한다
- 픽스처는 최소 크기로. 리뷰어가 diff를 읽을 수 있어야 한다
- 트레이스 보관은 30일 (`guardrails/policies/pii.yaml`의 `retain_days`와 일치)
