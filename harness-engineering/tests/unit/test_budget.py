"""토큰 예산 배분과 절삭 순서."""

import pytest

from harness.context import budget


def test_allocation_sums_to_one():
    assert abs(sum(budget.ALLOCATION.values()) - 1.0) < 1e-9


def test_eviction_order_excludes_fixed_sections():
    """시스템 프롬프트와 툴 스키마는 절삭 대상이 아니다."""
    assert "system_prompt" not in budget.EVICTION_ORDER
    assert "tool_schemas" not in budget.EVICTION_ORDER


@pytest.mark.xfail(reason="미구현 스캐폴드")
def test_evict_reports_removed_ids():
    """제거된 항목 ID를 반환해야 트레이스에 남길 수 있다."""
    plan = budget.plan(total_tokens=1000, fixed_tokens=200)
    _, removed = budget.evict({"retrieved_docs": [{"id": "d1"}] * 50}, plan)
    assert removed


@pytest.mark.xfail(reason="미구현 스캐폴드")
def test_raises_when_output_reserve_unreachable():
    """절삭 후에도 출력 여유분을 못 만들면 조용히 진행하지 않는다."""
    with pytest.raises(budget.BudgetExceededError):
        budget.plan(total_tokens=100, fixed_tokens=99)
