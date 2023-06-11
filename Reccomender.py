from math import sqrt
from recepie import Recepie
from favourite_ingredience import Favourite_ingrediences

class Recommender:
	def __init__(self, recepies) -> None:
		self.recepies = recepies


	def get_recommendation(self, matching_pattern, minimum_ingrediences):
		max_value = 0
		that_recepie = 0
		that_no_data = 0
		for i in range(len(self.recepies)):
			#value, count, no_data = self.calculate_similarity_ingrediences(self.recepies[i], matching_pattern)

			# if count > 0:
			# 	if value / count > max_value: #and no_data < 4 and count + no_data >= minimum_ingrediences:
			# 		max_value = value / count
			# 		that_recepie = i
			# 		that_no_data = no_data

			value = self.compare_recepies(matching_pattern, self.recepies[i])
			if max_value < value:
				max_value = value
				that_recepie = i

		return [max_value, that_recepie, that_no_data]
	
	def compare_recepies(self, matching_pattern: dict, recepie: Recepie):
		if not isinstance(recepie, Recepie):
			raise ValueError(f"recepie is {type(recepie)}")
		
		if not isinstance(matching_pattern, Favourite_ingrediences):
			raise ValueError(f"matching_pattern is {type(matching_pattern)}")

		numerator = 0
		denominator = 0

		keys = []
		keys += list(matching_pattern.sums.keys())
		keys += recepie.ingredience

		keys = list(set(keys))

		for key in keys:
			if key in recepie.ingredience and key in matching_pattern.sums:
				numerator += 1 * (matching_pattern.sums[key] / matching_pattern.counts[key])
		
		#----------------------------------------------
		valuex = 0
		for key in matching_pattern.sums:
			valuex += (matching_pattern.sums[key] / matching_pattern.counts[key]) ** 2
		valuex = sqrt(valuex)

		valuey = 0
		for key in recepie.ingredience:
			valuey += 1 ** 2
		valuey = sqrt(valuey)

		denominator = valuex * valuey

		try:
			return numerator / denominator
		except:
			return -1000
		

	def calculate_similarity_ingrediences(self, recepie, matching_pattern):
		value = 0
		count = 0
		no_data = 0
		print("matching_pattern:")
		print(matching_pattern)
		for element in recepie.ingredience:
			try:
				value += matching_pattern[element]
				count += 1
			except:
				no_data += 1
			

		return [value, count, no_data]