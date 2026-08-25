"""프롬프트 레지스트리 무결성."""

from pathlib import Path

import pytest
import yaml

REGISTRY = Path("harness/prompts/registry.yaml")
PROMPT_DIR = Path("harness/prompts")

registry = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
ENTRIES = registry["prompts"] + registry.get("deprecated", [])


@pytest.mark.contract
@pytest.mark.parametrize("entry", ENTRIES, ids=lambda e: e["path"])
def test_prompt_file_exists(entry):
    """이전 버전 파일도 남아 있어야 과거 트레이스를 재현할 수 있다."""
    assert (PROMPT_DIR / entry["path"]).exists()


@pytest.mark.contract
def test_one_active_version_per_id():
    active = [e["id"] for e in registry["prompts"] if e["stage"] == "active"]
    assert len(active) == len(set(active)), "같은 ID에 active 버전이 둘 이상이다"


@pytest.mark.contract
@pytest.mark.parametrize("entry", registry["prompts"], ids=lambda e: e["id"])
def test_includes_resolve(entry):
    """{{include: ...}}가 실재하는 partial을 가리키는지."""
    text = (PROMPT_DIR / entry["path"]).read_text(encoding="utf-8")
    for line in text.splitlines():
        if "{{include:" in line:
            target = line.split("{{include:")[1].split("}}")[0].strip()
            assert (PROMPT_DIR / target).exists(), f"{entry['id']}: {target} 없음"
