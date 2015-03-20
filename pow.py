# x^n power law

class Solution:
	def pow(self, x, n):
		if n==0:
			return 1.0
		elif n ==1:
			return x
		elif n < 0:
			return 1.0 / self.pow(x, -n)
		else:
			return self.pow(x, n / 2) * self.pow(x, n - n / 2)

print(pow(3,3))