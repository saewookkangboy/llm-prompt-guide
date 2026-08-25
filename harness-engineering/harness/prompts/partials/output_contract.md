<!-- 모든 시스템 프롬프트가 공유하는 출력 계약. 여기만 고치면 전체에 반영된다. -->

응답은 아래 JSON 스키마를 따른다. 코드 펜스 밖에 설명을 덧붙이지 않는다.

```json
{
  "status": "ok | needs_input | halted",
  "result": { },
  "sources": [{"id": "...", "used_for": "..."}],
  "next_step": "...",
  "halt_reason": null
}
```

- `status`가 `halted`면 `halt_reason`은 반드시 채운다
- `sources`는 `result`에서 사용한 근거만 넣는다. 검색했지만 쓰지 않은 문서는 제외한다
- 스키마를 만족하지 못하면 부분 결과라도 `status: "halted"`로 낸다
