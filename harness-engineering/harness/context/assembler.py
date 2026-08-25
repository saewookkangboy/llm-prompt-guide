"""컨텍스트 번들 조립 — 이 레이어의 유일한 진입점."""

from dataclasses import dataclass, field


@dataclass
class ContextBundle:
    system_prompt: str
    tool_schemas: list[dict]
    documents: list[dict] = field(default_factory=list)   # {id, source, text, score}
    memory: list[dict] = field(default_factory=list)
    conversation: list[dict] = field(default_factory=list)
    evicted: list[str] = field(default_factory=list)      # 절삭된 항목 ID
    token_estimate: int = 0


class EmptyContextError(RuntimeError):
    """검색 결과가 없어 근거 없이 답할 위험이 있는 경우."""


def assemble(goal: str, workflow: str, session_id: str) -> ContextBundle:
    """검색 → 메모리 → 예산 배분 순으로 번들을 만든다.

    검색 문서는 출처 태그로 감싸 넣는다. 태그 안의 텍스트는 데이터이지
    지시가 아니라는 점을 시스템 프롬프트가 명시한다 (docs/05-guardrails.md).
    """
    raise NotImplementedError
