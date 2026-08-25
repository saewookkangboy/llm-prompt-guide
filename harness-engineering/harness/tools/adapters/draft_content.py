"""draft_content 어댑터 — 초안 저장. 외부 공개 없음."""

from harness.tools.errors import ToolError

MAX_OUTPUT_CHARS = 4000   # policy.yaml constraints와 일치


def call(channel: str, body: str, title: str | None = None) -> dict:
    """초안을 저장하고 {"content_id", "channel", "char_count"}를 반환한다."""
    raise NotImplementedError
