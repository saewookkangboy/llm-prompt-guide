# 다이어그램

소스는 텍스트로 관리한다 (Mermaid `.mmd`). PNG만 커밋하면 6개월 뒤에 수정할 수 없다.

| 파일 | 내용 |
|---|---|
| `layer-flow.mmd` | 요청 → 6레이어 → 응답 흐름 |
| `loop-cycle.mmd` | 런타임 루프 상태 전이 |
| `eval-gate.mmd` | PR부터 배포까지 평가 게이트 |

렌더링: `mmdc -i layer-flow.mmd -o layer-flow.svg`
