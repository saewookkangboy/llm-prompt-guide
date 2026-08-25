"""툴 스키마 ↔ 어댑터 ↔ policy.yaml 일치 검증.

이 테스트가 없으면 스키마만 고치고 어댑터를 안 고친 채 머지되고,
모델은 존재하지 않는 파라미터를 채워 보내다 런타임에 실패한다.
"""

import json
from pathlib import Path

import pytest
import yaml

SCHEMA_DIR = Path("harness/tools/schemas")
ADAPTER_DIR = Path("harness/tools/adapters")
POLICY = Path("harness/tools/policy.yaml")

SCHEMAS = sorted(SCHEMA_DIR.glob("*.json"))


@pytest.mark.contract
@pytest.mark.parametrize("path", SCHEMAS, ids=lambda p: p.stem)
def test_schema_has_required_keys(path):
    schema = json.loads(path.read_text(encoding="utf-8"))
    assert schema["name"] == path.stem
    assert len(schema["description"]) >= 40, "설명이 모델이 읽는 유일한 사용 설명서다"
    assert "input_schema" in schema


@pytest.mark.contract
@pytest.mark.parametrize("path", SCHEMAS, ids=lambda p: p.stem)
def test_every_schema_has_adapter(path):
    assert (ADAPTER_DIR / f"{path.stem}.py").exists()


@pytest.mark.contract
@pytest.mark.parametrize("path", SCHEMAS, ids=lambda p: p.stem)
def test_every_schema_registered_in_policy(path):
    policy = yaml.safe_load(POLICY.read_text(encoding="utf-8"))
    registered = set()
    for env in policy["environments"].values():
        for key in ("allow", "dry_run", "deny", "require_human_approval"):
            registered.update(env.get(key, []))
    assert path.stem in registered, "policy에 없는 툴은 호출될 수 없다 — 등록 누락"


@pytest.mark.contract
def test_irreversible_tools_require_approval_in_prod():
    policy = yaml.safe_load(POLICY.read_text(encoding="utf-8"))
    prod = policy["environments"]["prod"]
    guarded = set(prod.get("require_human_approval", [])) | set(prod.get("deny", []))
    for path in SCHEMAS:
        schema = json.loads(path.read_text(encoding="utf-8"))
        if schema.get("x-side-effects") == "irreversible":
            assert schema["name"] in guarded, f"{schema['name']}: 되돌릴 수 없는 툴에 승인 요건이 없다"
