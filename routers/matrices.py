from fastapi import APIRouter
from models.matrices import *
from services.matrix import Matrix

router = APIRouter()

@router.post("/add", response_model=list[list[float]])
def add_matrices(data: MatrixOperation):
    m1 = Matrix(data.matrix1)
    m2 = Matrix(data.matrix2)
    return (m1 + m2).elements

@router.post("/subtract", response_model=list[list[float]])
def subtract_matrices(data: MatrixOperation):
    m1 = Matrix(data.matrix1)
    m2 = Matrix(data.matrix2)
    return (m1 - m2).elements

@router.post("/multiply/matrix", response_model=list[list[float]])
def multiply_matrices(data: MatrixOperation):
    m1 = Matrix(data.matrix1)
    m2 = Matrix(data.matrix2)
    return (m1 * m2).elements

@router.post("/multiply/vector", response_model=list[float])
def vector_matrix_multiply(data: VectorMatrixOperation):
    v = data.vector
    m = Matrix(data.matrix)
    return m * v

@router.post("/scale", response_model=list[list[float]])
def scale_matrix(data: ScalarMatrixOperation):
    m = Matrix(data.matrix)
    return (m * data.scalar).elements

@router.post("/determinant", response_model=float)
def determinant(data: ScalarMatrixOperation):
    m = Matrix(data.matrix)
    return m.determinant()

@router.post("/inverse", response_model=list[list[float]])
def inverse_matrix(data: ScalarMatrixOperation):
    m = Matrix(data.matrix)
    return m.inverse().elements

@router.post("/transpose", response_model=list[list[float]])
def transpose_matrix(data: ScalarMatrixOperation):
    m = Matrix(data.matrix)
    return m.transpose().elements
