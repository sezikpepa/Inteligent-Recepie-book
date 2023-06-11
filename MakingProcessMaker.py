class MakingProcessMaker:
	def __init__(self, instructions: str) -> None:
		if not isinstance(instructions, str):
			raise ValueError(f"instrutions is {type(instructions)}")


		self.instructions = instructions.split(" ")

	def do_magic(self):
		self.remove_nonletters()
		self.remove_words_without_meaning()


	def remove_nonletters(self):
		valid_letters = "qwertzuioplkjhgfdsayxcvbnmQWERTZUIOPLKJHGFDSAYXCVBNM "
		new_list = []

		for element in self.instructions:
			new_list.append(''.join([i.lower() for i in element if i in valid_letters]))

		self.instructions = new_list

	def remove_words_without_meaning(self):
		new_list = []

		useless_words = ["as","them","that","just", "these","for","well","same","all","then","it", "al", "x","not","when", "very","while","the","able", "about","can","you", "have","an", "f","if","a", "be", "by", "any", "an", "to", "are", "up", "on", "of", "in", "is", "or", "and", "from", "with", "at", "over", "into", "until", "but", "as", "will"]

		for element in self.instructions:
			if (element not in useless_words) and element != "":
				new_list.append(element)

		self.instructions = new_list