class Recepie:
	def __init__(self, name: str, ingredience_full: list, instructions_full: str, image_name: str):
		if not isinstance(name, str):
			raise ValueError(f"name is {type(name)}")

		if not isinstance(ingredience_full, list):
			raise ValueError(f"ingredience_full is {type(ingredience_full)}")

		if not isinstance(instructions_full, str):
			raise ValueError(f"instructions_full is {type(instructions_full)}")
		
		if not isinstance(image_name, str):
			raise ValueError(f"image_name is {type(image_name)}")

		self.name: str = name

		self.instructions_full: str = instructions_full
		self.ingredience_full: str = ingredience_full

		self.instructions: list = []
		self.ingredience: list = []

		self.instructions_appearance: dict = {}

		self.image_name: str = image_name

		self.vector = {}

	def insert_from_json(self, recepie_json: dict):
		if not isinstance(recepie_json, dict):
			raise ValueError(f"recepie_json is {type(recepie_json)}")
		
		self.name = recepie_json["name"]
		self.instructions = recepie_json["instructions"]
		self.instructions_full = recepie_json["instructions_full"]
		self.ingredience = recepie_json["ingredience"]
		self.ingredience_full = recepie_json["ingredience_full"]
		self.image_name = recepie_json["image_name"]

	def generate_vector(self):
		self.vector = {}
		count = 0
		for word in self.instructions:
			if word in self.vector:
				self.vector[word] += 1
			else:
				self.vector[word] = 1
			count += 1

		for key in self.vector:
			self.vector[key] = self.vector[key] / count

	def __str__(self):
		toReturn = ""

		toReturn += "name: \n"
		toReturn += self.name
		toReturn += "\n"
		toReturn += "\n"

		toReturn += "ingredience: \n"
		for element in self.ingredience:
			toReturn += element + "\n"
		toReturn += "\n"
		toReturn += "\n"

		toReturn += "ingredience_full: \n"
		for element in self.ingredience_full:
			toReturn += element + "\n"
		toReturn += "\n"
		toReturn += "\n"

		toReturn += "instructions: \n"
		for element in self.instructions:
			toReturn += element + " "
		toReturn += "\n"
		toReturn += "\n"

		toReturn += "instructions_full: \n"
		toReturn += self.instructions_full
		toReturn += "\n"
		toReturn += "\n"

		toReturn += "image name: \n"
		toReturn += self.image_name
		toReturn += "\n"
		toReturn += "\n"

		return toReturn
	
	def to_dict(self):
		return {
			"name": self.name,
			"ingredience": self.ingredience,
			"ingredience_full": self.ingredience_full,
			"instructions": self.instructions,
			"instructions_full": self.instructions_full,
			"image_name": self.image_name
		}