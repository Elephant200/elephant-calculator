from pydantic import BaseModel, validator

class MatrixOperation(BaseModel):
    matrix1: list[list[float]]
    matrix2: list[list[float]]

    @validator("matrix1", "matrix2")
    def validate_matrix(cls, matrix):
        if not all(isinstance(row, list) for row in matrix):
            raise ValueError("Each matrix must be a list of rows.")
        if not all(isinstance(elem, (int, float)) for row in matrix for elem in row):
            raise ValueError("Matrix elements must be integers or floats.")
        if len({len(row) for row in matrix}) > 1:
            raise ValueError("All rows in a matrix must have the same length.")
        return matrix

    @validator("matrix2")
    def validate_same_dimensions(cls, matrix2, values):
        matrix1 = values.get("matrix1")
        if matrix1 and len(matrix1) != len(matrix2):
            raise ValueError("Matrix1 and Matrix2 must have the same number of rows.")
        if matrix1 and len(matrix1[0]) != len(matrix2[0]):
            raise ValueError("Matrix1 and Matrix2 must have the same number of columns.")
        return matrix2


class ScalarMatrixOperation(BaseModel):
    matrix: list[list[float]]
    scalar: float

    @validator("matrix")
    def validate_matrix(cls, matrix):
        if not all(isinstance(row, list) for row in matrix):
            raise ValueError("Matrix must be a list of rows.")
        if not all(isinstance(elem, (int, float)) for row in matrix for elem in row):
            raise ValueError("Matrix elements must be integers or floats.")
        if len({len(row) for row in matrix}) > 1:
            raise ValueError("All rows in the matrix must have the same length.")
        return matrix

    @validator("scalar")
    def validate_scalar(cls, scalar):
        if not isinstance(scalar, (int, float)):
            raise ValueError("Scalar must be a numeric value (int or float).")
        return scalar


class VectorMatrixOperation(BaseModel):
    vector: list[float]
    matrix: list[list[float]]

    @validator("vector")
    def validate_vector(cls, vector):
        if not all(isinstance(elem, (int, float)) for elem in vector):
            raise ValueError("Vector elements must be integers or floats.")
        return vector

    @validator("matrix")
    def validate_matrix(cls, matrix):
        if not all(isinstance(row, list) for row in matrix):
            raise ValueError("Matrix must be a list of rows.")
        if not all(isinstance(elem, (int, float)) for row in matrix for elem in row):
            raise ValueError("Matrix elements must be integers or floats.")
        if len({len(row) for row in matrix}) > 1:
            raise ValueError("All rows in the matrix must have the same length.")
        return matrix

    @validator("matrix")
    def validate_matrix_vector_dimensions(cls, matrix, values):
        vector = values.get("vector")
        if vector and len(matrix[0]) != len(vector):
            raise ValueError("Matrix column count must match vector length.")
        return matrix
