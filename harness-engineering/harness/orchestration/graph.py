"""워크플로 YAML → 실행 그래프."""


def load(workflow_id: str) -> dict:
    """workflows/<id>.yaml을 읽고 검증한다.

    검증 항목: 단계 참조 무결성, 순환 없음, 선언된 툴이 policy에 존재,
    참조된 프롬프트 ID가 registry에서 active 또는 candidate 상태.
    """
    raise NotImplementedError


def execute(graph: dict, state) -> None:
    """단계를 순서대로 실행하며 state를 갱신한다."""
    raise NotImplementedError
