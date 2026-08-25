"""입력 가드레일."""

from dataclasses import dataclass


@dataclass
class FilterResult:
    allowed: bool
    reason: str | None = None
    redactions: list[str] = None   # 마스킹된 항목 유형


def check(user_input: str, *, env: str) -> FilterResult:
    """PII 탐지 → 인젝션 패턴 → 범위 이탈 순으로 검사한다.

    차단 시 사유를 반환한다. 사유 없는 차단은 사용자가 무엇을 고쳐야 할지
    알 수 없게 만들고, 결국 우회 시도를 유발한다.
    """
    raise NotImplementedError


def redact_pii(text: str) -> tuple[str, list[str]]:
    """주민등록번호·연락처·이메일·카드번호를 마스킹하고 유형 목록을 반환한다."""
    raise NotImplementedError
