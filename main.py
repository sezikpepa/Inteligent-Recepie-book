from Recepie_Creator import Recepie_Creator
from IngredienceTaker import IngredienceTaker
from StatisticsCreator import StatisticsCreator
from MakingProcessMaker import MakingProcessMaker
from Reccomender import Recommender
import pprint
import numpy as np
import settings

if __name__ == '__main__':
	recepie_creator = Recepie_Creator()

	recepie_creator.LoadFile(settings.dataset)
	statistics = StatisticsCreator()

	repeat = len(recepie_creator.recepies)
	for i in range(repeat):
		process_maker = MakingProcessMaker(recepie_creator.recepies[i].instructions.split(" "))
		ingredience_taker = IngredienceTaker(recepie_creator.recepies[i].ingredience)

		ingredience_taker.do_magic()
		process_maker.do_magic()

		recepie_creator.recepies[i].instructions = process_maker.processes
		recepie_creator.recepies[i].ingredience = ingredience_taker.ingredience

		


	print("loaded")

	for recepie in recepie_creator.recepies:
		statistics.add(recepie.ingredience)
	


	statistics.calculate_statistic()
	statistics.calculate_word_count()

	keys = list(statistics.words.keys())
	values = list(statistics.words.values())
	sorted_value_index = np.argsort(values)
	sorted_dict = {keys[i]: values[i] for i in sorted_value_index}

	print(sorted_dict)
	print("single words: " + str(len(sorted_dict)))
	print("ingredience_count: " + str(len(statistics.ingredinces_values)))






