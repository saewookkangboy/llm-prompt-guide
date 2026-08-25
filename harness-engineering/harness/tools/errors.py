"""툴 레이어 공통 예외."""


class ToolError(RuntimeError):
    """모델에게 전달되는 툴 실패. 메시지는 다음 행동을 안내하는 형태로 쓴다."""

    def __init__(self, message: str, *, retryable: bool = False):
        super().__init__(message)
        self.retryable = retryable


class ApprovalRequired(ToolError):
    """사람 승인이 필요한 작업. 모델은 이 예외를 우회할 수 없다."""


class PolicyDenied(ToolError):
    """policy.yaml에서 거부된 호출. 시도 자체를 트레이스에 기록한다."""
