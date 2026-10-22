"""Verify the exact Stage11 v0.5 original 23-file GitHub extraction.

Run: python stage11_v05_package/verify_github_package.py
Uses Python stdlib for file integrity. Optional NumPy verifies recorded phase counts.
This does NOT certify the numerical phase boundaries or publication claims.
"""
from pathlib import Path
import hashlib
import json
import sys

root = Path(__file__).resolve().parent
manifest = json.loads((root / 'SOURCE_FILE_HASHES.json').read_text())['files']
errors = []
for name, rec in manifest.items():
    p = root / name
    if not p.is_file():
        errors.append(f'MISSING: {name}')
        continue
    content = p.read_bytes()
    got = hashlib.sha256(content).hexdigest()
    if len(content) != rec['size'] or got != rec['sha256']:
        errors.append(f'CONTENT MISMATCH: {name}: {len(content)} bytes / {got}')

if errors:
    print('\n'.join(errors), file=sys.stderr)
    raise SystemExit(1)
print(f'PASS: {len(manifest)} byte-identical archived files verified (SHA-256 and size)')

pdf = (root / 'manuscript/stage25_jpet_v05.pdf').read_bytes()
assert pdf.startswith(b'%PDF-'), 'Missing PDF signature'
print('PASS: original article PDF signature')

try:
    import numpy as np
except ImportError:
    print('SKIP: NumPy classification check (stdlib hash verification PASS)')
else:
    data = np.load(root / 'verification/figure3_boundary_aware_map.npz')
    F, N = data['F'], data['N']
    expected = {'F_SW': 765, 'F_IS': 916, 'N_SW': 1047, 'N_IS': 634}
    actual = {'F_SW': int((F == 0).sum()), 'F_IS': int((F == 2).sum()),
              'N_SW': int((N == 0).sum()), 'N_IS': int((N == 2).sum())}
    assert F.shape == N.shape == (41, 41), (F.shape, N.shape)
    assert actual == expected, (expected, actual)
    print('PASS: corrected Figure 3 candidate-label matrix shape and counts')

print('CAUTION: exact all-depth proof applies only to the certified benchmark/open neighborhood.')
print('The 2D phase image is exploratory classification, not an interval theorem.')
