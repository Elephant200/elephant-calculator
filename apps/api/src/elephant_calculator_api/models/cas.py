from pydantic import BaseModel, field_validator, Field
from sympy import sympify, Symbol
from elephant_calculator.utils.formatters import format_expression

class ExpressionRequest(BaseModel):
    expression: str = Field(..., description="The algebraic expression to process.")

    @field_validator("expression")
    def validate_expression(cls, v):
        try:
            sympify(format_expression(v))  # Validate if the expression is mathematically valid
        except Exception as e:
            raise ValueError(f"Invalid mathematical expression: {v}. Error: {e}")
        return v


class IntegralRequest(BaseModel):
    expression: str = Field(..., description="The algebraic expression to integrate.")
    variable: str = Field(..., description="The variable with respect to which integration is performed.")

    @field_validator("expression")
    def validate_expression(cls, v):
        try:
            sympify(format_expression(v))
        except Exception as e:
            raise ValueError(f"Invalid mathematical expression: {v}. Error: {e}")
        return v

    @field_validator("variable")
    def validate_variable(cls, v):
        if not v.isalpha():
            raise ValueError(f"Variable must be a single letter. Received: {v}")
        return v


class DefiniteIntegralRequest(BaseModel):
    expression: str = Field(..., description="The algebraic expression to integrate.")
    variable: str = Field(..., description="The variable with respect to which integration is performed.")
    lower_limit: str = Field(..., description="The lower limit of the definite integral.")
    upper_limit: str = Field(..., description="The upper limit of the definite integral.")

    @field_validator("expression")
    def validate_expression(cls, v):
        try:
            sympify(format_expression(v))
        except Exception as e:
            raise ValueError(f"Invalid mathematical expression: {v}. Error: {e}")
        return v

    @field_validator("variable")
    def validate_variable(cls, v):
        if not v.isalpha():
            raise ValueError(f"Variable must be a single letter. Received: {v}")
        return v

    @field_validator("lower_limit", "upper_limit")
    def validate_limits(cls, v):
        try:
            sympify(format_expression(v))  # Ensure limits can be evaluated
        except Exception as e:
            raise ValueError(f"Invalid limit: {v}. Error: {e}")
        return v


class SingleVariableEquationRequest(BaseModel):
    equation: str = Field(..., description="The equation to solve, with '=' separating the left and right sides.")
    variable: str = Field(..., description="The variable to solve for.")

    @field_validator("equation")
    def validate_equation(cls, v):
        try:
            left, right = format_expression(v).split("=")
            sympify(left.strip())
            sympify(right.strip())
        except Exception as e:
            raise ValueError(f"Invalid equation format: {v}. Error: {e}")
        return v

    @field_validator("variable")
    def validate_variable(cls, v):
        if not v.isalpha():
            raise ValueError(f"Variable must be a single letter. Received: {v}")
        return v


class MultiVariableEquationsRequest(BaseModel):
    equations: list[str] = Field(..., description="A list of equations to solve.")
    variables: str = Field(..., description="A comma-separated list of variables to solve for.")

    @field_validator("equations")
    def validate_equations(cls, equations):
        for equation in equations:
            try:
                left, right = format_expression(equation).split("=")
                sympify(left.strip())
                sympify(right.strip())
            except Exception as e:
                raise ValueError(f"Invalid equation format: {equation}. Error: {e}")
        return equations

    @field_validator("variables")
    def validate_variables(cls, variables):
        vars_list = variables.split(",")
        if not all(var.strip().isalpha() for var in vars_list):
            raise ValueError(f"All variables must be single letters. Received: {variables}")
        return variables


class DifferentialEquationRequest(BaseModel):
    equation: str = Field(..., description="The first-order differential equation to solve.")

    @field_validator("equation")
    def validate_differential_equation(cls, v):
        # The solver splits the equation on '=' and formats each side with
        # diff=True (so y' becomes a derivative). Validating with a plain
        # sympify of the whole string would reject every real ODE, so we
        # only check the overall shape here and let the solver parse it.
        if v.count("=") != 1:
            raise ValueError(
                "A differential equation must contain exactly one '=' (e.g. y' + y = 0)."
            )
        left, right = v.split("=")
        if not left.strip() or not right.strip():
            raise ValueError("Both sides of the differential equation must be non-empty.")
        return v
        return v
    