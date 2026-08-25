#!/usr/bin/env python
"""평가 스위트 실행.

    python scripts/run_eval.py --suite evals/suites/smoke.yaml
    python scripts/run_eval.py --suite evals/suites/release-gate.yaml --baseline eval_0819_base

3단 판정 순서 (docs/04-eval-strategy.md):
    1. 결정적 검사 — 스키마·필수 필드·금칙어. 실패 시 저지를 부르지 않는다 (비용 절약)
    2. LLM 저지 — 루브릭 채점
    3. 사람 표본 — 이 스크립트 밖, 주 단위

종료 코드는 CI 게이트가 읽는다. 임계 미달이면 1을 반환한다.
"""

import argparse


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--suite", required=True)
    parser.add_argument("--baseline", help="비교할 이전 실행 ID. 없으면 절대 점수만 보고")
    parser.add_argument("--out", default="evals/reports")
    args = parser.parse_args()

    # 리포트에는 절대 점수가 아니라 기준선 대비 변화량, 실패 케이스 ID 전체 목록,
    # 실패 유형별 분포, 비용·지연을 함께 담는다.
    raise NotImplementedError


if __name__ == "__main__":
    raise SystemExit(main())
