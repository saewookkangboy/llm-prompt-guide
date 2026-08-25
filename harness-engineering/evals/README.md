# evals/ — 평가

전략은 `docs/04-eval-strategy.md`. 여기는 자산이 있는 곳이다.

```
datasets/golden/       대표 업무의 정답 기준 (사람이 작성)
datasets/regression/   과거에 깨졌던 케이스 (실패 발생 즉시 추가)
datasets/adversarial/  인젝션·범위 이탈·PII 유도
rubrics/               LLM 저지 채점 기준
judges/                저지 프롬프트
suites/                스위트 정의 (무엇을 언제 돌리는가)
reports/               실행 결과 (커밋하지 않음)
```

## 케이스 형식 (JSONL)

```json
{"id": "gold-014", "input": "...", "expect": {"must_include": [], "must_not_include": [],
 "schema": "output_contract", "rubric": "strategy_quality"}, "tags": ["strategy"]}
```

## 하지 말 것

- 평가 케이스를 프롬프트 예시로 재사용 — 시험 문제를 교재에 넣는 것과 같다
- 모델이 만든 정답으로 골든셋 구성 — 그 모델의 편향을 그대로 통과시킨다
- 점수 하나로 요약 — 실패 **유형별** 분포를 본다
