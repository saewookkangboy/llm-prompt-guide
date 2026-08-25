#!/usr/bin/env python
"""프롬프트 상태 승격 — registry.yaml을 수정하는 유일한 경로.

    python scripts/promote_prompt.py --id sys.copywriter --stage active

    draft → candidate → active → deprecated

승격 전 검사:
    candidate로: 파일 존재, 참조된 partial 존재
    active로:   해당 스위트 통과 + 기준선 대비 하락 없음 (하락 시 --force와 사유 필요)
    deprecated로: 대체 버전(replaced_by) 필수

레지스트리를 손으로 고치지 않는 이유는 승격 이력이 감사 로그로 남아야 하기
때문이다. 어떤 버전이 언제 왜 활성화됐는지 모르면 품질 회귀의 원인을 좁힐 수 없다.
"""

import argparse

STAGES = ("draft", "candidate", "active", "deprecated")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--id", required=True)
    parser.add_argument("--stage", required=True, choices=STAGES)
    parser.add_argument("--force", action="store_true", help="점수 하락에도 승격")
    parser.add_argument("--reason", help="--force 사용 시 필수")
    args = parser.parse_args()

    if args.force and not args.reason:
        parser.error("--force에는 --reason이 필요하다")
    raise NotImplementedError


if __name__ == "__main__":
    raise SystemExit(main())
