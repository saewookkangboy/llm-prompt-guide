# tools/ — 툴 레이어

**넣는 것**: JSON Schema 정의, 외부 API 어댑터, 권한 정책
**넣지 않는 것**: 프롬프트 문자열, 오케스트레이션 의존. 툴 설명은 스키마의 `description`에만 쓴다.

```
schemas/    모델에게 노출되는 툴 정의 (JSON Schema)
adapters/   실제 호출 구현
policy.yaml 환경별 허용·거부와 승인 요건
```

## 툴 하나를 추가하는 절차

1. `schemas/<name>.json` — 이름·설명·파라미터
2. `adapters/<name>.py` — 구현. 같은 입력이면 같은 요청을 보낸다
3. `policy.yaml` — 환경별 허용 등록 (**등록 전에는 호출 불가**)
4. `tests/contract/test_<name>.py` — 스키마와 구현 시그니처 일치 검증

## 스키마 작성 규칙

- `description`은 모델이 읽는 유일한 사용 설명서다. "언제 쓰는지"와 "언제 쓰지 않는지"를 같이 쓴다
- 파라미터는 최소로. 선택 파라미터가 늘수록 잘못된 호출이 늘어난다
- 자유 문자열보다 `enum`을 쓴다
- 부작용이 있는 툴은 이름에 동사를 명시한다 (`publish_`, `send_`)
