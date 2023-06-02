class StatisticsCreator:
	def __init__(self) -> None:
		self.ingrediences = []
		self.words = {}
		self.ingredinces_values = {}

	def add(self, ingrediences):
		self.ingrediences += ingrediences

	def calculate_statistic(self):
		for element in self.ingrediences:
			#splitted = element.split(" ")
			if element in self.ingredinces_values:
				self.ingredinces_values[element] += 1
			else:
				self.ingredinces_values[element] = 1

	def calculate_word_count(self):
		for element in self.ingrediences:
			for part in element.split(" "):
				if part in self.words:
					self.words[part] += 1
				else:
					self.words[part] = 1
	
	# def __str__(self):
	# 	toReturn = ""
	# 	for element in self.ingredinces_values:
	# 		toReturn += element.key
	# 		toReturn += ": "
	# 		toReturn += element.value
	# 		toReturn += "\n\n"

	# 	return toReturn