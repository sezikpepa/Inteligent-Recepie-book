import settings

class Delay_recepie_handler:
	def __init__(self):
		pass
    

	def load(self):
		pass

	def store(self, delayed_recepies: dict):
		if not isinstance(delayed_recepies, dict):
			raise ValueError(f"delayed_recepies is {type(delayed_recepies)}")
		


