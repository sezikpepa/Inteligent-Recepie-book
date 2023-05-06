class Ingrediences:
	def __init__(self, elements):
		self.elements = elements
			

	def __str__(self):
		toReturn = ""

		for element in self.elements:
			toReturn += element + "\n"

		return toReturn