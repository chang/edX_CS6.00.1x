from math import tan, pi

def polysum(n, s):
	'''
	sums the area and square of the perimeter of a polygon with n sides and side length s
	'''
	def area(n, s):
		'''
		returns area of polygon with n sides and side length s
		'''
		area = (.25*n*s**2)/tan(pi/n)
		return area

	def perimeter(n, s):
		'''
		returns perimeter of polygon with n sides and side length s
		'''
		return n * s

	return round(area(n, s) + perimeter(n, s)**2, 4)