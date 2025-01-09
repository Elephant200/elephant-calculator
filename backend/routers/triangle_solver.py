from fastapi import APIRouter
from models.triangle_solver import TriangleRequest
from services.triangle_solver import solve_triangle

router = APIRouter()

@router.post("/solve", response_model=dict)
def solve_triangle_endpoint(data: TriangleRequest):
    """
    Solve a triangle given sufficient inputs.

    Args:
        data (TriangleRequest): Contains side lengths (a, b, c) and/or angles (A, B, C).

    Returns:
        dict: A dictionary containing all sides and angles of the solved triangle.
    """
    #print(f"Received: {data}")
    #print(f"Attributes: a={data.a}, b={data.b}, c={data.c}, A={data.A}, B={data.B}, C={data.C}")
    return solve_triangle(a=data.a, b=data.b, c=data.c, A=data.A, B=data.B, C=data.C)
