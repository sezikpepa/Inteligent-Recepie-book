import csv


class Favourite_ingrediences:
	def __init__(self):
		self.sums = {}
		self.counts = {}

	def add_rating(self, ingredience, rating) -> None:
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
		with open(file_name, "w") as file:
			csv_writer = csv.writer(file)
			for key in self.sums.keys():
				to_write = [key, self.sums[key], self.counts[key]]
				
				csv_writer.writerow(to_write)



	def load_from_file(self, file_name: str):
		with open(file_name, "r") as file:
			csv_reader = csv.reader(file, delimiter=",")

			self.sums.clear()
			self.sums.clear()

			for row in csv_reader:
				if len(row) == 3:
					try:
						self.sums[row[0]] = float(row[1])
					except:
						print(row[1])
						print(type(row[1]))
					self.counts[row[0]] = int(row[2])
