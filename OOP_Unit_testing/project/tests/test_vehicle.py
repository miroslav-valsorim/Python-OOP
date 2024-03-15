from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self):
        self.car = Vehicle(40, 170)

    def test_default_fuel_consumption(self):
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_initialization(self):
        self.assertEqual(40, self.car.fuel)
        self.assertEqual(170, self.car.horse_power)
        self.assertEqual(self.car.fuel, self.car.capacity)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, self.car.fuel_consumption)

    def test_drive_if_no_fuel_raise_exception(self):
        self.car.fuel = 0
        with self.assertRaises(Exception) as ex:
            self.car.drive(55)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_successfully(self):
        self.car.drive(2)
        self.assertEqual(self.car.fuel, 37.5)

    def test_refuel_throw_exception(self):
        self.car.capacity = 10
        with self.assertRaises(Exception) as ex:
            self.car.refuel(11)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_with_no_problems(self):
        self.car.capacity = 10
        self.car.fuel = 2

        self.car.refuel(2)
        self.assertEqual(4, self.car.fuel)

    def test_correct__str__(self):
        result = str(self.car)
        expected = f"The vehicle has 170 " \
                   f"horse power with 40 fuel left and 1.25 fuel consumption"
        self.assertEqual(result, expected)


if __name__ == "__main__":
    main()