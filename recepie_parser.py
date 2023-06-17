from Recepie_Creator import Recepie_Creator
from IngredienceTaker import IngredienceTaker
from StatisticsCreator import StatisticsCreator
from MakingProcessMaker import MakingProcessMaker
from Reccomender import Recommender
import pprint
import numpy as np
import settings
import json
import os
from data_manipulation_functions import list_to_dict_value_appearance

if __name__ == '__main__':
	recepie_creator = Recepie_Creator()

	recepie_creator.LoadFile(settings.dataset)
	statistics = StatisticsCreator()

	repeat = len(recepie_creator.recepies)
	for i in range(repeat):
		process_maker = MakingProcessMaker(recepie_creator.recepies[i].instructions_full)
		ingredience_taker = IngredienceTaker(recepie_creator.recepies[i].ingredience_full)

		ingredience_taker.do_magic()
		process_maker.do_magic()

		recepie_creator.recepies[i].instructions = process_maker.instructions
		recepie_creator.recepies[i].ingredience = ingredience_taker.ingredience
		recepie_creator.recepies[i].instructions_appearance = list_to_dict_value_appearance(recepie_creator.recepies[i].instructions)

		print(f"recepie number {i} parsed")


	if os.path.exists(settings.json_data):
		os.remove(settings.json_data)

	recepie_data = {"recepies": {}}

	for i, element in enumerate(recepie_creator.recepies):
		recepie_data["recepies"][i] = element.to_dict()


	with open(settings.json_data, "w") as file:
		json.dump(recepie_data, file, indent=4)
