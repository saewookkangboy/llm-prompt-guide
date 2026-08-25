#!/usr/bin/env python
"""로컬 개발용 픽스처 적재.

data/fixtures/의 샘플을 로컬 스토어에 넣어 외부 API 없이 워크플로를 돌린다.
prod 환경에서는 실행을 거부한다.
"""

import os


def main() -> int:
    if os.getenv("ATLAS_ENV") == "prod":
        raise SystemExit("prod에서는 픽스처를 적재하지 않는다")
    raise NotImplementedError


if __name__ == "__main__":
    raise SystemExit(main())
