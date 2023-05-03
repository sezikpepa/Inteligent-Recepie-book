from Recepie_Creator import Recepie_Creator

if __name__ == '__main__':
	recepie_creator = Recepie_Creator()

	recepie_creator.LoadFile("C:\\Users\\sezik\\OneDrive - Univerzita Karlova\\projekty\\Inteligent-Recepie-book\\archive\\" + "dataset_small.csv")

	print(recepie_creator)