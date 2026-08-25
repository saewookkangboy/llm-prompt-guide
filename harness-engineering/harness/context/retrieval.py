"""문서 검색과 랭킹."""

MAX_CHUNKS = 8
MIN_SCORE = 0.62   # 미달 시 개수가 모자라도 넣지 않는다


def search(query: str, top_k: int = MAX_CHUNKS) -> list[dict]:
    """관리형 벡터 스토어 조회. 반환 항목은 {id, source, text, score}."""
    raise NotImplementedError


def rerank(query: str, chunks: list[dict]) -> list[dict]:
    """리랭커로 재정렬 후 MIN_SCORE 미달 청크를 버린다."""
    raise NotImplementedError
