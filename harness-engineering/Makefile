.PHONY: install lint test eval-smoke eval-full trace promote clean

install:            ## 의존성 설치
	pip install -e ".[dev]"

lint:               ## 포맷·정적 검사
	ruff check harness scripts tests
	ruff format --check harness scripts tests

test:               ## 단위·계약 테스트
	pytest tests/unit tests/contract -q

eval-smoke:         ## 골든셋 20건 (PR 필수)
	python scripts/run_eval.py --suite evals/suites/smoke.yaml

eval-full:          ## 전체 스위트 (릴리스 게이트)
	python scripts/run_eval.py --suite evals/suites/release-gate.yaml

trace:              ## 최근 실행 트레이스 리플레이
	python scripts/replay_trace.py --latest

promote:            ## 프롬프트 승격 (PROMPT_ID=... STAGE=active)
	python scripts/promote_prompt.py --id $(PROMPT_ID) --stage $(STAGE)

clean:
	rm -rf .pytest_cache .ruff_cache __pycache__
