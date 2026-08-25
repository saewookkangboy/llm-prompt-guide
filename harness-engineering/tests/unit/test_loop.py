"""루프 종료 조건 — 셋 다 있어야 한다."""

from harness.orchestration import loop
from harness.orchestration.state import HaltReason, RunState, Status


def _state(**kw) -> RunState:
    base = dict(run_id="r1", trace_id="t1", goal="g", workflow="campaign_brief")
    return RunState(**{**base, **kw})


def test_stops_on_critique_pass():
    s = _state()
    assert loop.should_continue(s, {"verdict": "pass"}, max_iterations=6) is False
    assert s.status is Status.DONE


def test_stops_on_max_iterations_with_reason():
    """멈출 때 halt_reason이 없으면 관측되지 않는 실패가 된다."""
    s = _state(iteration=6)
    assert loop.should_continue(s, {"verdict": "fail"}, max_iterations=6) is False
    assert s.halt_reason is HaltReason.MAX_ITERATIONS


def test_continues_when_under_limit():
    s = _state(iteration=2)
    assert loop.should_continue(s, {"verdict": "fail"}, max_iterations=6) is True
