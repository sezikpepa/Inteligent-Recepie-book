from Recepie_Creator import Recepie_Creator
from IngredienceTaker import IngredienceTaker
from StatisticsCreator import StatisticsCreator
import pprint
import numpy as np

if __name__ == '__main__':
	recepie_creator = Recepie_Creator()

	recepie_creator.LoadFile("C:\\Users\\sezik\\OneDrive - Univerzita Karlova\\projekty\\Inteligent-Recepie-book\\archive\\" + "dataset_small.csv")

	statistics = StatisticsCreator()
	for i in range(10000):
		ingredience_taker = IngredienceTaker(recepie_creator.recepies[i].ingredience)
		ingredience_taker.remove_things_in_brackets()
		ingredience_taker.remove_after()
		ingredience_taker.to_lower_case()
		ingredience_taker.remove_non_letters()
		ingredience_taker.remove_nonneeded_words()
		ingredience_taker.remove_white_speces_around()
		ingredience_taker.remove_duplicities()
		ingredience_taker.remove_white_speces_around()
		ingredience_taker.remove_long_ingredience()

		statistics.add(ingredience_taker.ingredience)
		

	statistics.calculate_statistic()

	#pprint.pprint(statistics.ingredinces_values)
	keys = list(statistics.ingredinces_values.keys())
	values = list(statistics.ingredinces_values.values())
	sorted_value_index = np.argsort(values)
	sorted_dict = {keys[i]: values[i] for i in sorted_value_index}

	print(sorted_dict)