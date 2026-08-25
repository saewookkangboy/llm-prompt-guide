"""3계층 메모리 (docs/02-context-engineering.md).

working  실행 내 스크래치패드, 종료 시 폐기
session  세션 요약, TTL 24시간
org      브랜드 가이드·과거 캠페인. 사람 검토를 거친 것만 승격한다.
"""

TTL_SESSION_HOURS = 24


def read(session_id: str, layers: tuple[str, ...] = ("session", "org")) -> list[dict]:
    raise NotImplementedError


def write_session(session_id: str, summary: str) -> None:
    raise NotImplementedError


def propose_org_memory(candidate: dict) -> str:
    """조직 메모리 승격 후보를 큐에 넣는다. 자동 승격은 하지 않는다 —
    검증되지 않은 사실이 조직 메모리에 들어가면 모든 실행이 오염된다."""
    raise NotImplementedError
