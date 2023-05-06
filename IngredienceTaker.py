import re
#11156
class IngredienceTaker:
	def __init__(self, ingredience: list) -> None:
		self.ingredience = ingredience 

	def do_magic(self):
		self.remove_things_in_brackets()
		self.remove_after()
		self.to_lower_case()
		self.remove_non_letters()
		self.split_ingredients()
		self.remove_nonneeded_words()
		self.remove_white_speces_around()
		self.remove_duplicities()
		self.remove_white_speces_around()
		self.remove_long_ingredience()
		self.connect_possible_connections()

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

	def split_ingredients(self):
		new_list = []
		new_list2 = []

		for element in self.ingredience:
			toappend = element.split(" and ")
			for element2 in toappend:
				new_list.append(element2)

		for element in new_list:
			toappend2 = element.split(" with ") #maybe dont work
			for element3 in toappend2:
				new_list2.append(element3)

		self.ingredience = new_list2

	def remove_nonneeded_words(self):
		new_list = []

		words_without_meaning = ["the","of", "to", "other", "plus", "top", "a", "an", "choice","for", "by", "enough", "up", "about", "x", "xx", "your", "favourite", "you", "will", "in", "any"]
		colors = ["white", "black", "purple", "red"]
		units = ["half", "halves","double","each","milliliter","gram","handful","fl","gallon","few","cubes","four","liter","six","slice","pieces","l","lbs","s","us", "use","t","tbs","ten","xxinch","xinch","three","two","percent","ml", "grams","oz", "lb", "kg", "qt", "pound", "pounds", "g", "ounces", "aj", "one", "ounce", "bag", "bags", "inch", "single", "ml"]
		size_words = ["as needed","splash","several","inchwide","inchdiameter","inchlong","quarts", "quart","slices","small", "medium", "big", "large", "whole", "head", "inchthick", "mini", "mediumsize"]
		things_sizes = ["stick","cloves","bottles","halves","sprigs","tiny","teapoon","pinch","pint", "pints", "sheet", "sheets","tube","box","bottle","bunch", "package", "packages", "tsp", "tbsp", "cup", "teaspoon", "teaspoons", "pan","tablespoon", "tablespoons","can", "jar", "jars", "cans", "cups"]
		adjectives = ["sticks","fashioned","old","shelled","finequality","converted","hotsmoked","melted","nonhydrogenated","strong","bunches","nonfat","aged","jumbo","neutral","freerange","nonstick","flaky","kosher","lowsalt","bittersweet","roomtemperature","percentfat","low","mature","preserved","doubleconcentrated","reducedfat","baby", "shaved","available","assorted","seedless","mediumdry","mild","cracked","vacuumpacked","quality","chilled","unseasoned","smashed","squeezed","topquality","round","crispy","crisp","crusty","sushigrade","milled","extralarge","extravirgin","fatfree","favorite","tightly","tiny","lowsodium","organic","lowfat","natural","goodquality","leftover","premium","prepared","mediumlarge","mediumsized","mediumthin","fine","garnish","minced","ripe","dried","light","heaping","highquality","homemade","packaged","frozen","plain","shortgrain","simple","crumbled","shredded","pitted","fully", "fried", "froznen","imported","jarred","lightly","little","square","squares","storebought","purchased","long", "local","wellchilled","wellmarbled","wellseasoned","short","thin","wild","young","trimmed","unpeeled","precooked","thick","gigante","boneless", "piece","very","new", "peeled","accompaniments","heavy","wide","accompaniment","centercut", "packed", "loosely", "canned", "mixed", "warm", "skinless", "heaped", "zest", "good", "generous", "amount", "boiling", "sharp", "coarsely", "thinly", "sliced", "wavy", "pure", "regular", "ground", "rrated", "smoked", "finely", "chopped", "freshly", "fresh", "hot", "cold", "diced", "crushed", "grated", "roasted", "pickled", "roughly", "toasted", "extra"]
		countries = ["italian", "english"]
		random = ["at room temperature minutes"]

		nonneeded_words = size_words + things_sizes + colors + adjectives + words_without_meaning + units + countries + random

		for element in self.ingredience:
			new_list.append(''.join([" " + i + " " for i in element.split(" ") if i not in nonneeded_words]))

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
			new_list.append(to_append)

		self.ingredience = new_list

	def remove_duplicities(self):
		self.ingredience = list(set(self.ingredience))

	def remove_long_ingredience(self):
		new_list = []

		for element in self.ingredience:
			if len(element) < 40:
				new_list.append(element.strip())
		self.ingredience = new_list

	def connect_possible_connections(self):
		new_list = []

		for element in self.ingredience:
			to_append = element.replace("allpurpose", "all purpose")
			new_list.append(to_append)

		self.ingredience = new_list


	def __str__(self):
		toReturn = ""
		for element in self.ingredience:
			toReturn += element + "\n"

		return toReturn