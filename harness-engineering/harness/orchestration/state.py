"""실행 상태 — 단일 정의.

레이어마다 자기 상태를 들고 있으면 루프 재시작 시 복원이 불가능하다.
상태 필드를 추가할 일이 생기면 여기에 추가한다.
"""

from dataclasses import dataclass, field
from enum import Enum


class Status(str, Enum):
    PLANNING = "planning"
    ACTING = "acting"
    REFLECTING = "reflecting"
    DONE = "done"
    HALTED = "halted"


class HaltReason(str, Enum):
    SELF_CRITIQUE_FAILED = "self_critique_failed"
    MAX_ITERATIONS = "max_iterations"
    BUDGET_EXCEEDED = "budget_exceeded"
    GUARDRAIL_BLOCKED = "guardrail_blocked"
    TOOL_UNAVAILABLE = "tool_unavailable"
    APPROVAL_REQUIRED = "approval_required"


@dataclass
class RunState:
    run_id: str
    trace_id: str
    goal: str
    workflow: str
    status: Status = Status.PLANNING
    iteration: int = 0
    tokens_used: int = 0
    cost_usd: float = 0.0
    scratchpad: list[dict] = field(default_factory=list)
    artifacts: dict = field(default_factory=dict)
    halt_reason: HaltReason | None = None

    def halt(self, reason: HaltReason) -> None:
        """종료 사유 없이 멈추지 않는다 — 관측되지 않는 실패를 만들지 않기 위해."""
        self.status = Status.HALTED
        self.halt_reason = reason
