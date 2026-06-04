"""Multivariable & vector calculus built on sympy.

Input expressions use the same lenient formatting as the CAS (``^`` for powers,
implicit multiplication), and results are rendered back in that style via
``reverse_format`` so they match the rest of the calculator.
"""

from sympy import diff, integrate, limit, series, sqrt, simplify, oo, Symbol, sympify

from elephant_calculator.utils.formatters import format_expression, reverse_format


def _parse(expression):
    """Parse a user expression into a sympy object."""
    return sympify(format_expression(str(expression)))


def _show(value):
    return reverse_format(str(value))


def _symbols(variables):
    syms = [Symbol(v.strip()) for v in str(variables).split(",") if v.strip()]
    if not syms:
        raise ValueError("At least one variable is required.")
    return syms


def _point(value):
    text = str(value).strip().lower()
    if text in ("oo", "inf", "infinity", "+oo", "+inf"):
        return oo
    if text in ("-oo", "-inf", "-infinity"):
        return -oo
    return _parse(value)


# ---- Derivatives ----

def partial_derivative(expression, variable, order=1):
    if order < 1:
        raise ValueError("Order must be a positive integer.")
    return _show(diff(_parse(expression), Symbol(variable.strip()), order))


def gradient(expression, variables):
    expr = _parse(expression)
    return [_show(diff(expr, v)) for v in _symbols(variables)]


def laplacian(expression, variables):
    expr = _parse(expression)
    return _show(sum(diff(expr, v, 2) for v in _symbols(variables)))


def hessian(expression, variables):
    expr = _parse(expression)
    syms = _symbols(variables)
    return [[_show(diff(expr, a, b)) for b in syms] for a in syms]


def jacobian(functions, variables):
    syms = _symbols(variables)
    funcs = [_parse(f) for f in functions]
    if not funcs:
        raise ValueError("At least one function is required.")
    return [[_show(diff(f, v)) for v in syms] for f in funcs]


def directional_derivative(expression, variables, direction):
    expr = _parse(expression)
    syms = _symbols(variables)
    vec = [_parse(c) for c in direction]
    if len(vec) != len(syms):
        raise ValueError("The direction vector must have one component per variable.")
    norm = sqrt(sum(c * c for c in vec))
    if norm == 0:
        raise ValueError("The direction vector must be non-zero.")
    result = sum(diff(expr, syms[i]) * vec[i] for i in range(len(syms))) / norm
    return _show(simplify(result))


# ---- Vector fields ----

def divergence(field, variables):
    syms = _symbols(variables)
    comps = [_parse(c) for c in field]
    if len(comps) != len(syms):
        raise ValueError("The field must have one component per variable.")
    return _show(sum(diff(comps[i], syms[i]) for i in range(len(syms))))


def curl(field, variables):
    syms = _symbols(variables)
    if len(syms) != 3 or len(field) != 3:
        raise ValueError("Curl is only defined for 3-D vector fields (3 components, 3 variables).")
    p, q, r = (_parse(c) for c in field)
    x, y, z = syms
    return [
        _show(diff(r, y) - diff(q, z)),
        _show(diff(p, z) - diff(r, x)),
        _show(diff(q, x) - diff(p, y)),
    ]


# ---- Multiple integration ----

def _integrate_step(expr, variable, lower, upper):
    var = Symbol(variable.strip())
    if lower is None and upper is None:
        return integrate(expr, var)
    if lower is None or upper is None:
        raise ValueError(f"Both limits are required for a definite integral over {variable}.")
    return integrate(expr, (var, _parse(lower), _parse(upper)))


def double_integral(expression, var1, lower1, upper1, var2, lower2, upper2):
    """Integrate over var1 (inner) then var2 (outer)."""
    expr = _parse(expression)
    expr = _integrate_step(expr, var1, lower1, upper1)
    expr = _integrate_step(expr, var2, lower2, upper2)
    return _show(expr)


def triple_integral(expression, var1, lower1, upper1, var2, lower2, upper2, var3, lower3, upper3):
    """Integrate over var1 (innermost), then var2, then var3 (outermost)."""
    expr = _parse(expression)
    expr = _integrate_step(expr, var1, lower1, upper1)
    expr = _integrate_step(expr, var2, lower2, upper2)
    expr = _integrate_step(expr, var3, lower3, upper3)
    return _show(expr)


# ---- Other symbolic calculus ----

def compute_limit(expression, variable, point, direction="+"):
    if direction not in ("+", "-", "+-"):
        raise ValueError("Direction must be '+', '-' or '+-'.")
    return _show(limit(_parse(expression), Symbol(variable.strip()), _point(point), direction))


def taylor_series(expression, variable, point=0, order=6):
    if order < 1:
        raise ValueError("Order must be a positive integer.")
    expanded = series(_parse(expression), Symbol(variable.strip()), _point(point), order).removeO()
    return _show(expanded)
