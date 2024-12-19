class Vector:
	def __init__(self, nums):
		self.length = len(nums)
		self.me = nums

	def len(self):
		return self.length
	
	def get(self, i=None):
		if i == None: return self.me
		else: return self.me[i]

	def __str__(self):
		return "" + str(self.me)

	def __len__(self):
		return self.length