from recepie_type_profile import Recepie_type_profile
from recepie import Recepie
from comparing_methods import cosine_compare
from data_manipulation_functions import list_to_dict_value_appearance

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

		for recepie_type in self.types.values():
			calculated_value = cosine_compare(recepie_type.elements, recepie.instructions_appearance)

			if calculated_value >= maximum_value:
				recepie_type_name = recepie_type.name
				second_maximum = maximum_value
				maximum_value = calculated_value
		
		#if second_maximum > 0.75 * second_maximum:
			#return "not able to decide"
		return recepie_type_name
			



