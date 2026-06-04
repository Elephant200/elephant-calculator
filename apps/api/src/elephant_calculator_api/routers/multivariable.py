from fastapi import APIRouter

from elephant_calculator_api.models.multivariable import *
from elephant_calculator.services import multivariable as mv

router = APIRouter()


@router.post("/partial", response_model=str)
def partial_derivative(data: PartialDerivativeRequest):
    """Compute a (possibly higher-order) partial derivative."""
    return mv.partial_derivative(data.expression, data.variable, data.order)


@router.post("/gradient", response_model=list[str])
def gradient(data: ScalarFieldRequest):
    """Gradient ∇f as a list of partial derivatives, one per variable."""
    return mv.gradient(data.expression, data.variables)


@router.post("/divergence", response_model=str)
def divergence(data: VectorFieldRequest):
    """Divergence ∇·F of a vector field."""
    return mv.divergence(data.field, data.variables)


@router.post("/curl", response_model=list[str])
def curl(data: VectorFieldRequest):
    """Curl ∇×F of a 3-D vector field."""
    return mv.curl(data.field, data.variables)


@router.post("/laplacian", response_model=str)
def laplacian(data: ScalarFieldRequest):
    """Laplacian ∇²f (sum of unmixed second partials)."""
    return mv.laplacian(data.expression, data.variables)


@router.post("/hessian", response_model=list[list[str]])
def hessian(data: ScalarFieldRequest):
    """Hessian matrix of second partial derivatives."""
    return mv.hessian(data.expression, data.variables)


@router.post("/jacobian", response_model=list[list[str]])
def jacobian(data: JacobianRequest):
    """Jacobian matrix of a vector-valued function."""
    return mv.jacobian(data.functions, data.variables)


@router.post("/directional-derivative", response_model=str)
def directional_derivative(data: DirectionalDerivativeRequest):
    """Directional derivative of f along a (normalised) direction vector."""
    return mv.directional_derivative(data.expression, data.variables, data.direction)


@router.post("/double-integral", response_model=str)
def double_integral(data: DoubleIntegralRequest):
    """Iterated double integral (inner variable first)."""
    return mv.double_integral(
        data.expression, data.var1, data.lower1, data.upper1,
        data.var2, data.lower2, data.upper2,
    )


@router.post("/triple-integral", response_model=str)
def triple_integral(data: TripleIntegralRequest):
    """Iterated triple integral (innermost variable first)."""
    return mv.triple_integral(
        data.expression, data.var1, data.lower1, data.upper1,
        data.var2, data.lower2, data.upper2,
        data.var3, data.lower3, data.upper3,
    )


@router.post("/limit", response_model=str)
def compute_limit(data: LimitRequest):
    """Limit of an expression as a variable approaches a point."""
    return mv.compute_limit(data.expression, data.variable, data.point, data.direction)


@router.post("/taylor-series", response_model=str)
def taylor_series(data: TaylorSeriesRequest):
    """Taylor/Maclaurin series expansion to a given order."""
    return mv.taylor_series(data.expression, data.variable, data.point, data.order)
