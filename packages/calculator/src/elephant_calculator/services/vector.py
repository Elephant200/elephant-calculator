from math import sqrt, acos, degrees as _degrees
from elephant_calculator.utils.validators import parse_input

class Vector:
	def __init__(self, elements):
		self.elements = elements

	def __len__(self):
		return len(self.elements)

	def __getitem__(self, index):
		return self.elements[index]

	def __add__(self, other):
		if len(self) != len(other):
			raise ValueError("Vectors must be of the same dimension for addition.")
		return Vector([a + b for a, b in zip(self.elements, other.elements)])

	def __sub__(self, other):
		if len(self) != len(other):
			raise ValueError("Vectors must be of the same dimension for subtraction.")
		return Vector([a - b for a, b in zip(self.elements, other.elements)])

	def __mul__(self, other):
		if isinstance(other, Vector):
			return self.dot(self, other)
		elif isinstance(other, (int, float)):
			return Vector([a * other for a in self.elements])
		else:
			raise ValueError("Unsupported operand for multiplication.")

	def __rmul__(self, other):
		return self * other

	def cross(self, other):
		if len(self) != 3 or len(other) != 3:
			raise ValueError("Cross product is only defined for 3-dimensional vectors.")
		a, b, c = self.elements
		d, e, f = other.elements
		return Vector([
			b * f - c * e,
			c * d - a * f,
			a * e - b * d
		])
	
	def dot(self, other):
		if len(self) != len(other):
			raise ValueError("Vectors must be of the same dimension for dot product.")
		return sum(a * b for a, b in zip(self.elements, other.elements))

	def magnitude(self):
		"""Euclidean length (L2 norm) of the vector."""
		return sqrt(sum(a * a for a in self.elements))

	def normalize(self):
		"""Unit vector pointing in the same direction."""
		mag = self.magnitude()
		if mag == 0:
			raise ValueError("Cannot normalize the zero vector.")
		return Vector([a / mag for a in self.elements])

	def distance(self, other):
		"""Euclidean distance between the points the vectors point to."""
		if len(self) != len(other):
			raise ValueError("Vectors must be of the same dimension to measure distance.")
		return sqrt(sum((a - b) ** 2 for a, b in zip(self.elements, other.elements)))

	def angle(self, other, in_degrees=True):
		"""Angle between two vectors (in degrees by default)."""
		if len(self) != len(other):
			raise ValueError("Vectors must be of the same dimension to measure an angle.")
		m1, m2 = self.magnitude(), other.magnitude()
		if m1 == 0 or m2 == 0:
			raise ValueError("Angle is undefined when a vector has zero magnitude.")
		cos_theta = max(-1.0, min(1.0, self.dot(other) / (m1 * m2)))
		theta = acos(cos_theta)
		return _degrees(theta) if in_degrees else theta

	def projection(self, other):
		"""Vector projection of this vector onto ``other``."""
		denom = other.dot(other)
		if denom == 0:
			raise ValueError("Cannot project onto the zero vector.")
		scale = self.dot(other) / denom
		return Vector([scale * b for b in other.elements])

	@staticmethod
	def input_vector():
		while True:
			try:
				print("Enter vector elements separated by spaces: ")
				elements = input().replace(',',' ').replace('  ',' ').split()
				elements = [parse_input(x) for x in elements]
				break
			except:
				print("Invalid vector, please try again.")
		return Vector(elements)

	def __str__(self):
		if len(str(max(self.elements))) > 20:
			return '\n'.join(["%s\t" % element for element in self.elements])
		if len(str(max(self.elements))) > 6:
			return '\n'.join(["%16s" % element for element in self.elements])
		return '\n'.join(["%8s" % element for element in self.elements])

	def __repr__(self):
		return self.__str__()
