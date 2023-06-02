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

	""" pprint.pprint(statistics.ingredinces_values)
	print(len(statistics.ingredinces_values)) """

	""" pprint.pprint(statistics.words)
	print(len(statistics.words)) """

	keys = list(statistics.words.keys())
	values = list(statistics.words.values())
	sorted_value_index = np.argsort(values)
	sorted_dict = {keys[i]: values[i] for i in sorted_value_index}

	print(sorted_dict)
	print("single words: " + str(len(sorted_dict)))
	print("ingredience_count: " + str(len(statistics.ingredinces_values)))














	#print(recepie_creator.recepies[247])


""" 	recommender = Recommender(recepie_creator.recepies)
	recepie1 = {"test" : 0.2, "test2": 1}
	recepie2 = {"test" : 1}

	result = recommender.compare_recepies(recepie1, recepie2)
	print(result) """

	#succesful recommendation--------------------------------------------------------
	# recommender = Recommender(recepie_creator.recepies)
	
	# matching_pattern = {"olive oil": 0.5,
	# 					"bonein": 1,
	# 					"unbleached all purpose flour": 1,
	# 					"ginger": 0.1,
	# 					"leafy herbs": 1,
	# 					"salt": 1,
	# 					"swanson chicken broth": 1,
	# 					"noodles": 1,
	# 					"garlic": 1}
	# score, recepie, no_data = recommender.get_recommendation(matching_pattern, 6)

	# print(f"score {score}")
	# print(f"no data: {no_data}")
	# print(recepie)

	# recepie.generate_vector()
	# print(recepie.vector)
	#--------------------------------------------






	#for i in range(repeat):
		#print(recepie_creator.recepies[i])
		#print("-----------------------------------------------------------------------------")

	# for i in range(10000):
	# 	process_maker = MakingProcessMaker(recepie_creator.recepies[i].instructions.split(" "))
	# 	process_maker.remove_nonletters()
	# 	process_maker.remove_words_without_meaning()

		#print(process_maker.processes)
		#print(i)
		#print("-----------------------------------------------------------------------------")

	# statistics = StatisticsCreator()
	# for i in range(10000):
	# 	ingredience_taker = IngredienceTaker(recepie_creator.recepies[i].ingredience)
	# 	ingredience_taker.remove_things_in_brackets()
	# 	ingredience_taker.remove_after()
	# 	ingredience_taker.to_lower_case()
	# 	ingredience_taker.remove_non_letters()
	# 	ingredience_taker.split_ingredients()
	# 	ingredience_taker.remove_nonneeded_words()
	# 	ingredience_taker.remove_white_speces_around()
	# 	ingredience_taker.remove_duplicities()
	# 	ingredience_taker.remove_white_speces_around()
	# 	ingredience_taker.remove_long_ingredience()
	# 	ingredience_taker.connect_possible_connections()

	# 	statistics.add(ingredience_taker.ingredience)
		

	# statistics.calculate_statistic()

	# pprint.pprint(statistics.ingredinces_values)
	# print(len(statistics.ingredinces_values))

	# keys = list(statistics.ingredinces_values.keys())
	# values = list(statistics.ingredinces_values.values())
	# sorted_value_index = np.argsort(values)
	# sorted_dict = {keys[i]: values[i] for i in sorted_value_index}

	# print(sorted_dict)
	# print(len(sorted_dict))

	# stats = {}
	# for element in statistics.ingredinces_values:
	# 	splitted = element.split(" ")
	# 	for word in splitted:
	# 		if word in stats:
	# 			stats[word] += 1
	# 		else:
	# 			stats[word] = 1
	# keys = list(stats.keys())
	# values = list(stats.values())
	# sorted_value_index = np.argsort(values)
	# sorted_dict = {keys[i]: values[i] for i in sorted_value_index}

	# print(sorted_dict)
	# print(len(sorted_dict))