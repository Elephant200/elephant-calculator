from pydantic import BaseModel

class ExpressionRequest(BaseModel):
    expression: str

class IntegralRequest(BaseModel):
    expression: str
    variable: str

class DefiniteIntegralRequest(BaseModel):
    expression: str
    variable: str
    lower_limit: str
    upper_limit: str

class SingleVariableEquationRequest(BaseModel):
    equation: str
    variable: str

class MultiVariableEquationsRequest(BaseModel):
    equations: list[str]
    variables: str

class DifferentialEquationRequest(BaseModel):
    equation: str