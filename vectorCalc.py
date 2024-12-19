from vector import Vector
from matrix import Matrix
import numpy as np

def inputVector():
    """
    Takes inputs and returns a Vector object
    """
    while True:
        vec = input("Enter the vector, separeted by commas (\", \"): ").split(", ")
        try:
            for i in range(len(vec)):
                vec[i] = eval(vec[i])
            break
        except:
            print("Inputs must be either integers, fractions, or decimals. ")
    return Vector(vec)


def inputMatrix():
    """
    Takes inputs and returns a Matrix object
    """
    while True:
        try:
            size = input("Matrix Dimensions (rows, columns): ").split(',')
            n = int(size[0].strip())
            m = int(size[1].strip())

            if n <= 0 or m <= 0:
                raise ValueError("Dimensions must be positive integers.")

            matrix = []
            for i in range(m):
                while True:
                    row = input(f"Enter row {i+1}, separated by commas (\", \"): ").split(", ")
                    if len(row) != n:
                        print("The length of your row is incorrect. Please input the row again.")
                        continue
                    try:
                        matrix.append([eval(v) for v in row])  # Handle numeric conversions
                        break  # Break if the row input is valid
                    except (SyntaxError, NameError, TypeError):
                        print("Inputs must be either integers, fractions, or decimals. Please try again.")
            return Matrix(matrix)

        except ValueError as ve:
            print(str(ve))
        except Exception as e:
            print("An error occurred: " + str(e) + ". Please try again.")


def transpose(matrix):
    """
    Takes a matrix and transposes that matrix, then returns it.
    """
    mat = matrix.get()
    result = [[0 for i in range(len(mat))] for j in range(len(mat[0]))]
    print(result)
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            result[j][i] = mat[i][j]
    return Matrix(result)


def multiplyVM(vec, mat):
    """
    Takes a Vector and a Matrix, returning their product Vector.
    """
    if vec.len() != mat.getN():
        raise ArithmeticError("Cannot multiply incompatible vectors and matrices.")
    result = [0 for i in range(mat.getM())]
    for i in range(mat.getM()):
        for j in range(mat.getN()):
            result[i] += mat.get(i, j) * vec.get(j)
    return Vector(result)


def multiplyMM(mat1, mat2):
    """
    Takes a Matrix and a Matrix, returning their product Matrix.
    """
    result = [[0 for i in range(mat2.getN())] for j in range(mat1.getM())]
    for i in range(mat1.getM()):
        for j in range(mat2.getN()):
            for k in range(mat2.getM()):
                result[i][j] += mat1.get(i, k) * mat2.get(k, j)
    return Matrix(result)


def pow(mat1, index):
    """
    Recursively computes the power of a matrix using multiplyMM()
    """
    if index == 1:
        return mat1
    return multiplyMM(mat1, pow(mat1, index - 1))

def listMinus(l1, l2):
    """
    A helper function that returns a list with the elements of l1 that are not in l2.
    """
    res = []
    for element in l1:
        if element not in l2:
            res.append(element)
    return res

def det(mat):
    """
    Recursively computes the determinant of a matrix.
    """
    if mat.getN() != mat.getM(): raise ArithmeticError("Cannot find determinant of non-square matrix.")
    size = mat.getN()
    if size == 1: return mat.get(0, 0)
    if size == 2: return mat.get(0, 0)*mat.get(1,1) - mat.get(1,0)*mat.get(0,1)
    sign = 1
    result = 0
    for i in range(size):
        cofactor = Matrix([[mat.get(j, k) for k in listMinus(range(size), [i])] for j in range(1, size)])
        result += sign * mat.get(0, i) * det(cofactor)
        sign*=(-1)
    return result

def inverse(mat):
    """
    Uses numpy to compute the inverse of a matrix
    """
    if mat.getN() != mat.getM(): raise ArithmeticError("Cannot find inverse of a non-square matrix")
    matrix = np.array(mat.get())
    try: return Matrix(np.round(np.linalg.inv(matrix), 10).tolist())
    except: raise ArithmeticError("Cannot invert singular matrix")


def add(mat1, mat2):
    """
    Uses numpy to add two matrices
    """
    if mat1.getN() != mat2.getN() or mat1.getM() != mat2.getM(): raise ArithmeticError("Cannot add matrices of different dimensions.")
    matrix1, matrix2 = np.array(mat1.get()), np.array(mat2.get())
    return Matrix(np.add(matrix1, matrix2).tolist())
    
def subtract(mat1, mat2):
    """
    Uses numpy to subtracts mat2 from mat1
    """
    if mat1.getN() != mat2.getN() or mat1.getM() != mat2.getM(): raise ArithmeticError("Cannot subtract matrices of different dimensions.")
    matrix1, matrix2 = np.array(mat1.get()), np.array(mat2.get())
    return Matrix(np.subtract(matrix1, matrix2).tolist())


def cross(vec1, vec2):
    """
    Computes the cross product of two 3D vectors.
    Returns a Vector object containing the result.
    Raises ArithmeticError if vectors are not 3D.
    """
    if vec1.len() != 3 or vec2.len() != 3:
        raise ArithmeticError("Cross product is only defined for 3D vectors.")
    
    result = [
        vec1.get(1) * vec2.get(2) - vec1.get(2) * vec2.get(1),
        vec1.get(2) * vec2.get(0) - vec1.get(0) * vec2.get(2),
        vec1.get(0) * vec2.get(1) - vec1.get(1) * vec2.get(0)
    ]
    
    return Vector(result)


def dot(vec1, vec2):
    """
    Computes the dot product of two vectors.
    Returns a scalar value containing the result.
    Raises ArithmeticError if vectors have different dimensions.
    """
    if vec1.len() != vec2.len():
        raise ArithmeticError("Cannot compute dot product of vectors with different dimensions.")
    
    result = 0
    for i in range(vec1.len()):
        result += vec1.get(i) * vec2.get(i)
    return result