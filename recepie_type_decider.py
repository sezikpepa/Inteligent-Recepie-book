from recepie_type_profile import Recepie_type_profile
from recepie import Recepie
from comparing_methods import cosine_compare
from data_manipulation_functions import list_to_dict_value_appearance, shift_cosine_value_weight

class Recepie_type_decider:
    
	def __init__(self):
		self.types: dict = {}

	def add_new_type(self, recepie_type: Recepie_type_profile):
		if not isinstance(recepie_type, Recepie_type_profile):
			raise ValueError(f"type is {type(recepie_type)}")
		
		if recepie_type.name in self.types.keys():
			raise ValueError(f"{recepie_type.name} is already in the decider")

		self.types[recepie_type.name] = recepie_type


	def get_recepie_type(self, recepie: Recepie):
		if not isinstance(recepie, Recepie):
			raise ValueError(f"recepie is {type(recepie)}")

		maximum_value: float = -10000
		second_maximum: float = -20000
		recepie_type_name: str = ""
		second_recepie_type_name: str = ""

		values_sum = 0
		calculated_value = 0

		for recepie_type in self.types.values():
			try:
				calculated_value = cosine_compare(recepie_type.elements, recepie.instructions_appearance)
			except ZeroDivisionError:
				calculated_value = 0

			values_sum += calculated_value

			if recepie_type_name == "":
				second_recepie_type_name = recepie_type_name
				recepie_type_name = recepie_type.name
				second_maximum = maximum_value
				maximum_value = calculated_value
				continue

			if shift_cosine_value_weight(calculated_value, self.types[recepie_type.name].get_number_of_known_words(), self.types[recepie_type_name].get_number_of_known_words()) >= maximum_value:
				second_recepie_type_name = recepie_type_name
				recepie_type_name = recepie_type.name
				second_maximum = maximum_value
				maximum_value = shift_cosine_value_weight(calculated_value, self.types[recepie_type.name].get_number_of_known_words(), self.types[recepie_type_name].get_number_of_known_words())

		
		#if second_maximum > 0.9 * second_maximum:
			#return "not able to decide"

		if maximum_value < 0.2  * values_sum:
			return "not able to decide"
		
		#if maximum_value * 0.8 < second_maximum:
			#return "not able to decide"
		
		if maximum_value < 0.2:
			return "not able to decide"

		
		print(maximum_value)
		print(values_sum)
		print(second_recepie_type_name)
		print(recepie_type_name)

		print()

		return recepie_type_name
			



