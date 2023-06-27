from typing import List

class Ingrediences:
	def __init__(self, elements: List[str]) -> None:
		if not isinstance(elements, list):
			raise ValueError(f"elements is {type(elements)}")
		
		if not all(isinstance(item, str) for item in elements):
			raise ValueError(f"not all parts of elements are strings")

		self.elements: List[str] = elements
			

	def __str__(self) -> str:
		toReturn = ""

		for element in self.elements:
			toReturn += element + "\n"

		return toReturn
	


if __name__ == '__main__':
	import unittest

	class TestIngredinces__str__(unittest.TestCase):

		def test_empty(self):
			ingrediences = Ingrediences([])

			self.assertEqual(str(ingrediences), "")

		def test_normal(self):
			ingrediences = Ingrediences(["one", "two", "three"])

			self.assertEqual(str(ingrediences), "one\ntwo\nthree\n")

	unittest.main()


