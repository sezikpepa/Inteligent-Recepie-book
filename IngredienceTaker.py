import re

class IngredienceTaker:
	def __init__(self, ingredience: list) -> None:
		self.ingredience = ingredience 


	def remove_things_in_brackets(self):
		new_list = []

		for element in self.ingredience:
			new_list.append(re.sub("\(.*?\)","",element))

		self.ingredience = new_list

	def remove_non_letters(self):
		valid_letters = "qwertzuioplkjhgfdsayxcvbnmQWERTZUIOPLKJHGFDSAYXCVBNM "
		new_list = []

		for element in self.ingredience:
			new_list.append(''.join([i for i in element if i in valid_letters]))

		self.ingredience = new_list

	def remove_after(self):
		new_list = []

		for element in self.ingredience:
			toappend = element.split(",")[0]
			toappend = toappend.split(" or ")[0]
			toappend = toappend.split(" such as ")[0]
			toappend = toappend.split(" from ")[0]
			toappend = toappend.split(" but ")[0]
			new_list.append(toappend)

		self.ingredience = new_list

	def remove_nonneeded_words(self):
		new_list = []

		words_without_meaning = ["of", "to", "other", "plus", "a", "an", "for", "by", "enough", "up", "about"]
		colors = ["white", "black", "purple", "red"]
		units = ["oz", "lb", "kg", "qt", "pound", "pounds", "g", "ounces", "aj", "one", "ounce", "bag", "bags", "inch", "single"]
		size_words = ["small", "medium", "big", "large", "whole", "head", "inchthick", "mini", "mediumsize"]
		things_sizes = ["bunch", "package", "packages", "tsp", "tbsp", "cup", "teaspoon", "teaspoons", "pan","tablespoon", "tablespoons","can", "jar", "jars", "cans", "cups"]
		adjectives = ["accompaniments","heavy","wide","accompaniment","centercut", "packed", "loosely", "canned", "mixed", "warm", "skinless", "heaped", "zest", "good", "generous", "amount", "boiling", "sharp", "coarsely", "thinly", "sliced", "wavy", "pure", "regular", "ground", "rrated", "smoked", "finely", "chopped", "freshly", "fresh", "hot", "cold", "diced", "crushed", "grated", "roasted", "pickled", "roughly", "toasted", "extra"]

		nonneeded_words = size_words + things_sizes + colors + adjectives + words_without_meaning + units

		for element in self.ingredience:
			new_list.append(''.join([i + " " for i in element.split(" ") if i not in nonneeded_words]))

		self.ingredience = new_list

	def to_lower_case(self):
		new_list = []

		for element in self.ingredience:
			new_list.append(element.lower())

		self.ingredience = new_list

	def remove_white_speces_around(self):
		new_list = []

		for element in self.ingredience:
			to_append = element.strip()
			to_append = re.sub("  ", " ", to_append)
			new_list.append(element.strip())

		self.ingredience = new_list

	def remove_duplicities(self):
		self.ingredience = list(set(self.ingredience))

	def remove_long_ingredience(self):
		new_list = []

		for element in self.ingredience:
			if len(element) < 40:
				new_list.append(element.strip())
		self.ingredience = new_list


	def __str__(self):
		toReturn = ""
		for element in self.ingredience:
			toReturn += element + "\n"

		return toReturn