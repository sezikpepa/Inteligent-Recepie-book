class StatisticsCreator:
	def __init__(self) -> None:
		self.ingrediences = []
		self.ingredinces_values = {}

	def add(self, ingrediences):
		self.ingrediences += ingrediences

	def calculate_statistic(self):
		for element in self.ingrediences:
			if element in self.ingredinces_values:
				self.ingredinces_values[element] += 1
			else:
				self.ingredinces_values[element] = 1
	
	# def __str__(self):
	# 	toReturn = ""
	# 	for element in self.ingredinces_values:
	# 		toReturn += element.key
	# 		toReturn += ": "
	# 		toReturn += element.value
	# 		toReturn += "\n\n"

	# 	return toReturn