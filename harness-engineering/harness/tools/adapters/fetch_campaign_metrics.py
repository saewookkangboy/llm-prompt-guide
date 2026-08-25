"""fetch_campaign_metrics 어댑터."""

from harness.tools.errors import ToolError

MAX_RANGE_DAYS = 180   # policy.yaml의 constraints와 일치해야 한다 (contract 테스트가 검증)


def call(campaign_id: str, start_date: str, end_date: str, metrics: list[str] | None = None) -> dict:
    """광고 플랫폼 API 조회. 기간 상한을 넘으면 호출 전에 ToolError를 던진다."""
    raise NotImplementedError
