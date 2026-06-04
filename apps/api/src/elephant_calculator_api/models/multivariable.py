from pydantic import BaseModel, Field, field_validator
from sympy import sympify

from elephant_calculator.utils.formatters import format_expression


def _check_expression(value: str) -> str:
    try:
        sympify(format_expression(value))
    except Exception as e:
        raise ValueError(f"Invalid mathematical expression: {value}. Error: {e}")
    return value


def _check_variables(value: str) -> str:
    parts = [v.strip() for v in value.split(",") if v.strip()]
    if not parts:
        raise ValueError("At least one variable is required.")
    if not all(p.isalpha() for p in parts):
        raise ValueError(f"Variables must be letters, comma-separated. Received: {value}")
    return value


class PartialDerivativeRequest(BaseModel):
    expression: str = Field(..., description="The expression to differentiate.")
    variable: str = Field(..., description="The variable to differentiate with respect to.")
    order: int = Field(1, description="The order of the derivative.")

    @field_validator("expression")
    def _expr(cls, v):
        return _check_expression(v)

    @field_validator("variable")
    def _var(cls, v):
        if not v.strip().isalpha():
            raise ValueError(f"Variable must be a single letter. Received: {v}")
        return v

    @field_validator("order")
    def _order(cls, v):
        if v < 1:
            raise ValueError("Order must be a positive integer.")
        return v


class ScalarFieldRequest(BaseModel):
    """A scalar function plus the variables it depends on (gradient, laplacian, hessian)."""

    expression: str = Field(..., description="The scalar field f(x, y, ...).")
    variables: str = Field(..., description="Comma-separated variables, e.g. 'x, y, z'.")

    @field_validator("expression")
    def _expr(cls, v):
        return _check_expression(v)

    @field_validator("variables")
    def _vars(cls, v):
        return _check_variables(v)


class VectorFieldRequest(BaseModel):
    """A vector field (one expression per component) plus its variables."""

    field: list[str] = Field(..., description="Vector-field components, e.g. ['x*y', 'y*z', 'z*x'].")
    variables: str = Field(..., description="Comma-separated variables, e.g. 'x, y, z'.")

    @field_validator("field")
    def _field(cls, v):
        if not v:
            raise ValueError("The vector field must have at least one component.")
        for comp in v:
            _check_expression(comp)
        return v

    @field_validator("variables")
    def _vars(cls, v):
        return _check_variables(v)


class JacobianRequest(BaseModel):
    functions: list[str] = Field(..., description="Component functions, e.g. ['x*y', 'x+y'].")
    variables: str = Field(..., description="Comma-separated variables, e.g. 'x, y'.")

    @field_validator("functions")
    def _funcs(cls, v):
        if not v:
            raise ValueError("At least one function is required.")
        for f in v:
            _check_expression(f)
        return v

    @field_validator("variables")
    def _vars(cls, v):
        return _check_variables(v)


class DirectionalDerivativeRequest(BaseModel):
    expression: str = Field(..., description="The scalar field f(x, y, ...).")
    variables: str = Field(..., description="Comma-separated variables, e.g. 'x, y'.")
    direction: list[str] = Field(..., description="Direction vector components (one per variable).")

    @field_validator("expression")
    def _expr(cls, v):
        return _check_expression(v)

    @field_validator("variables")
    def _vars(cls, v):
        return _check_variables(v)

    @field_validator("direction")
    def _dir(cls, v):
        if not v:
            raise ValueError("The direction vector must have at least one component.")
        for c in v:
            _check_expression(c)
        return v


class DoubleIntegralRequest(BaseModel):
    expression: str = Field(..., description="The integrand.")
    var1: str = Field(..., description="Inner integration variable.")
    lower1: str = Field(..., description="Inner lower limit (may depend on the outer variable).")
    upper1: str = Field(..., description="Inner upper limit (may depend on the outer variable).")
    var2: str = Field(..., description="Outer integration variable.")
    lower2: str = Field(..., description="Outer lower limit.")
    upper2: str = Field(..., description="Outer upper limit.")

    @field_validator("expression", "lower1", "upper1", "lower2", "upper2")
    def _expr(cls, v):
        return _check_expression(v)


class TripleIntegralRequest(BaseModel):
    expression: str = Field(..., description="The integrand.")
    var1: str = Field(..., description="Innermost integration variable.")
    lower1: str = Field(..., description="Innermost lower limit.")
    upper1: str = Field(..., description="Innermost upper limit.")
    var2: str = Field(..., description="Middle integration variable.")
    lower2: str = Field(..., description="Middle lower limit.")
    upper2: str = Field(..., description="Middle upper limit.")
    var3: str = Field(..., description="Outermost integration variable.")
    lower3: str = Field(..., description="Outermost lower limit.")
    upper3: str = Field(..., description="Outermost upper limit.")

    @field_validator("expression", "lower1", "upper1", "lower2", "upper2", "lower3", "upper3")
    def _expr(cls, v):
        return _check_expression(v)


class LimitRequest(BaseModel):
    expression: str = Field(..., description="The expression to take the limit of.")
    variable: str = Field(..., description="The variable that approaches the point.")
    point: str = Field(..., description="The point approached (use 'oo' for infinity).")
    direction: str = Field("+", description="Approach direction: '+', '-' or '+-'.")

    @field_validator("expression")
    def _expr(cls, v):
        return _check_expression(v)

    @field_validator("variable")
    def _var(cls, v):
        if not v.strip().isalpha():
            raise ValueError(f"Variable must be a single letter. Received: {v}")
        return v

    @field_validator("direction")
    def _dir(cls, v):
        if v not in ("+", "-", "+-"):
            raise ValueError("Direction must be '+', '-' or '+-'.")
        return v


class TaylorSeriesRequest(BaseModel):
    expression: str = Field(..., description="The expression to expand.")
    variable: str = Field(..., description="The expansion variable.")
    point: str = Field("0", description="The point to expand about.")
    order: int = Field(6, description="Truncation order.")

    @field_validator("expression")
    def _expr(cls, v):
        return _check_expression(v)

    @field_validator("variable")
    def _var(cls, v):
        if not v.strip().isalpha():
            raise ValueError(f"Variable must be a single letter. Received: {v}")
        return v

    @field_validator("order")
    def _order(cls, v):
        if v < 1:
            raise ValueError("Order must be a positive integer.")
        return v
