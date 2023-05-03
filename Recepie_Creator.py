from recepie import Recepie
import csv

class Recepie_Creator:
	def __init__(self) -> None:
		self.recepies: list = [] 

	def LoadFile(self, file_path: str):
		with open(file_path, encoding="utf-8") as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			next(csv_reader)
			for row in csv_reader:
				self.recepies.append(self.create_recepie(row))
				

	def parse_file(self):
		pass

	def parse_recepie(self):
		pass

	def parse_line(self, line: str):
		splitted_line = line.split(",")
		return splitted_line
	
	def create_recepie(self, row: list):
		recepie = Recepie(row[1], row[2].split("'"), row[3], row[4] + ".jpg")
		return recepie
	
	def __str__(self):
		toReturn = ""
		for recepie in self.recepies:
			toReturn += str(recepie)
			toReturn += "---------------------------------------------------"
			toReturn += "\n\n"

		return toReturn