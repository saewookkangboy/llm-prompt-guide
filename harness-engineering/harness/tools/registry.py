"""툴 로딩과 권한 검사.

오케스트레이션은 어댑터를 직접 import 하지 않고 이 레지스트리를 통해서만
툴을 얻는다. 권한 검사를 우회할 경로를 하나로 줄이기 위해서다.
"""


def load_schemas(workflow: str, env: str) -> list[dict]:
    """워크플로가 선언한 툴 중 해당 환경에서 허용된 것만 스키마로 반환한다.

    필요 없는 툴을 컨텍스트에 넣지 않는다 — 토큰 낭비이자 오호출 원인이다.
    """
    raise NotImplementedError


def invoke(name: str, arguments: dict, *, env: str, run_id: str) -> dict:
    """정책 검사 → 파라미터 제약 검사 → 어댑터 호출 → 트레이스 기록."""
    raise NotImplementedError
