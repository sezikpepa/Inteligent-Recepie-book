from Recepie_Creator import Recepie_Creator
from IngredienceTaker import IngredienceTaker

if __name__ == '__main__':
	recepie_creator = Recepie_Creator()

	recepie_creator.LoadFile("C:\\Users\\sezik\\OneDrive - Univerzita Karlova\\projekty\\Inteligent-Recepie-book\\archive\\" + "dataset_small.csv")

	for i in range(13000):
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
		print(ingredience_taker)
	

	print(ingredience_taker)