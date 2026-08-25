"""비용 집계와 예산 차단."""

# 단가는 config/models.yaml에서 읽는다. 여기에 하드코딩하면 갱신이 누락된다.


def estimate(model: str, input_tokens: int, output_tokens: int) -> float:
    raise NotImplementedError


def check_budget(run_id: str, spent_usd: float, limit_usd: float) -> None:
    """한도 초과 시 BudgetExceeded를 던진다. 경고만 하고 계속 돌지 않는다."""
    raise NotImplementedError
