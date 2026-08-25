"""메트릭 방출.

대시보드(ops/dashboards/)가 읽는 지표. docs/00-overview.md의 성공 기준 4개와
1:1로 대응한다 — 대응하지 않는 지표는 늘리지 않는다.
"""

METRICS = (
    "atlas.golden_pass_rate",
    "atlas.rework_rate",
    "atlas.cost_per_run_usd",
    "atlas.latency_p95_seconds",
    # 진단용
    "atlas.loop_iterations",
    "atlas.guardrail_blocks",
    "atlas.tool_denials",
    "atlas.empty_retrieval",
)


def emit(name: str, value: float, **tags) -> None:
    raise NotImplementedError
