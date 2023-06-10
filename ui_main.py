# import system module
import sys
 
# import PySide2 modules
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QRadioButton
from PySide6.QtGui import QPalette, QColor, QPixmap

from Recepie_Creator import Recepie_Creator
from IngredienceTaker import IngredienceTaker
from StatisticsCreator import StatisticsCreator
from MakingProcessMaker import MakingProcessMaker
from Reccomender import Recommender
import pprint
import numpy as np
from Ingredience import Ingrediences
from favourite_ingredience import Favourite_ingredience

from random import randint
from copy import deepcopy
from PySide6.QtCore import Qt

import settings


class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class UI_Recepie():
	def __init__(self):
		self.name_widget = None
		self.ingredience_widget = None
		self.instructions_widget = None
		self.image = None

	def set_new_recepie(self, recepie):
		pass


class Main_window(QMainWindow):
	def __init__(self):
		super().__init__()

		self.ui_recepie = UI_Recepie()
		self.recepie_creator = Recepie_Creator()

		self.recommender = None

		self.original_recepies = []

		#self.recepie_creator.LoadFile("C:\\Users\\sezik\\OneDrive - Univerzita Karlova\\projekty\\Inteligent-Recepie-book\\archive\\" + "dataset_small.csv")
		self.recepie_creator.LoadFile(settings.dataset)

		self.ingredients_values = Favourite_ingredience() #tady to bude problém

		self.current_recepie_number = None

		self.original_recepies = deepcopy(self.recepie_creator.recepies)

		repeat = len(self.recepie_creator.recepies)
		for i in range(repeat):
			process_maker = MakingProcessMaker(self.recepie_creator.recepies[i].instructions.split(" "))
			ingredience_taker = IngredienceTaker(self.recepie_creator.recepies[i].ingredience)

			ingredience_taker.do_magic()
			process_maker.do_magic()

			self.recepie_creator.recepies[i].instructions = process_maker.processes
			self.recepie_creator.recepies[i].ingredience = ingredience_taker.ingredience

		self.recommender = Recommender(self.recepie_creator.recepies)

	def on_get_random_recepie_button(self):
		recepie_number = randint(0, len(self.original_recepies) - 1)
		self.show_recepie(self.original_recepies[recepie_number])	
		self.current_recepie_number = recepie_number	

		self.enable_stars_buttons()

	def on_get_recommended_recepie_button(self):
		print("yes")
		score, recepie, no_data = self.recommender.get_recommendation(self.ingredients_values, 4)
		print(recepie)
		self.show_recepie(self.original_recepies[recepie])	
		self.current_recepie_number = recepie	

		self.enable_stars_buttons()

	def enable_stars_buttons(self):
		self.stars_bad.setEnabled(True)
		self.stars_neutral.setEnabled(True)
		self.stars_good.setEnabled(True)

	def disable_stars_buttons(self):
		self.stars_bad.setEnabled(False)
		self.stars_neutral.setEnabled(False)
		self.stars_good.setEnabled(False)

	def insert_ratings(self, ingredients, rating):
		for element in ingredients:
			self.ingredients_values.add_rating(element, rating)

	def show_recepie(self, recepie):
		self.ui_recepie.name_widget.setText(recepie.name)
		self.ui_recepie.ingredience_widget.setText(str(Ingrediences(recepie.ingredience)))
		self.ui_recepie.instructions_widget.setText(str(recepie.instructions))


		image = QPixmap(f"{settings.images_path}{recepie.image_name}")

		self.ui_recepie.image.setText(recepie.image_name)
		self.ui_recepie.image.setPixmap(image)

	def show_ingredience_values(self):
		result = self.ingredients_values.get_favouritness()
		keys = list(result.keys())
		values = list(result.values())
		sorted_value_index = np.argsort(values)[::-1][:15]
		sorted_dict = {keys[i]: values[i] for i in sorted_value_index}

		textToShow = ""
		for element in sorted_dict:
			textToShow += element + ": " + str(sorted_dict[element]) + "\n"

		self.top_ingrediences.setText(textToShow)

	def rating_inserted(self):
		value = self.sender()

		self.setWindowTitle(value.text())
		text = value.text()

		rating = None
		if text == "good":
			rating = 1
		elif text == "neutral":
			rating = 0.5
		elif text == "bad":
			rating = 0

		self.stars_bad.setEnabled(False)
		self.stars_neutral.setEnabled(False)
		self.stars_good.setEnabled(False)

		self.insert_ratings(self.recepie_creator.recepies[self.current_recepie_number].ingredience, rating)
		self.show_ingredience_values()


	def basic_setup(self):
		self.setWindowTitle("Inteligent recepie book")
		self.setFixedSize(900, 600)

	def layout_setup(self):		
		self.ui_recepie.name_widget = QLabel()
		self.ui_recepie.name_widget.setAlignment(Qt.AlignCenter)
		self.ui_recepie.name_widget.setText("zatím nic")

		self.ui_recepie.ingredience_widget = QLabel()
		self.ui_recepie.ingredience_widget.setText("v budoucnu")

		name_ingredients_layout = QVBoxLayout()
		name_ingredients_layout.addWidget(self.ui_recepie.name_widget)
		name_ingredients_layout.addWidget(self.ui_recepie.ingredience_widget)


		text = QWidget()
		text.setLayout(name_ingredients_layout)

		self.ui_recepie.image = QLabel()
		self.ui_recepie.image.setText("tady bude obrázek")
		
		topside_layout = QHBoxLayout()
		topside_layout.addWidget(text)
		topside_layout.addWidget(self.ui_recepie.image)
		

		topside = QWidget()
		topside.setLayout(topside_layout)

		self.ui_recepie.instructions_widget = QLabel()
		self.ui_recepie.instructions_widget.setFixedWidth(1200)
		self.ui_recepie.instructions_widget.setWordWrap(True)
		self.ui_recepie.instructions_widget.setText("uvidime")


		get_recommendation_button = QPushButton()
		get_recommendation_button.setText("Get recommendation")
		get_recommendation_button.clicked.connect(self.on_get_recommended_recepie_button)

		self.get_random_button = QPushButton()
		self.get_random_button.setText("Get random recepie")
		self.get_random_button.clicked.connect(self.on_get_random_recepie_button)

		self.top_ingrediences = QLabel()
		self.top_ingrediences.setText("tady budou top ingredience")

		self.stars_good = QPushButton("good", self)
		self.stars_good.clicked.connect(self.rating_inserted)

		self.stars_neutral = QPushButton("neutral", self)
		self.stars_neutral.clicked.connect(self.rating_inserted)

		self.stars_bad = QPushButton("bad", self)
		self.stars_bad.clicked.connect(self.rating_inserted)

		self.disable_stars_buttons()



		buttons_layout = QHBoxLayout()
		buttons_layout.addWidget(get_recommendation_button)
		buttons_layout.addWidget(self.get_random_button)

		buttons_layout.addWidget(self.stars_good)
		buttons_layout.addWidget(self.stars_neutral)
		buttons_layout.addWidget(self.stars_bad)


		buttons = QWidget()
		buttons.setLayout(buttons_layout)

		central_layout = QVBoxLayout()
		central_layout.addWidget(topside)
		central_layout.addWidget(self.ui_recepie.instructions_widget)
		central_layout.addWidget(buttons)
		central_layout.addWidget(self.top_ingrediences)

		central_widget = QWidget()
		central_widget.setLayout(central_layout)
		self.setCentralWidget(central_widget)


# create new app
app = QApplication(sys.argv)
 
# create main window
mainwindow = Main_window()
mainwindow.basic_setup()
mainwindow.layout_setup()

mainwindow.show_ingredience_values()






# invoke show function
mainwindow.show()
 
# to kee in loop invoke exec_() function
app.exec_()