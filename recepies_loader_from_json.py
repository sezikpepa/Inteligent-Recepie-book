import settings
import json
from recepie import Recepie


class Recepies_loader_from_json:
	def __init__(self):
		self.recepies: list = []
		


	def read_from_json(self, path: str):
		if not isinstance(path, str):
			raise ValueError(f"path is {type(path)}")
		print("reading started")

		with open(path, "r") as reader:
			data = json.load(reader)

		for i in data['recepies']:
			recipe_id = str(i)
			recipe = data["recepies"][recipe_id]
			recepie = Recepie("", [], "", "")
			recepie.insert_from_json(recipe)
			self.recepies.append(recepie)

		print(f"{len(self.recepies)} recepies was loaded")


	def get_recepies(self):
		self.read_from_json(settings.json_data)
		return self.recepies
	

if __name__ == '__main__':
	loader = Recepies_loader_from_json()
	loader.read_from_json(settings.json_data)