from pydantic import BaseModel

class MatrixOperation(BaseModel):
    matrix1: list[list[float]]
    matrix2: list[list[float]]

class ScalarMatrixOperation(BaseModel):
    matrix: list[list[float]]
    scalar: float

class VectorMatrixOperation(BaseModel):
    vector: list[float]
    matrix: list[list[float]]