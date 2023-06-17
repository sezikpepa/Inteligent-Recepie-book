from math import sqrt
from functools import cache


def cosine_compare(values1: dict, values2: dict):
	if not isinstance(values1, dict):
		raise ValueError(f"values1 is {type(values1)}")
	
	if not isinstance(values2, dict):
		raise ValueError(f"values2 is {type(values2)}")

	numerator = 0
	denominator = 0

	keys = []
	keys += values1.keys()
	keys += values2.keys()

	keys = list(set(keys))

	for key in keys:
		if key in values1.keys() and key in values2.keys():
			numerator += values1[key] * values2[key]
	
	#----------------------------------------------
	valuex = 0
	for key in values1.keys():
		valuex += values1[key] ** 2
	valuex = sqrt(valuex)

	valuey = 0
	for key in values2.keys():
		valuey += values2[key] ** 2
	valuey = sqrt(valuey)

	denominator = valuex * valuey

	try:
		return numerator / denominator
	except:
		return -1000
