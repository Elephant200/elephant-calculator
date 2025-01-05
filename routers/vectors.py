from fastapi import APIRouter
from models.vectors import *
from services.vector import Vector

router = APIRouter()

@router.post("/add", response_model=list[float])
def add_vectors(data: VectorOperation):
    v1 = Vector(data.vector1)
    v2 = Vector(data.vector2)
    return (v1 + v2).elements

@router.post("/subtract", response_model=list[float])
def subtract_vectors(data: VectorOperation):
    v1 = Vector(data.vector1)
    v2 = Vector(data.vector2)
    return (v1 - v2).elements

@router.post("/dot", response_model=float)
def dot_product(data: VectorOperation):
    v1 = Vector(data.vector1)
    v2 = Vector(data.vector2)
    return v1.dot(v2)

@router.post("/cross", response_model=list[float])
def cross_product(data: VectorOperation):
    v1 = Vector(data.vector1)
    v2 = Vector(data.vector2)
    return v1.cross(v2).elements

@router.post("/scale", response_model=list[float])
def scale_vector(data: ScalarVectorOperation):
    v = Vector(data.vector)
    return (v * data.scalar).elements
