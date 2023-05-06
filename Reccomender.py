from math import sqrt

class Recommender:
	def __init__(self, recepies) -> None:
		self.recepies = recepies


	def get_recommendation(self, matching_pattern, minimum_ingrediences):
		max_value = 0
		that_recepie = None
		that_no_data = 0
		for recepie in self.recepies:
			value, count, no_data = self.calculate_similarity_ingrediences(recepie, matching_pattern)
			if count > 0:
				if value / count > max_value and no_data < 4 and count + no_data >= minimum_ingrediences:
					max_value = value / count
					that_recepie = recepie
					that_no_data = no_data
		return [max_value, that_recepie, that_no_data]
	
	def compare_recepies(self, recepie1, recepie2):
		numerator = 0
		denominator = 0

		keys = []
		keys += list(recepie1.keys())
		keys += list(recepie2.keys())

		keys = list(set(keys))

		for key in keys:
			if key in recepie1 and key in recepie2:
				numerator += recepie1[key] * recepie2[key]
		
		#----------------------------------------------
		valuex = 0
		for key in recepie1:
			valuex += recepie1[key] ** 2
		valuex = sqrt(valuex)

		valuey = 0
		for key in recepie2:
			valuey += recepie2[key] ** 2
		valuey = sqrt(valuey)

		denominator = valuex * valuey

		return numerator / denominator
		

	def calculate_similarity_ingrediences(self, recepie, matching_pattern):
		value = 0
		count = 0
		no_data = 0
		for element in recepie.ingredience:
			try:
				value += matching_pattern[element]
				count += 1
			except:
				no_data += 1
			

		return [value, count, no_data]