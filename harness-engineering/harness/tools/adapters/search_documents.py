"""search_documents 어댑터."""

from harness.tools.errors import ToolError

MAX_RETRIES = 3


def call(query: str, collection: str = "all", top_k: int = 5) -> dict:
    """벡터 스토어를 조회하고 결과를 정규화한다.

    Returns:
        {"chunks": [{"id", "source", "text", "score"}], "truncated": bool}

    Raises:
        ToolError: 조회 실패 또는 컬렉션 없음. 메시지는 모델이 다음 행동을
            고를 수 있는 형태로 작성한다.
    """
    raise NotImplementedError
