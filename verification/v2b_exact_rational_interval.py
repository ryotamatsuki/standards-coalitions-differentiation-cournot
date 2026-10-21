#!/usr/bin/env python3
"""Verified coefficient-construction boundary for V2b interval certificates.

Numerical root proposals and logging may use floats; NEVER introduce binary64
coefficients inside rigorous proof interval expressions. Rational literals
in the SymPy expression trees are printed as RAT(p,q), which constructs
outward intervals from exact integer endpoints in mpmath.iv.
"""
from fractions import Fraction
from sympy import Rational, lambdify
from sympy.printing.pycode import PythonCodePrinter
from mpmath import iv


class _ExactRationalPrinter(PythonCodePrinter):
    def _print_Rational(self, expr):
        return f"RAT({int(expr.p)}, {int(expr.q)})"


def interval_lambdify(variables, expressions):
    """Produce an interval-valued compiled expression without float constants.

    Only use for SymPy rational-coefficient formulae with interval inputs.
    The underlying SymPy/MPMath kernels are trusted, not formally verified.
    """
    fn = lambdify(
        variables,
        expressions,
        modules="math",
        printer=_ExactRationalPrinter(
            {"fully_qualified_modules": False, "allow_unknown_functions": True}
        ),
        cse=True,
    )
    fn.__globals__["RAT"] = lambda p, q: iv.mpf(int(p)) / int(q)
    return fn


def exact_interval(a, b=None):
    """Inclusive rational endpoints; outward-rounded at current iv precision."""
    if b is None:
        b = a
    a, b = Fraction(a), Fraction(b)
    if a > b:
        raise ValueError("Reversed rational interval")
    # Integer-only arithmetic until mpmath's outward interval evaluation.
    den = a.denominator * b.denominator
    return iv.mpf([a.numerator * b.denominator,
                   b.numerator * a.denominator]) / den


def assert_exact_coefficient_contract():
    """Pre-flight to detect regression to early binary64 coefficient rounding."""
    iv.dps = 40
    for n, d in ((71, 500), (1, 10), (621, 500), (1701, 2000)):
        val = interval_lambdify((), Rational(n, d))()
        truth = iv.mpf(n) / d
        if not (val.a <= truth.a and val.b >= truth.b):
            raise AssertionError(("Coefficient is not enclosed", n, d, val, truth))
    # Deliberately test the precise previously uncovered bug.
    wrong = iv.mpf(71 / 500)  # intentionally binary64 for regression test ONLY
    true = exact_interval(Fraction(71, 500))
    if not (wrong.b < true.a):
        raise AssertionError("Historical early-float error not detected")
    # No integer-denominator code path may be simplified to binary float.
    expr = Rational(71, 500) + Rational(1, 10)
    got = interval_lambdify((), expr)()
    target = iv.mpf(121) / 500
    if not (got.a <= target.a and got.b >= target.b):
        raise AssertionError(("Composite rational coefficient not enclosed", got))
    print("PASS: rational compiler constructs outward coefficients, float regression exposed")


if __name__ == "__main__":
    assert_exact_coefficient_contract()
