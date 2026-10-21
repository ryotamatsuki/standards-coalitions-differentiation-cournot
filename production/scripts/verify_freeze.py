#!/usr/bin/env python3
"""Read-only Stage8 model/code freeze integrity guard (no network or dependencies).

Checks Git *blob* SHA-1 on checked-out bytes, exactly matching freeze_manifest.json.
Do not silently refresh hashes: a changed primitive or theorem requires rollback
to affected research gates and a new freeze identifier.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def blob_sha(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()

def main() -> None:
    manifest = json.loads((ROOT / "production" / "freeze_manifest.json").read_text("utf-8"))
    assert manifest["freeze_id"] == "V2B-THEORY-FREEZE-2026-10-21-v1", "Unknown freeze ID"
    errors = []
    for path, expected in manifest["frozen_files"].items():
        file = ROOT / path
        if not file.is_file():
            errors.append(f"MISSING: {path}")
            continue
        actual = blob_sha(file.read_bytes())
        if actual != expected:
            errors.append(f"DRIFT: {path} expected={expected} actual={actual}")
        else:
            print("FROZEN OK", path, actual)
    if errors:
        raise SystemExit("FROZEN THEORY VIOLATION:\n" + "\n".join(errors))
    print(f"STAGE8 FREEZE VERIFIED: {len(manifest['frozen_files'])} file blobs, {manifest['freeze_id']}")

if __name__ == "__main__":
    main()
