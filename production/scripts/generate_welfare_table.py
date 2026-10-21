#!/usr/bin/env python3
"""Deterministically generate the Stage8 V2b baseline welfare table for LaTeX.

This is a *regime-continuation* diagnostic at EXACT g=1/20, theta witness.
It does NOT imply SU/IS are government equilibrium outcomes (they are not).
Only φ(x)=x canonical V2b is tabulated here. Do not import archival V1.
"""
import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "verification"))
from v2b_stage07_welfare_institutions import BASE, equilibrium, world  # noqa: E402

OUT = ROOT / "paper" / "generated" / "welfare_table.tex"
W_SW, W_SU_A, W_SU_C, W_IS = (2.422078421718, 2.421604947547,
                              2.440259596858, 2.439013049624)

def render() -> str:
    cases = [
        ("SW", equilibrium("SW", 0, BASE)),
        ("SU (AB)", equilibrium("SU", 0.05, BASE)),
        ("IS (ABC)", equilibrium("IS", 0.05, BASE)),
    ]
    sw, su, intl = [z for _, z in cases]
    checks = (
        (sw["W"][0], W_SW),
        (su["W"][0], W_SU_A),
        (su["W"][2], W_SU_C),
        (intl["W"][0], W_IS),
    )
    for actual, expected in checks:
        if abs(actual - expected) > 2e-8:
            raise AssertionError(f"Frozen Stage8 benchmark drift: {actual} vs {expected}")
    if not (su["W"][0] < sw["W"][0] < intl["W"][0] < su["W"][2]):
        raise AssertionError("Unexpected coalition welfare ordering")
    if not (world(intl) > world(su) > world(sw)):
        raise AssertionError("Unexpected world welfare ordering")
    rows = []
    for name, values in cases:
        rows.append(f"{name} & {values['CS']:.8f} & {values['W'][0]:.8f} "
                    f"& {values['W'][2]:.8f} & {world(values):.8f} " + r"\\")
    return (
        "% GENERATED FILE — DO NOT EDIT. Run: make table\n"
        "% Source: Stage8 frozen V2b; verification/v2b_stage07_welfare_institutions.py\n"
        r"\begin{table}[!htbp]" "\n"
        r"\centering" "\n"
        r"\caption{Conditional regime welfare at $g=0.05$ (normalized units)}" "\n"
        r"\label{tab:v2b-regime-welfare}" "\n"
        r"\begin{tabular}{lrrrr}" "\n"
        r"\hline" "\n"
        r"Regime & National CS & $W_A$ & $W_C$ & World welfare \\" "\n"
        r"\hline" "\n"
        + "\n".join(rows) + "\n"
        + r"\hline" "\n"
        + r"\end{tabular}" "\n"
        + r"\par\smallskip" "\n"
        + r"\begin{minipage}{0.94\linewidth}\footnotesize"
        + "These are downstream firm equilibrium continuation payoffs conditional "
        + "on each indicated standards regime, not on-path government agreements. "
        + "The canonical sequential government game implements no positive-depth "
        + "agreement at the certified witness."
        + r"\end{minipage}" "\n"
        + r"\end{table}" "\n"
    )

def main() -> None:
    parser = argparse.ArgumentParser()
    g = parser.add_mutually_exclusive_group(required=True)
    g.add_argument("--write", action="store_true")
    g.add_argument("--check", action="store_true")
    opts = parser.parse_args()
    result = render()
    if opts.write:
        OUT.parent.mkdir(parents=True, exist_ok=True)
        OUT.write_text(result, encoding="utf-8", newline="\n")
        print(f"WROTE {OUT.relative_to(ROOT)}")
    else:
        if not OUT.is_file() or OUT.read_text("utf-8") != result:
            raise SystemExit("Generated welfare table missing/out-of-date; run make table")
        print(f"VERIFIED {OUT.relative_to(ROOT)} deterministically matches frozen model")

if __name__ == "__main__":
    main()
