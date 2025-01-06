from pydantic import BaseModel, Field, field_validator

class MatrixOperation(BaseModel):
    matrix1: list[list[float]] = Field(..., description="The first matrix for the operation.")
    matrix2: list[list[float]] = Field(..., description="The second matrix for the operation.")

    @field_validator("matrix1", "matrix2")
    def validate_matrices(cls, matrix):
        if not matrix or not all(isinstance(row, list) for row in matrix):
            raise ValueError("Matrix must be a non-empty list of rows.")
        if not all(isinstance(x, (int, float)) for row in matrix for x in row):
            raise ValueError("Matrix elements must be numeric (int or float).")
        if len({len(row) for row in matrix}) > 1:
            raise ValueError("All rows in a matrix must have the same length.")
        return matrix

class ScalarMatrixOperation(BaseModel):
    matrix: list[list[float]] = Field(..., description="The matrix to scale or operate on.")
    scalar: float = Field(..., description="The scalar value for scaling the matrix.")

    @field_validator("matrix")
    def validate_matrix(cls, matrix):
        if not matrix or not all(isinstance(row, list) for row in matrix):
            raise ValueError("Matrix must be a non-empty list of rows.")
        if not all(isinstance(x, (int, float)) for row in matrix for x in row):
            raise ValueError("Matrix elements must be numeric (int or float).")
        if len({len(row) for row in matrix}) > 1:
            raise ValueError("All rows in a matrix must have the same length.")
        return matrix

    @field_validator("scalar")
    def validate_scalar(cls, scalar):
        if not isinstance(scalar, (int, float)):
            raise ValueError("Scalar must be numeric (int or float).")
        return scalar

class VectorMatrixOperation(BaseModel):
    vector: list[float] = Field(..., description="The vector to multiply with the matrix.")
    matrix: list[list[float]] = Field(..., description="The matrix to multiply with the vector.")

    @field_validator("vector")
    def validate_vector(cls, vector):
        if not vector or not all(isinstance(x, (int, float)) for x in vector):
            raise ValueError("Vector must be a non-empty list of numeric values.")
        return vector

    @field_validator("matrix")
    def validate_matrix(cls, matrix):
        if not matrix or not all(isinstance(row, list) for row in matrix):
            raise ValueError("Matrix must be a non-empty list of rows.")
        if not all(isinstance(x, (int, float)) for row in matrix for x in row):
            raise ValueError("Matrix elements must be numeric (int or float).")
        if len({len(row) for row in matrix}) > 1:
            raise ValueError("All rows in a matrix must have the same length.")
        return matrix

    @field_validator("matrix")
    def validate_dimensions(cls, matrix, values):
        vector = values.get("vector")
        if vector and len(matrix[0]) != len(vector):
            raise ValueError("Matrix column count must match vector length.")
        return matrix
