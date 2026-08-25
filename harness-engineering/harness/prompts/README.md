# prompts/ — 프롬프트 자산

**넣는 것**: 프롬프트 텍스트(`.md`), 버전 레지스트리, 재사용 파셜
**넣지 않는 것**: 로직. 조건 분기는 오케스트레이션에서 프롬프트를 "고르는" 방식으로 처리한다.

```
system/      역할 프롬프트 (에이전트 1개당 1파일)
task/        작업 지시 프롬프트
partials/    여러 프롬프트가 공유하는 블록
registry.yaml  버전과 상태의 단일 출처
```

## 파일명 규칙

`<역할>.v<메이저>.md` — 예) `orchestrator.v3.md`

버전은 덮어쓰지 않고 새 파일로 만든다. 이전 버전이 남아 있어야 트레이스에
기록된 프롬프트로 실행을 재현할 수 있다.

## 상태

`draft → candidate → active → deprecated`

`scripts/promote_prompt.py`로만 바꾼다. `registry.yaml` 직접 편집 금지 —
승격 이력이 감사 로그로 남아야 한다.

## 작성 원칙

1. 역할·목표·제약·출력 형식 순서로 쓴다
2. 출력 계약은 `partials/output_contract.md`를 인클루드해 중복을 없앤다
3. 예시는 2~3개. 많을수록 그 형태에 과적합한다
4. 평가셋 케이스를 예시로 쓰지 않는다 (docs/04-eval-strategy.md)
