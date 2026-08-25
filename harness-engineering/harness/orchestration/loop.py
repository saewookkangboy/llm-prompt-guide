"""런타임 루프 (docs/03-loop-engineering.md).

계획 → 실행 → 자기평가 → (미달이면 재계획)
"""

from harness.orchestration.state import HaltReason, RunState, Status

MAX_ITERATIONS = 6


def run(state: RunState, *, max_iterations: int = MAX_ITERATIONS) -> RunState:
    """종료 조건 세 가지를 모두 검사하며 루프를 돈다.

    자기평가는 반드시 별도 호출(`task.self_critique`)로 실행한다. 본 프롬프트에
    "잘 했는지 확인해"를 덧붙이면 모델은 거의 항상 자기 결과를 통과시킨다.
    """
    raise NotImplementedError


def should_continue(state: RunState, critique: dict, max_iterations: int) -> bool:
    """계속 돌지 판단하고, 멈춰야 하면 state에 halt_reason을 채운다."""
    if critique.get("verdict") == "pass":
        state.status = Status.DONE
        return False
    if state.iteration >= max_iterations:
        state.halt(HaltReason.MAX_ITERATIONS)
        return False
    return True
