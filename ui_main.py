# import system module
import sys
 
# import PySide2 modules
from PySide2.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton
from PySide2.QtGui import QPalette, QColor

from Recepie_Creator import Recepie_Creator
from IngredienceTaker import IngredienceTaker
from StatisticsCreator import StatisticsCreator
from MakingProcessMaker import MakingProcessMaker
from Reccomender import Recommender
import pprint
import numpy as np


class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)



class Main_window(QMainWindow):
	def __init__(self):
		super().__init__()

		recepie_creator = Recepie_Creator()

		recepie_creator.LoadFile("C:\\Users\\sezik\\OneDrive - Univerzita Karlova\\projekty\\Inteligent-Recepie-book\\archive\\" + "dataset_small.csv")

		repeat = 1000
		for i in range(repeat):
			process_maker = MakingProcessMaker(recepie_creator.recepies[i].instructions.split(" "))
			ingredience_taker = IngredienceTaker(recepie_creator.recepies[i].ingredience)

			ingredience_taker.remove_things_in_brackets()
			ingredience_taker.remove_after()
			ingredience_taker.to_lower_case()
			ingredience_taker.remove_non_letters()
			ingredience_taker.split_ingredients()
			ingredience_taker.remove_nonneeded_words()
			ingredience_taker.remove_white_speces_around()
			ingredience_taker.remove_duplicities()
			ingredience_taker.remove_white_speces_around()
			ingredience_taker.remove_long_ingredience()
			ingredience_taker.connect_possible_connections()

			process_maker.remove_nonletters()
			process_maker.remove_words_without_meaning()

			recepie_creator.recepies[i].instructions = process_maker.processes
			recepie_creator.recepies[i].ingredience = ingredience_taker.ingredience

	def on_get_random_recepie_button(self):
		self.setWindowTitle("done")

	def basic_setup(self):
		self.setWindowTitle("Inteligent recepie book")
		self.resize(1500, 1000)

	def layout_setup(self):		
		name = Color('yellow')
		ingredients = Color('pink')
		name_ingredients_layout = QVBoxLayout()
		name_ingredients_layout.addWidget(name)
		name_ingredients_layout.addWidget(ingredients)


		text = QWidget()
		text.setLayout(name_ingredients_layout)
		picture = Color('red')
		
		topside_layout = QHBoxLayout()
		topside_layout.addWidget(text)
		topside_layout.addWidget(picture)
		

		topside = QWidget()
		topside.setLayout(topside_layout)
		instructions = Color('green')


		get_recommendation_button = QPushButton()
		get_recommendation_button.setText("Get recommendation")

		get_random_button = QPushButton()
		get_random_button.setText("Get random recepie")
		get_random_button.clicked.connect(self.on_get_random_recepie_button)

		buttons_layout = QHBoxLayout()
		buttons_layout.addWidget(get_recommendation_button)
		buttons_layout.addWidget(get_random_button)

		buttons = QWidget()
		buttons.setLayout(buttons_layout)

		central_layout = QVBoxLayout()
		central_layout.addWidget(topside)
		central_layout.addWidget(instructions)
		central_layout.addWidget(buttons)

		central_widget = QWidget()
		central_widget.setLayout(central_layout)
		self.setCentralWidget(central_widget)


# create new app
app = QApplication(sys.argv)
 
# create main window
mainwindow = Main_window()
mainwindow.basic_setup()
mainwindow.layout_setup()






# invoke show function
mainwindow.show()
 
# to kee in loop invoke exec_() function
app.exec_()