import csv
import settings

class Recepie_type_profile:
	def __init__(self, name: str):
		if not isinstance(name, str):
			raise ValueError(f"name is {type(name)}")
		

		self.name: str = name

		self.elements: dict = {}

	def add_elements(self, elements: list):
		if not isinstance(elements, list):
			raise ValueError(f"elements is {type(elements)}")
		
		for element in elements:
			if element in self.elements.keys():
				self.elements[element] += 1
			else:
				self.elements[element] = 1

		self.save_to_file()

	def load_from_file(self):
		file_path = settings.recepie_type_profiles_path + self.name + ".csv"
		try:
			with open(file_path, "r") as file:
				csv_reader = csv.reader(file, delimiter=",")

				self.elements.clear()

				for row in csv_reader:
					if len(row) <= 0:
						continue
					if len(row) == 2:
						self.elements[row[0]] = int(row[1])
					else:
						print(f"invalid element in row {row}")

		except:
			print(f"file was not found in {file_path}")
			return
			

		print(f"{self.name} profile was load from file")

	def save_to_file(self):
		with open(settings.recepie_type_profiles_path + self.name + ".csv", "w") as file:
			csv_writer = csv.writer(file)

			for key in self.elements:
				to_write = [key, self.elements[key]]
				csv_writer.writerow(to_write)

		print(f"{self.name} profile was saved to file")