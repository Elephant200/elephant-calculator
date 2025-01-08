from pydantic import BaseModel, field_validator, Field
from sympy import sympify, Symbol

class ExpressionRequest(BaseModel):
    expression: str = Field(..., description="The algebraic expression to process.")

    @field_validator("expression")
    def validate_expression(cls, v):
        try:
            sympify(v)  # Validate if the expression is mathematically valid
        except Exception as e:
            raise ValueError(f"Invalid mathematical expression: {v}. Error: {e}")
        return v


class IntegralRequest(BaseModel):
    expression: str = Field(..., description="The algebraic expression to integrate.")
    variable: str = Field(..., description="The variable with respect to which integration is performed.")

    @field_validator("expression")
    def validate_expression(cls, v):
        try:
            sympify(v)
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
            sympify(v)
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
            sympify(v)  # Ensure limits can be evaluated
        except Exception as e:
            raise ValueError(f"Invalid limit: {v}. Error: {e}")
        return v


class SingleVariableEquationRequest(BaseModel):
    equation: str = Field(..., description="The equation to solve, with '=' separating the left and right sides.")
    variable: str = Field(..., description="The variable to solve for.")

    @field_validator("equation")
    def validate_equation(cls, v):
        try:
            left, right = v.split("=")
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
                left, right = equation.split("=")
                sympify(left.strip())
                sympify(right.strip())
            except Exception as e:
                raise ValueError(f"Invalid equation format: {equation}. Error: {e}")
        return equations

    @field_validator("variables")
    def validate_variables(cls, variables):
        vars_list = variables.split(",")
        if not all(var.isalpha() for var in vars_list):
            raise ValueError(f"All variables must be single letters. Received: {variables}")
        return variables


class DifferentialEquationRequest(BaseModel):
    equation: str = Field(..., description="The first-order differential equation to solve.")

    @field_validator("equation")
    def validate_differential_equation(cls, v):
        try:
            sympify(v)  # Ensure the differential equation is mathematically valid
        except Exception as e:
            raise ValueError(f"Invalid differential equation: {v}. Error: {e}")
        return v
    