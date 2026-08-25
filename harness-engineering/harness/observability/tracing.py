"""실행 트레이스."""

from contextlib import contextmanager


@contextmanager
def span(name: str, *, run_id: str, **attrs):
    """단계 하나를 감싼다. 예외가 나도 스팬은 닫히고 실패로 기록된다."""
    raise NotImplementedError


def record_prompt_version(run_id: str, step: str, prompt_id: str, version: str) -> None:
    """어떤 프롬프트 버전으로 돌았는지 기록 — 재현의 전제 조건."""
    raise NotImplementedError


def record_tool_call(run_id: str, name: str, args: dict, *, allowed: bool, error: str | None) -> None:
    """거부된 호출도 기록한다. 시도 자체가 정책 검증 데이터다."""
    raise NotImplementedError
