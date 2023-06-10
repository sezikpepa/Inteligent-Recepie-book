class Favourite_ingrediences:
	def __init__(self):
		self.sums = {}
		self.counts = {}

	def add_rating(self, ingredience, rating):

		if ingredience in self.sums:
			self.sums[ingredience] += rating
			self.counts[ingredience] += 1

		else:
			self.sums[ingredience] = rating
			self.counts[ingredience] = 1

	def get_favouritness(self):
		toReturn = {}

		for element in self.sums:
			toReturn[element] = self.sums[element] / self.counts[element]

		return toReturn
	
	def save_to_file(self, file_name: str):
		file = open(file_name, "w")
		for key in self.sums.keys():
			to_write = ""

			to_write += key
			to_write += ";"
			to_write += str(self.sums[key])
			to_write += ";"
			to_write += str(self.counts[key])
			to_write += "\n"

			file.write(to_write)

		file.close()
