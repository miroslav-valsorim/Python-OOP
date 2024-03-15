from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self):
        self.mammal_animal = Mammal("Gosho", "cat", "meow")

    def test_initialization(self):
        self.assertEqual("Gosho", self.mammal_animal.name)
        self.assertEqual("cat", self.mammal_animal.type)
        self.assertEqual("meow", self.mammal_animal.sound)
        self.assertEqual("animals", self.mammal_animal._Mammal__kingdom)

    def test_make_sound(self):
        result = self.mammal_animal.make_sound()
        self.assertEqual(result, f"Gosho makes meow")

    def test_get_kingdom(self):
        result = self.mammal_animal.get_kingdom()
        self.assertEqual(result, self.mammal_animal._Mammal__kingdom)

    def test_info(self):
        result = self.mammal_animal.info()
        self.assertEqual(result, f"Gosho is of type cat")


if __name__ == "__main__":
    main()