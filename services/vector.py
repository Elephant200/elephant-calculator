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

	@staticmethod
	def input_vector():
		while True:
			try:
				print("Enter vector elements separated by spaces:")
				elements = list(map(float, input().replace(',',' ').replace('  ',' ').split()))
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
