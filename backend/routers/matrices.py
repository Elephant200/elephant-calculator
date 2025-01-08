from fastapi import APIRouter
from models.matrices import *
from services.matrix import Matrix

router = APIRouter()

@router.post("/add", response_model=list[list[float]])
def add_matrices(data: MatrixOperation):
    """
    Add two matrices.

    Args:
        data (MatrixOperation): Contains two matrices for addition.

    Returns:
        list[list[float]]: The resulting matrix after addition.
    """
    m1 = Matrix(data.matrix1)
    m2 = Matrix(data.matrix2)
    return (m1 + m2).elements

@router.post("/subtract", response_model=list[list[float]])
def subtract_matrices(data: MatrixOperation):
    """
    Subtract one matrix from another.

    Args:
        data (MatrixOperation): Contains two matrices for subtraction.

    Returns:
        list[list[float]]: The resulting matrix after subtraction.
    """
    m1 = Matrix(data.matrix1)
    m2 = Matrix(data.matrix2)
    return (m1 - m2).elements

@router.post("/multiply/matrix", response_model=list[list[float]])
def multiply_matrices(data: MatrixOperation):
    """
    Multiply two matrices.

    Args:
        data (MatrixOperation): Contains two matrices for multiplication.

    Returns:
        list[list[float]]: The resulting matrix after multiplication.
    """
    m1 = Matrix(data.matrix1)
    m2 = Matrix(data.matrix2)
    return (m1 * m2).elements

@router.post("/multiply/vector", response_model=list[float])
def vector_matrix_multiply(data: VectorMatrixOperation):
    """
    Multiply a matrix with a vector.

    Args:
        data (VectorMatrixOperation): Contains a matrix and a vector for multiplication.

    Returns:
        list[float]: The resulting vector after multiplication.
    """
    v = data.vector
    m = Matrix(data.matrix)
    return m * v

@router.post("/scale", response_model=list[list[float]])
def scale_matrix(data: ScalarMatrixOperation):
    """
    Scale a matrix by a scalar value.

    Args:
        data (ScalarMatrixOperation): Contains a matrix and a scalar for scaling.

    Returns:
        list[list[float]]: The resulting matrix after scaling.
    """
    m = Matrix(data.matrix)
    return (m * data.scalar).elements

@router.post("/determinant", response_model=float)
def determinant(data: SingleMatrixOperation):
    """
    Calculate the determinant of a matrix.

    Args:
        data (ScalarMatrixOperation): Contains the matrix for which to calculate the determinant.

    Returns:
        float: The determinant of the matrix.
    """
    m = Matrix(data.matrix)
    print("From router function: " + str(m))
    return m.determinant()

@router.post("/inverse", response_model=list[list[float]])
def inverse_matrix(data: SingleMatrixOperation):
    """
    Compute the inverse of a matrix.

    Args:
        data (ScalarMatrixOperation): Contains the matrix to be inverted.

    Returns:
        list[list[float]]: The inverse of the matrix.
    """
    m = Matrix(data.matrix)
    return m.inverse().elements

@router.post("/transpose", response_model=list[list[float]])
def transpose_matrix(data: SingleMatrixOperation):
    """
    Compute the transpose of a matrix.

    Args:
        data (ScalarMatrixOperation): Contains the matrix to be transposed.

    Returns:
        list[list[float]]: The transposed matrix.
    """
    m = Matrix(data.matrix)
    return m.transpose().elements
