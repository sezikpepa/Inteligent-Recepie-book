import settings
import csv

class Delayed_recepie_handler:
	@staticmethod
	def load_delayed_recepies() -> dict:
		delayed_recepies = {}

		try:
			with open(settings.delayed_recepies_file_name, "r") as reader:
				csv_reader = csv.reader(reader, delimiter=",")


				for row in csv_reader:
					if len(row) == 0:
						continue
					if len(row) != 2:
						print(f"invalid line {row}")
						continue
					delayed_recepies[int(row[0])] = row[1]
		
		except FileNotFoundError:
			print(f"file on {settings.delayed_recepies_file_name} was not found") 
			return {}

		return delayed_recepies	

	@staticmethod
	def store_delay_recepies(delayed_recepies: dict) -> None:
		if not isinstance(delayed_recepies, dict):
			raise ValueError(f"delayed_recepies is {type(delayed_recepies)}")
		

		with open(settings.delayed_recepies_file_name, "w") as writer:
			csv_writer = csv.writer(writer, delimiter=",")

			for key in delayed_recepies.keys():
				csv_writer.writerow([key, delayed_recepies[key]])
		


