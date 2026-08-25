"""워크플로 종단 실행 — 픽스처 기반, 실제 모델 호출 없음.

품질이 아니라 하네스 동작을 본다: 예산 초과 시 멈추는가, 검색 0건에서
실패하는가, 정책에 없는 툴이 거부되는가.
"""

import pytest


@pytest.mark.xfail(reason="미구현 스캐폴드")
def test_halts_on_budget_exceeded():
    """예산 초과 시 halt_reason과 부분 산출물을 함께 반환한다."""
    raise NotImplementedError


@pytest.mark.xfail(reason="미구현 스캐폴드")
def test_fails_on_empty_retrieval():
    """검색 0건은 빈 컨텍스트로 진행하지 않는다 (reg-2026-08-12-02)."""
    raise NotImplementedError


@pytest.mark.xfail(reason="미구현 스캐폴드")
def test_denied_tool_is_recorded():
    """거부된 호출 시도도 트레이스에 남아야 정책을 검증할 수 있다."""
    raise NotImplementedError


@pytest.mark.xfail(reason="미구현 스캐폴드")
def test_missing_fields_stop_before_research():
    """intake의 missing이 비어 있지 않으면 다음 단계로 넘어가지 않는다."""
    raise NotImplementedError
