from fastapi import APIRouter
from models.triangle_solver import *
from services.triangle_solver import *

router = APIRouter()

@router.post("/solve", response_model=dict)
def solve_triangle_endpoint(data: TriangleRequest):
    return solve_triangle(a=data.a, b=data.b, c=data.c, A=data.A, B=data.B, C=data.C)