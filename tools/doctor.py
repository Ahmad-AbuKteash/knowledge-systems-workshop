"""Check readiness without API calls or exposing credentials."""
import importlib.metadata
import os
from pathlib import Path
import shutil
import sqlite3
import sys

ROOT = Path(__file__).resolve().parents[1]


def main():
    failures = []
    print(f"Python {sys.version.split()[0]}; SQLite {sqlite3.sqlite_version}")
    if not (3, 12) <= sys.version_info[:2] <= (3, 14):
        failures.append("Use Python 3.12–3.14.")
    if sys.prefix == sys.base_prefix:
        failures.append("Run with the project's .venv Python.")
    if not shutil.which("git"):
        failures.append("Git is unavailable.")
    for package in ("markitdown", "openai", "python-dotenv"):
        try:
            print(f"{package}: {importlib.metadata.version(package)}")
        except importlib.metadata.PackageNotFoundError:
            failures.append(f"Install {package} using requirements.txt.")
    try:
        from markitdown import MarkItDown
        result = MarkItDown(enable_plugins=False).convert_local(str(ROOT / "sources/source-01/expenses-current.html"))
        if "USD 85" not in result.text_content:
            raise ValueError("expected text absent")
        print("PASS: synthetic HTML extraction preserves USD 85.")
    except Exception as error:
        failures.append(f"HTML smoke check failed: {type(error).__name__}.")
    try:
        from dotenv import load_dotenv
        load_dotenv(ROOT / ".env", override=False)
        print("API key: configured (not authenticated)" if os.environ.get("OPENAI_API_KEY", "").strip() else "API key: missing; needed for embed/search only")
    except ImportError:
        pass
    for failure in failures:
        print("FAIL:", failure)
    print("No API calls made. Billing, credentials, and other file formats are not verified.")
    return bool(failures)


if __name__ == "__main__":
    raise SystemExit(main())
