from vector import Vector


class Matrix:

	def __init__(self, mat):
		self.n = len(mat[0])
		self.m = len(mat)
		self.me = mat

	def getN(self):
		return self.n

	def getM(self):
		return self.m

	def get(self, i=None, j=None):
		if i == None or j == None: return self.me
		else: return self.me[i][j]

	def getCol(self, j):
		vec = []
		for i in range(self.m):
			vec.append(self.get(i, j))
		return Vector(vec)

	def setCol(self, j, col):
		for i in range(self.m):
			self.me[i][j] = col[i]

	def __str__(self):
		string = ""
		for i in range(self.m):
			string += "" + str(self.me[i]) + "\n"
		return string
