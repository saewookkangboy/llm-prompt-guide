# workflows/ — 단계 정의

워크플로 하나당 YAML 하나. 스키마는 `graph.py`의 `load()`가 검증한다.

## 필수 키

`id` · `version` · `budget` · `steps` · `outputs.required`

## 단계 하나의 필수 키

`id` · `prompt`(레지스트리 ID) · `model_tier` · `tools`(허용 목록)

## 규칙

- 프롬프트는 파일 경로가 아니라 **레지스트리 ID**로 참조한다. 버전 승격이
  워크플로 수정 없이 반영되어야 한다.
- `tools`는 그 단계에서만 쓸 툴로 좁힌다. 전 단계에 전체 툴을 노출하면
  오호출이 늘고 토큰이 샌다.
- `version`을 올리면 실험 기록(`experiments/`)에 어떤 버전이었는지 남긴다.
