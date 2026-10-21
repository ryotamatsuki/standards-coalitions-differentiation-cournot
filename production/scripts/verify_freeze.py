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
    versions = {"V2B-THEORY-FREEZE-2026-10-21-v1",
                "V2B-THEORY-FREEZE-2026-10-21-v2-CERT-REPAIR"}
    if manifest.get("freeze_id") not in versions:
        raise SystemExit("Unknown freeze identifier")
    if manifest["freeze_id"].endswith("v2-CERT-REPAIR"):
        if manifest.get("parent_freeze_id") != "V2B-THEORY-FREEZE-2026-10-21-v1":
            raise SystemExit("V2 must preserve explicit v1 provenance")
        for name in ("verification/v2b_exact_rational_interval.py",
                     "docs/V2B_THEORY_FREEZE_2026-10-21_v2.md"):
            if name not in manifest["frozen_files"]:
                raise SystemExit("Required v2 evidence missing: " + name)
        # Independent immutable source anchors that cannot be silently re-keyed.
        anchors = {
            "docs/V2B_THEORY_FREEZE_2026-10-21_v1.md":
                "ca16f0d4699364c7466d463c40e01cb5eaa2d8e5",
            "formal/V2bWelfareCore.lean":
                "b93d4564c4e29093bea1e3e006d2e9865d627c2f",
            "verification/v2b_stage04a_krawczyk_cleanroom.py":
                "25cb3b15cff6e50f7ee1bc5b0e1657300c8c306f"
        }
        for path, sha in anchors.items():
            if manifest["frozen_files"].get(path) != sha:
                raise SystemExit("Unchanged historical source SHA drift: " + path)
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
