"""요청 → 워크플로·모델 라우팅.

라우팅 규칙은 config/defaults.yaml에서 읽는다. 여기에 하드코딩하지 않는다 —
모델 티어 조정은 실험 대상이고, 실험은 배포 없이 돌 수 있어야 한다.
"""


def select_workflow(intake: dict) -> str:
    """구조화된 브리프를 보고 워크플로 ID를 고른다."""
    raise NotImplementedError


def select_model(step: str, complexity: str) -> str:
    """단계와 난이도로 모델 티어를 고른다.

    단순 추출·분류는 저비용 모델로 내린다. 전체를 최상위 모델로 돌리는 것은
    품질 전략이 아니라 비용 설계의 부재다.
    """
    raise NotImplementedError
