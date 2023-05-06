class Recepie:
	def __init__(self, name, ingredience, instructions, image_name):
		self.name: str = name


		self.ingredience: list = [x for x in ingredience if len(x.strip())>1]


		self.instructions: str = instructions
		self.image_name: str = image_name

		self.vector = {}

	def generate_vector(self):
		self.vector = {}
		count = 0
		for word in self.instructions:
			if word in self.vector:
				self.vector[word] += 1
			else:
				self.vector[word] = 1
			count += 1

		for key in self.vector:
			self.vector[key] = self.vector[key] / count

	def __str__(self):
		toReturn = ""

		toReturn += "name: \n"
		toReturn += self.name
		toReturn += "\n"
		toReturn += "\n"

		toReturn += "ingredience: \n"
		for element in self.ingredience:
			toReturn += element + "\n"
		toReturn += "\n"
		toReturn += "\n"

		toReturn += "instructions: \n"
		for element in self.instructions:
			toReturn += element + " "
		toReturn += "\n"
		toReturn += "\n"

		toReturn += "image name: \n"
		toReturn += self.image_name
		toReturn += "\n"
		toReturn += "\n"

		return toReturn