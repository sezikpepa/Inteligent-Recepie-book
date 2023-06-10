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
		#self.remove_includings()		
		self.remove_duplicities()
		self.remove_white_speces_around()
		self.remove_words_with_specific_ending()
		#self.remove_words_with_specific_prefix()
		self.remove_long_ingredience()
		self.connect_possible_connections()
		self.remove_white_speces_around()
		self.remove_short_ingrediences()

	def remove_things_in_brackets(self):
		new_list = []

		for element in self.ingredience:
			new_list.append(re.sub("\(.*?\)","",element))

		self.ingredience = new_list

	def remove_non_letters(self):
		valid_letters = "qwertzuioplkjhgfdsayxcvbnmQWERTZUIOPLKJHGFDSAYXCVBNM "
		new_list = []

		for element in self.ingredience:
			new_list.append("".join([ letter if letter in valid_letters else " " for letter in element ]))

		self.ingredience = new_list

	def remove_short_ingrediences(self):
		new_list = []

		for element in self.ingredience:
			if len(element) > 2:
				new_list.append(element)


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

	def remove_includings(self):
		new_list = []

		
		for element in self.ingredience:
			new_list.append(self.is_in(element))




		self.ingredience = new_list

	def is_in(self, test_word):
		for element in self.ingredience:
			if test_word == element + "s":
				print(test_word)
				return element
			elif test_word == element + "es":
				return element
		return test_word



	def remove_nonneeded_words(self):
		new_list = []

		words_without_meaning = ["the","of", "to", "other", "plus", "top", "a", "an", "choice","for", "by", "enough", "up", "about", "x", "xx", "your", "favourite", "you", "will", "in", "any"]
		colors = ["white", "black", "purple", "red", "yellow", "orange", "green", "gold", "blue", "slow", "rock"]
		units = ["half", "halves","double","each","milliliter","gram","handful","fl","gallon","few","cubes","four","liter","six","slice","pieces","l","lbs","s","us", "use","t","tbs","ten","xxinch","xinch","three","two","percent","ml", "grams","oz", "lb", "kg", "qt", "pound", "pounds", "g", "ounces", "aj", "one", "ounce", "bag", "bags", "inch", "single", "ml"]
		size_words = ["as needed","splash","several","inchwide","inchdiameter","inchlong","quarts", "quart","slices","small", "medium", "big", "large", "whole", "head", "inchthick", "mini", "mediumsize"]
		things_sizes = ["stick","cloves","bottles","halves","sprigs","tiny","teapoon","pinch","pint", "pints", "sheet", "sheets","tube","box","bottle","bunch", "package", "packages", "tsp", "tbsp", "cup", "teaspoon", "teaspoons", "pan","tablespoon", "tablespoons","can", "jar", "jars", "cans", "cups"]
		adjectives = ["sticks","fashioned","old","shelled","finequality","converted","hotsmoked","melted","nonhydrogenated","strong","bunches","nonfat","aged","jumbo","neutral","freerange","nonstick","flaky","kosher","lowsalt","bittersweet","roomtemperature","percentfat","low","mature","preserved","doubleconcentrated","reducedfat","baby", "shaved","available","assorted","seedless","mediumdry","mild","cracked","vacuumpacked","quality","chilled","unseasoned","smashed","squeezed","topquality","round","crispy","crisp","crusty","sushigrade","milled","extralarge","extravirgin","fatfree","favorite","tightly","tiny","lowsodium","organic","lowfat","natural","goodquality","leftover","premium","prepared","mediumlarge","mediumsized","mediumthin","fine","garnish","minced","ripe","dried","light","heaping","highquality","homemade","packaged","frozen","plain","shortgrain","simple","crumbled","shredded","pitted","fully", "fried", "froznen","imported","jarred","lightly","little","square","squares","storebought","purchased","long", "local","wellchilled","wellmarbled","wellseasoned","short","thin","wild","young","trimmed","unpeeled","precooked","thick","gigante","boneless", "piece","very","new", "peeled","accompaniments","heavy","wide","accompaniment","centercut", "packed", "loosely", "canned", "mixed", "warm", "skinless", "heaped", "zest", "good", "generous", "amount", "boiling", "sharp", "coarsely", "thinly", "sliced", "wavy", "pure", "regular", "ground", "rrated", "smoked", "finely", "chopped", "freshly", "fresh", "hot", "cold", "diced", "crushed", "grated", "roasted", "pickled", "roughly", "toasted", "extra", "wholewheat", "wholemilk", "wholegrain", "whipped", "wellstirred", "welltrimmed", "unsweetened", "unsalted", "untrimmed", "unwaxed", "unsliced", "thawed"]
		countries = ["italian", "english"]
		random = ["at room temperature minutes"]
		frequent_adjectives = ["granulated", "high", "size", "seeds", "leaves", "herbs", "wedge", "wedges", "japanese", "reduced", "thermometer", "five", "table", "grand", "iron", "range", "duty", "additional", "sized", "plate", "latin", "freeze", "bought", "well", "chinese", "quick", "dish","all", "purpose", "virgin", "electric", "flat", "steamed", "deepfry", "extrasharped","sweet", "drained", "cooked", "golden", "dry", "firm", "more", "cooking", "raw", "cubed", "specialty", "halved", "diamond", "mixer", "removable", "rolled", "mexican", "diameter", "striped", "flameproof", "tin", "icing", "eight", "slivered", "pink", "french", "firmly", "flaked", "mix", "powdered", "extract", "powder", "dark", "soft", "bottled", "swiss", "oldfashioned", "blanched", "uncooked", "spanish", "korean", "bowl", "cooker", "rimmed", "indian", "optional", "sifted", "seasoned", "reserved", "unbleached", "seeded", "brown", "asian", "oilpacked", "metal", "rouned", "crystallized", "hardboiled", "recipe", "winter", "solid", "quatered", "sweetened", "distilled", "unflavored", "condensed", "rounded", "redskinned", "fitted", "brewed", "grilled", "sundried", "candied", "cleaned", "fluted", "mashed", "brinecured", "deveined", "hulled", "marinated", "stemmed", "refrigerated", "quatered", "evaporated", "oilcured", "strained", "softened", "active", "semisweet", "thai", "temperature", "container", "pans", "note", "baking", "whipping", "king"]

		nonneeded_words = size_words + frequent_adjectives + things_sizes + colors + adjectives + words_without_meaning + units + countries + random

		for element in self.ingredience:
			new_list.append(''.join([" " + i + " " for i in element.split(" ") if i not in nonneeded_words]))



		self.ingredience = new_list

	def remove_words_with_specific_ending(self):
		new_list = []
		
		for element in self.ingredience:
			new_list.append(''.join([" " + i + " " for i in element.split(" ") if not i.endswith("ing") and not i.endswith("ian") and not i.endswith("red") and not i.endswith("ied")and not i.endswith("can") and not i.endswith("ked") and not i.endswith("ned") and not i.endswith("sed") and not i.endswith("style") and not i.endswith("led") and not i.endswith("tly") and not i.endswith("hed") and not i.endswith("den") and not i.endswith("ial")]))


		self.ingredience = new_list

	def remove_words_with_specific_prefix(self):
		new_list = []
		#print(" cream".startswith("all"))
		for element in self.ingredience:
			new_list.append(''.join([" " + i + " " for i in element.split(" ") if i[0] == 'u' and i[1] == 'n']))


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