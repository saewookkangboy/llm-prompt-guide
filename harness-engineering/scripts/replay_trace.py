#!/usr/bin/env python
"""트레이스 조회·리플레이·평가 케이스 변환.

    python scripts/replay_trace.py --latest
    python scripts/replay_trace.py --since 24h --sort cost --top 20
    python scripts/replay_trace.py --since 1h --group-by halt_reason
    python scripts/replay_trace.py --run-id run_8f2a19c4 --to-case regression

--to-case가 개선 루프의 핵심 경로다. 실패한 실행을 평가 케이스로 바꿔
regression 셋에 넣는다. 이 경로가 없으면 관측은 대시보드 장식으로 끝난다.

리플레이는 트레이스에 기록된 프롬프트 버전으로 실행한다. 현재 active 버전으로
돌리면 "그때 왜 그랬는지"가 아니라 "지금 어떻게 되는지"를 보게 된다.
"""

import argparse


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--latest", action="store_true")
    parser.add_argument("--run-id")
    parser.add_argument("--since", help="예: 24h, 7d")
    parser.add_argument("--status", choices=["ok", "halted", "error"])
    parser.add_argument("--group-by", choices=["halt_reason", "tool_name", "workflow", "prompt_version"])
    parser.add_argument("--sort", choices=["cost", "latency", "iterations"])
    parser.add_argument("--top", type=int, default=20)
    parser.add_argument("--to-case", choices=["regression", "adversarial"])
    parser.add_argument("--show", help="쉼표 구분: sources,evicted,prompt_versions,tools")
    args = parser.parse_args()
    raise NotImplementedError


if __name__ == "__main__":
    raise SystemExit(main())
