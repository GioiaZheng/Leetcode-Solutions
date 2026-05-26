from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SECURITY_SCAN_PATH = ROOT / "scripts" / "security_scan.py"


def load_security_scan():
    spec = spec_from_file_location("security_scan", SECURITY_SCAN_PATH)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


security_scan = load_security_scan()


def test_security_scan_reports_high_confidence_secret_patterns(tmp_path):
    sample = tmp_path / "sample.py"
    fake_key = "sk-" + "proj-" + "abcdefghijklmnopqrstuvwxyz123456"
    sample.write_text(f'OPENAI_API_KEY = "{fake_key}"\n')

    findings = security_scan.scan_repository(tmp_path)

    assert [finding[0] for finding in findings] == ["OpenAI API key"]
    assert findings[0][1] == sample
    assert findings[0][2] == 1


def test_security_scan_ignores_common_algorithm_words(tmp_path):
    sample = tmp_path / "notes.md"
    sample.write_text(
        "This graph problem has a secret, token variable, and password complexity.\n",
        encoding="utf-8",
    )

    assert security_scan.scan_repository(tmp_path) == []


def test_security_scan_reports_sensitive_filenames(tmp_path):
    env_file = tmp_path / ".env"
    env_file.write_text("DEBUG=true\n", encoding="utf-8")

    findings = security_scan.scan_repository(tmp_path)

    assert findings == [("sensitive filename", env_file, 0)]
