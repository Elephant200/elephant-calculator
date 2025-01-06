from fastapi import APIRouter
from models.cas import *
from services.cas import *

router = APIRouter()

@router.post("/factor", response_model=str)
def factor_expression_endpoint(data: ExpressionRequest):
    """
    Factor an algebraic expression.
    """
    return factor_expression(data.expression)

@router.post("/expand", response_model=str)
def expand_expression_endpoint(data: ExpressionRequest):
    """
    Expand an algebraic expression.
    """
    return expand_expression(data.expression)

@router.post("/simplify", response_model=str)
def simplify_expression_endpoint(data: ExpressionRequest):
    """
    Simplify an algebraic expression.
    """
    return simplify_expression(data.expression)

@router.post("/differentiate", response_model=str)
def derivative_endpoint(data: ExpressionRequest):
    """
    Compute the derivative of an expression.
    """
    return derivative(data.expression)

@router.post("/integrate", response_model=str)
def indefinite_integral_endpoint(data: IntegralRequest):
    """
    Compute the indefinite integral of an expression.
    """
    return indefinite_integral(data.expression, data.variable)

@router.post("/definite-integral", response_model=str)
def definite_integral_endpoint(data: DefiniteIntegralRequest):
    """
    Compute the definite integral of an expression over a range.
    """
    return definite_integral(data.expression, data.variable, data.lower_limit, data.upper_limit)

@router.post("/solve-equation", response_model=str)
def solve_single_variable_endpoint(data: SingleVariableEquationRequest):
    """
    Solve a single-variable equation.
    """
    return solve_single_variable(data.equation, data.variable)

@router.post("/solve-multivariable", response_model=str)
def solve_multivariable_endpoint(data: MultiVariableEquationsRequest):
    """
    Solve a system of multivariable equations.
    """
    return solve_multivariable(data.equations, data.variables)

@router.post("/solve-differential", response_model=str)
def solve_differential_endpoint(data: DifferentialEquationRequest):
    """
    Solve a first-order differential equation.
    """
    return solve_differential(data.equation)