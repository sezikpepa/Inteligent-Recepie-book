import numbers


def list_to_dict_value_appearance(values: list) -> dict:
	if not isinstance(values, list):
		raise ValueError(f"values is {type(values)}")
		
	to_return = {}

	for value in values:
		if value in to_return.keys():
			to_return[value] += 1

		else:
			to_return[value] = 1

	return to_return


def shift_cosine_value_weight(value: float, count1: int, count2: int):
	if not isinstance(value, numbers.Number):
		raise ValueError(f"value is {type(value)}")
	if not isinstance(count1, int):
		raise ValueError(f"count1 is {type(count1)}")
	if not isinstance(count2, int):
		raise ValueError(f"count2 is {type(count2)}")
	

	try:
		return (count1 / count2) * value
	except ZeroDivisionError:
		return -1000

	

