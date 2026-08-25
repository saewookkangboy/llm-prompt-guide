"""출력 가드레일. 실패 시 1회 재시도 후 사람에게 에스컬레이션한다."""

from dataclasses import dataclass, field


@dataclass
class ValidationResult:
    valid: bool
    failures: list[str] = field(default_factory=list)
    escalate: bool = False


def validate(output: dict, *, contract: dict, workflow: str) -> ValidationResult:
    """순서대로 검사하고 실패를 모두 모아 반환한다 (첫 실패에서 멈추지 않는다).

    1. 출력 계약 스키마 유효성
    2. 근거 존재 — 주장에 대응하는 source ID가 있는가
    3. 금칙 표현
    4. 브랜드 톤 (정책 파일 기반, 저지 모델 아님)
    5. 예상 밖 툴 호출 — 워크플로가 허용하지 않은 툴을 부르려 했는가
    """
    raise NotImplementedError
