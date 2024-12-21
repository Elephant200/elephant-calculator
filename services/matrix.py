from math import sqrt
import copy
from .vector import Vector

class Matrix:
	def __init__(self, elements):
		self.elements = elements
		self.rows = len(elements)
		self.cols = len(elements[0]) if elements else 0

	def __getitem__(self, index):
		return self.elements[index]

	def __add__(self, other):
		if self.rows != other.rows or self.cols != other.cols:
			raise ValueError("Matrices must have the same dimensions for addition.")
		return Matrix([
			[self[i][j] + other[i][j] for j in range(self.cols)]
			for i in range(self.rows)
		])

	def __sub__(self, other):
		if self.rows != other.rows or self.cols != other.cols:
			raise ValueError("Matrices must have the same dimensions for subtraction.")
		return Matrix([
			[self[i][j] - other[i][j] for j in range(self.cols)]
			for i in range(self.rows)
		])

	def __mul__(self, other):
		if isinstance(other, Matrix):
			if self.cols != other.rows:
				raise ValueError("Matrix multiplication is not defined for these dimensions.")
			result = [[
				sum(self[i][k] * other[k][j] for k in range(self.cols))
				for j in range(other.cols)
			] for i in range(self.rows)]
			return Matrix(result)
		elif isinstance(other, Vector):
			if self.cols != len(other):
				raise ValueError("Matrix and vector dimensions do not align for multiplication.")
			result = [
				sum(self[i][j] * other[j] for j in range(self.cols))
				for i in range(self.rows)
			]
			return Vector(result)
		elif isinstance(other, (int, float)):
			return Matrix([
				[self[i][j] * other for j in range(self.cols)]
				for i in range(self.rows)
			])
		else:
			raise ValueError("Unsupported operand for multiplication.")

	def __rmul__(self, other):
		if isinstance(other, Matrix):
			return other.__mul__(self)
		elif isinstance(other, (int, float)):
			return Matrix([
				[self[i][j] * other for j in range(self.cols)]
				for i in range(self.rows)
			])
	
	def __pow__(self, exponent):
		if not isinstance(exponent, int) or exponent < 0:
			raise ValueError("Exponent must be a non-negative integer.")
		if self.rows != self.cols:
			raise ValueError("Matrix exponentiation is only defined for square matrices.")
		result = Matrix([[1 if i == j else 0 for j in range(self.cols)] for i in range(self.rows)])  # Identity matrix
		base = self
		while exponent > 0:
			if exponent % 2 == 1:
				result = result * base
			base = base * base
			exponent //= 2
		return result

	def determinant(self):
		if self.rows != self.cols:
			raise ValueError("Determinant is only defined for square matrices.")
		if self.rows == 1:
			return self.elements[0][0]
		if self.rows == 2:
			return self.elements[0][0] * self.elements[1][1] - self.elements[0][1] * self.elements[1][0]

		det = 0
		for c in range(self.cols):
			det += ((-1) ** c) * self.elements[0][c] * self.minor(0, c).determinant()
		return det

	def minor(self, row, col):
		return Matrix([
			[self[i][j] for j in range(self.cols) if j != col]
			for i in range(self.rows) if i != row
		])

	def transpose(self):
		return Matrix([
			[self[j][i] for j in range(self.rows)]
			for i in range(self.cols)
		])

	def inverse(self):
		det = self.determinant()
		if det == 0:
			raise ValueError("Matrix is singular and cannot be inverted.")

		cofactors = [[
			((-1) ** (i + j)) * self.minor(i, j).determinant()
			for j in range(self.cols)
		] for i in range(self.rows)]

		adjugate = Matrix(cofactors).transpose()
		return (1 / det) * adjugate

	@staticmethod
	def input_matrix():
		while True:
			try:
				dims = input("Enter the dimensions of the matrix: ").replace(',',' ').replace('  ',' ').split(' ')
				rows, cols = int(dims[0]), int(dims[1])
				break
			except Exception as e:
				print("Invalid dimensions, please try again. " + str(e))
		print("Enter the matrix elements row by row, separated by spaces:")
		elements = []
		for i in range(rows):
			while True:
				row = input(f"Row {i}: ").replace(',','').split(' ')
				try:
					row = [eval(row[x]) for x in range(cols)]
					if len(row) != cols:
						raise ValueError("Length of row does not match matrix width.")
					break
				except:
					print("Invalid row, please try again.")
			elements.append(row)
		return Matrix(elements)

	def __str__(self):
		if len(str(max(self.elements[0]))) > 20:
			return '\n'.join([''.join(["%s\t" % element for element in row]) for row in self.elements])
		if len(str(max(self.elements[0]))) > 6:
			return '\n'.join([''.join(["%16s" % element for element in row]) for row in self.elements])
		return '\n'.join([''.join(["%8s" % element for element in row]) for row in self.elements])

	def __repr__(self):
		return self.__str__()
