from math import sqrt
from recepie import Recepie
from favourite_ingredience import Favourite_ingrediences
from recepie_type_decider import Recepie_type_decider

class Recommender:
	def __init__(self, recepies) -> None:
		self.recepies = recepies
		self.recepie_type_decider = None

	def set_recepie_type_decider(self, recepie_type_decider):
		if not isinstance(recepie_type_decider, Recepie_type_decider):
			raise ValueError(f"recepie_type_decider is {type(recepie_type_decider)}")
		
		self.recepie_type_decider = recepie_type_decider


	def get_recommendation(self, matching_pattern, minimum_ingrediences, delayed_recepies: dict, recepie_type: str):
		if not isinstance(delayed_recepies, dict):
			raise ValueError(f"delay_recepies is {type(delayed_recepies)}")
		if not isinstance(recepie_type, str):
			raise ValueError(f"recepie_type is {type(recepie_type)}")

		max_value = 0
		that_recepie = 0
		that_no_data = 0
		for i in range(len(self.recepies)):
			if i in delayed_recepies.keys():
				continue

			if self.recepie_type_decider.get_recepie_type(self.recepies[i]) != recepie_type:
				continue

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