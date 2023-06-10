from recepie import Recepie
import csv

class Recepie_waiting_time_handler:
	def __init__(self) -> None:
		self.recepies_with_waiting_time = []


	def write_new_recepie(self, recepie, file_name):
		if not isinstance(recepie, Recepie):
			raise ValueError(f"recepie is {type(recepie)}")
		
		if not isinstance(file_name, str):
			raise ValueError(f"file_name is {type(file_name)}")
		
		with open(file_name, "w") as file:
			csv_writer = csv.writer(file)
			for key in self.sums.keys():
				to_write = [key, self.sums[key], self.counts[key]]
				
				csv_writer.writerow(to_write)