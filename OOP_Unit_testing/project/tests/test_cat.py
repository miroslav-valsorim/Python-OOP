from unittest import TestCase, main
from project.cat import Cat


class TestCat(TestCase):

    def setUp(self):
        self.cat = Cat("Spas")

    def test_initialization_of_cat(self):
        self.assertEqual("Spas", self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_if_cat_eats_and_its_fed(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_if_cat_eats_and_its_sleepy(self):
        self.cat.eat()
        self.assertTrue(self.cat.sleepy)

    def test_if_cat_eats_and_grows_size_plus_one(self):
        self.cat.eat()
        self.assertEqual(1, self.cat.size)

    def test_raise_exception_if_cat_already_fed(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual(str(ex.exception), 'Already fed.')

    def test_if_cat_goes_to_sleep_and_sets_value_to_false(self):
        self.cat.fed = True
        self.cat.sleepy = True
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)

    def test_raise_exception_if_cat_has_to_sleep_and_not_fed(self):

        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        self.assertEqual(str(ex.exception), 'Cannot sleep while hungry')


if __name__ == "__main__":
    main()