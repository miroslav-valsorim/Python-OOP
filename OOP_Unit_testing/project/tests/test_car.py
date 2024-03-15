from unittest import TestCase, main
from project.car_manager import Car


class TestCar(TestCase):

    def setUp(self):
        self.alfa_romeo = Car("Alfa", "Mito", 10, 40)

    def test_initializing(self):
        self.assertEqual("Alfa", self.alfa_romeo.make)
        self.assertEqual("Mito", self.alfa_romeo.model)
        self.assertEqual(10, self.alfa_romeo.fuel_consumption)
        self.assertEqual(40, self.alfa_romeo.fuel_capacity)
        self.assertEqual(0, self.alfa_romeo.fuel_amount)

    def test_no_make_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.alfa_romeo.make = ""

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_no_model_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.alfa_romeo.model = ""

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_zero_fuel_consumption_expect_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.alfa_romeo.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_zero_fuel_capacity_expect_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.alfa_romeo.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_negative_fuel_amount(self):
        with self.assertRaises(Exception) as ex:
            self.alfa_romeo.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_if_fuel_is_zero_or_less(self):
        with self.assertRaises(Exception) as ex:
            self.alfa_romeo.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_if_fuel_more_than_capacity(self):
        result = self.alfa_romeo.refuel(40)
        self.assertEqual(40, self.alfa_romeo._Car__fuel_capacity)

    def test_refuel_successfuly(self):
        self.alfa_romeo.refuel(5)
        self.assertEqual(5, self.alfa_romeo._Car__fuel_amount)

    def test_drive_raise_exception(self):
        self.alfa_romeo.fuel_amount = 20

        with self.assertRaises(Exception) as ex:
            self.alfa_romeo.drive(1000)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_valid_distance(self):
        self.alfa_romeo.fuel_amount = 40
        self.alfa_romeo.drive(55)

        self.assertEqual(self.alfa_romeo.fuel_amount, 34.5)


if __name__ == "__main__":
    main()