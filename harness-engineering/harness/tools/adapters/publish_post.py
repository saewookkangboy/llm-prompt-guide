"""publish_post 어댑터 — 되돌릴 수 없는 부작용을 가진 툴."""

from harness.tools.errors import ToolError, ApprovalRequired


def call(channel: str, content_id: str, scheduled_at: str | None = None, *, env: str) -> dict:
    """발행.

    dev/stage에서는 드라이런으로 페이로드만 반환한다.
    prod에서는 승인 토큰이 없으면 ApprovalRequired를 던진다 — 모델이 스스로
    승인할 수 없어야 하므로 승인 검사는 프롬프트가 아니라 여기서 한다.
    """
    raise NotImplementedError
