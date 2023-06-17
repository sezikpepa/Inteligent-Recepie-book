def list_to_dict_value_appearance(values: list):
	if not isinstance(values, list):
		raise ValueError(f"values is {type(values)}")
		
	to_return = {}

	for value in values:
		if value in to_return.keys():
			to_return[value] += 1

		else:
			to_return[value] = 1

	return to_return
