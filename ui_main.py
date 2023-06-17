# import system module
import sys
 
# import PySide2 modules
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QComboBox
from PySide6.QtGui import QPalette, QColor, QPixmap, QFont, QIcon


from Reccomender import Recommender
import numpy as np
from Ingredience import Ingrediences
from favourite_ingredience import Favourite_ingrediences

from random import randint
from copy import deepcopy
from PySide6.QtCore import Qt

from recepie import Recepie
from recepies_loader_from_json import Recepies_loader_from_json

import datetime

import settings

from recepie_type_decider import Recepie_type_decider
from recepie_type_profile import Recepie_type_profile




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

		self.ingredients_values = Favourite_ingrediences()

		self.current_recepie_number = None

		recepies_loader = Recepies_loader_from_json()
		self.recepies = recepies_loader.get_recepies()

		self.recommender = Recommender(self.recepies)
		self.ingredients_values.load_from_file(settings.favourite_ingrediences_file_name)

		self.delayed_recepies = {}

		self.recepie_type_decider = Recepie_type_decider()

	def enable_recepie_types_ui_elements(self):
		self.send_recepie_type_box.setEnabled(True)
		self.send_recepie_type_button.setEnabled(True)
		
	def disable_recepie_types_ui_elements(self):
		self.send_recepie_type_box.setEnabled(False)
		self.send_recepie_type_button.setEnabled(False)

	def on_get_random_recepie_button(self):
		while True:
			recepie_number = randint(0, len(self.recepies) - 1)
			if recepie_number not in self.delayed_recepies.keys():
				break
		self.show_recepie(self.recepies[recepie_number])	
		self.current_recepie_number = recepie_number	

		self.delayed_recepies[recepie_number] = datetime.datetime.now()

		self.enable_stars_buttons()
		self.enable_recepie_types_ui_elements()

	def on_get_recommended_recepie_button(self):
		score, recepie_number, no_data = self.recommender.get_recommendation(self.ingredients_values, 4, self.delayed_recepies, self.select_recepie_type_box.currentText())
		self.show_recepie(self.recepies[recepie_number])	
		self.current_recepie_number = recepie_number	

		self.delayed_recepies[recepie_number] = datetime.datetime.now()

		self.enable_stars_buttons()
		self.enable_recepie_types_ui_elements()

	def enable_stars_buttons(self):
		self.stars_bad.setEnabled(True)
		self.stars_neutral.setEnabled(True)
		self.stars_good.setEnabled(True)

	def disable_stars_buttons(self):
		self.stars_bad.setEnabled(False)
		self.stars_neutral.setEnabled(False)
		self.stars_good.setEnabled(False)

	def insert_ratings(self, ingredients, rating):
		if not isinstance(rating, int) and not isinstance(rating, float):
			raise ValueError(f"rating is {type(rating)}")

		for element in ingredients:
			self.ingredients_values.add_rating(element, rating)

	def show_recepie(self, recepie):
		if not isinstance(recepie, Recepie):
			raise ValueError(f"recepie is {type(recepie)}")

		self.ui_recepie.name_widget.setText(recepie.name)
		self.ui_recepie.ingredience_widget.setText(str(Ingrediences(recepie.ingredience_full)))
		self.ui_recepie.instructions_widget.setText(str(recepie.instructions_full))

		image = QPixmap(f"{settings.images_path}{recepie.image_name}")
		image.width = 200
		image.height = 200

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

		self.setWindowTitle(settings.program_name)
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

		self.insert_ratings(self.recepies[self.current_recepie_number].ingredience, rating)
		self.show_ingredience_values()

		self.ingredients_values.save_to_file(settings.favourite_ingrediences_file_name)

	def on_send_recepie_type_button(self):
		self.send_recepie_type_button.setDisabled(True)
		self.send_recepie_type_box.setDisabled(True)

		self.recepie_type_decider.types[self.send_recepie_type_box.currentText()].add_elements(self.recepies[self.current_recepie_number].instructions)

		print("elements added")


	def basic_setup(self):
		self.setWindowTitle("Inteligent recepie book")
		self.setFixedSize(1500, 800)
		self.setWindowIcon(QIcon(settings.icon_path))

	def layout_setup(self):		
		self.ui_recepie.name_widget = QLabel()
		self.ui_recepie.name_widget.setAlignment(Qt.AlignCenter)
		self.ui_recepie.name_widget.setText("zatím nic")
		self.ui_recepie.name_widget.setFont(QFont('Arial', 20))
		self.ui_recepie.name_widget.setWordWrap(True)

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

		self.select_recepie_type_box = QComboBox()
		self.select_recepie_type_box.addItems(["salty", "sweet", "green", "drink"])

		self.send_recepie_type_box = QComboBox()
		self.send_recepie_type_box.addItems(["salty", "sweet", "green", "drink"])

		self.recepie_type_decider.add_new_type(Recepie_type_profile("salty"))
		self.recepie_type_decider.add_new_type(Recepie_type_profile("sweet"))
		self.recepie_type_decider.add_new_type(Recepie_type_profile("green"))
		self.recepie_type_decider.add_new_type(Recepie_type_profile("drink"))

		for key in self.recepie_type_decider.types.keys():
			self.recepie_type_decider.types[key].load_from_file()

		self.recepie_type_decider.types

		self.send_recepie_type_button = QPushButton()
		self.send_recepie_type_button.setText("Send feedback")
		self.send_recepie_type_button.clicked.connect(self.on_send_recepie_type_button)



		get_recommendation_button = QPushButton()
		get_recommendation_button.setText("Get recommendation")
		get_recommendation_button.clicked.connect(self.on_get_recommended_recepie_button)

		self.get_random_button = QPushButton()
		self.get_random_button.setText("Get random recepie")
		self.get_random_button.clicked.connect(self.on_get_random_recepie_button)

		self.top_ingrediences = QLabel()
		self.top_ingrediences.setText("tady budou top ingredience")

		self.stars_good = QPushButton("good", self)
		self.stars_good.setStyleSheet("background-color: green")
		self.stars_good.clicked.connect(self.rating_inserted)

		self.stars_neutral = QPushButton("neutral", self)
		self.stars_neutral.setStyleSheet("background-color: orange")
		self.stars_neutral.clicked.connect(self.rating_inserted)

		self.stars_bad = QPushButton("bad", self)
		self.stars_bad.setStyleSheet("background-color: red")
		self.stars_bad.clicked.connect(self.rating_inserted)

		self.disable_stars_buttons()
		self.disable_recepie_types_ui_elements()


		self.recommender.set_recepie_type_decider(self.recepie_type_decider)



		buttons_layout = QHBoxLayout()
		buttons_layout.addWidget(self.send_recepie_type_box)
		buttons_layout.addWidget(self.send_recepie_type_button)
		buttons_layout.addWidget(self.select_recepie_type_box)
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