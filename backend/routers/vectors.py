from fastapi import APIRouter
from models.vectors import *
from services.vector import Vector

router = APIRouter()

@router.post("/add", response_model=list[float])
def add_vectors(data: VectorOperation):
    """
    Add two vectors.

    Args:
        data (VectorOperation): Contains two vectors to add.

    Returns:
        list[float]: The resulting vector after addition.
    """
    v1 = Vector(data.vector1)
    v2 = Vector(data.vector2)
    return (v1 + v2).elements

@router.post("/subtract", response_model=list[float])
def subtract_vectors(data: VectorOperation):
    """
    Subtract one vector from another.

    Args:
        data (VectorOperation): Contains two vectors for subtraction.

    Returns:
        list[float]: The resulting vector after subtraction.
    """
    v1 = Vector(data.vector1)
    v2 = Vector(data.vector2)
    return (v1 - v2).elements

@router.post("/dot", response_model=float)
def dot_product(data: VectorOperation):
    """
    Compute the dot product of two vectors.

    Args:
        data (VectorOperation): Contains two vectors for dot product computation.

    Returns:
        float: The dot product of the two vectors.
    """
    v1 = Vector(data.vector1)
    v2 = Vector(data.vector2)
    return v1.dot(v2)

@router.post("/cross", response_model=list[float])
def cross_product(data: VectorOperation):
    """
    Compute the cross product of two 3D vectors.

    Args:
        data (VectorOperation): Contains two 3D vectors for cross product computation.

    Returns:
        list[float]: The resulting vector after cross product.

    Raises:
        ValueError: If the vectors are not 3D.
    """
    v1 = Vector(data.vector1)
    v2 = Vector(data.vector2)
    return v1.cross(v2).elements

@router.post("/scale", response_model=list[float])
def scale_vector(data: ScalarVectorOperation):
    """
    Scale a vector by a scalar.

    Args:
        data (ScalarVectorOperation): Contains a vector and a scalar for scaling.

    Returns:
        list[float]: The resulting vector after scaling.
    """
    v = Vector(data.vector)
    return (v * data.scalar).elements
