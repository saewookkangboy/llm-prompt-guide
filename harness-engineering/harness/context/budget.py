"""토큰 예산 배분과 절삭 순서.

컨텍스트를 자르는 코드는 이 파일에만 있다. 다른 곳에서 문자열을 자르면
어떤 근거가 사라졌는지 트레이스에서 추적할 수 없다.
"""

from dataclasses import dataclass

# 구획별 비중. 합이 1.0을 넘으면 로드 시점에 실패한다.
ALLOCATION = {
    "retrieved_docs": 0.45,
    "conversation": 0.30,
    "memory": 0.15,
    "output_reserve": 0.10,
}

# 예산 초과 시 이 순서로 줄인다. 시스템 프롬프트와 툴 스키마는 대상이 아니다.
EVICTION_ORDER = ("retrieved_docs", "memory", "conversation")


@dataclass
class BudgetPlan:
    total: int
    per_section: dict[str, int]
    reserved_for_output: int


class BudgetExceededError(RuntimeError):
    """절삭 후에도 출력 여유분을 확보하지 못한 경우."""


def plan(total_tokens: int, fixed_tokens: int) -> BudgetPlan:
    """고정 구획(시스템 프롬프트·툴 스키마)을 제외한 나머지를 배분한다."""
    raise NotImplementedError


def evict(sections: dict[str, list], plan: BudgetPlan) -> tuple[dict[str, list], list[str]]:
    """예산에 맞을 때까지 EVICTION_ORDER대로 제거한다.

    Returns:
        (남은 구획, 제거된 항목 ID 목록) — 제거 목록은 반드시 트레이스에 기록한다.
    """
    raise NotImplementedError
