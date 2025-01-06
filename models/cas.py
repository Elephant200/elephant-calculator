from pydantic import BaseModel, validator
from sympy import sympify, Symbol

class ExpressionRequest(BaseModel):
    expression: str

    @validator("expression")
    def validate_expression(cls, v):
        try:
            sympify(v)  # Validate if the expression is mathematically valid
        except Exception as e:
            raise ValueError(f"Invalid mathematical expression: {v}. Error: {e}")
        return v


class IntegralRequest(BaseModel):
    expression: str
    variable: str

    @validator("expression")
    def validate_expression(cls, v):
        try:
            sympify(v)
        except Exception as e:
            raise ValueError(f"Invalid mathematical expression: {v}. Error: {e}")
        return v

    @validator("variable")
    def validate_variable(cls, v):
        if not v.isalpha():
            raise ValueError(f"Variable must be a single letter. Received: {v}")
        return v


class DefiniteIntegralRequest(BaseModel):
    expression: str
    variable: str
    lower_limit: str
    upper_limit: str

    @validator("expression")
    def validate_expression(cls, v):
        try:
            sympify(v)
        except Exception as e:
            raise ValueError(f"Invalid mathematical expression: {v}. Error: {e}")
        return v

    @validator("variable")
    def validate_variable(cls, v):
        if not v.isalpha():
            raise ValueError(f"Variable must be a single letter. Received: {v}")
        return v

    @validator("lower_limit", "upper_limit")
    def validate_limits(cls, v):
        try:
            sympify(v)  # Ensure limits can be evaluated
        except Exception as e:
            raise ValueError(f"Invalid limit: {v}. Error: {e}")
        return v


class SingleVariableEquationRequest(BaseModel):
    equation: str
    variable: str

    @validator("equation")
    def validate_equation(cls, v):
        try:
            left, right = v.split("=")
            sympify(left.strip())
            sympify(right.strip())
        except Exception as e:
            raise ValueError(f"Invalid equation format: {v}. Error: {e}")
        return v

    @validator("variable")
    def validate_variable(cls, v):
        if not v.isalpha():
            raise ValueError(f"Variable must be a single letter. Received: {v}")
        return v


class MultiVariableEquationsRequest(BaseModel):
    equations: list[str]
    variables: str

    @validator("equations", each_item=True)
    def validate_equations(cls, v):
        try:
            left, right = v.split("=")
            sympify(left.strip())
            sympify(right.strip())
        except Exception as e:
            raise ValueError(f"Invalid equation format: {v}. Error: {e}")
        return v

    @validator("variables")
    def validate_variables(cls, v):
        vars_list = v.split(",")
        if not all(var.isalpha() for var in vars_list):
            raise ValueError(f"All variables must be single letters. Received: {v}")
        return v


class DifferentialEquationRequest(BaseModel):
    equation: str

    @validator("equation")
    def validate_differential_equation(cls, v):
        try:
            sympify(v)  # Ensure the differential equation is mathematically valid
        except Exception as e:
            raise ValueError(f"Invalid differential equation: {v}. Error: {e}")
        return v
