from project.vehicle import Vehicle
from unittest import TestCase,main

class TestVehicle(TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(100,150)

    def test_if_initiated_correctly(self):
        fuel = 100
        horse_power= 150
        test_vehicle = Vehicle(100,150)
        self.assertEqual(fuel,test_vehicle.fuel)
        self.assertEqual(fuel, test_vehicle.capacity)
        self.assertEqual(horse_power, test_vehicle.horse_power)
        self.assertEqual(1.25,test_vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_if_str_method_works_correctly(self):
        expected = f"The vehicle has {self.vehicle.horse_power} " \
               f"horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption"
        actual = str(self.vehicle)
        self.assertEqual(expected,actual)

    def test_if_drive_method_will_throw_exception_if_not_enough_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(self.vehicle.fuel)
        self.assertEqual("Not enough fuel",str(ex.exception))
    def test_if_drive_method_worsk_correctly_if_enough_fuel(self):
        distance = 10
        fuel_burned = distance*self.vehicle.DEFAULT_FUEL_CONSUMPTION
        expected = self.vehicle.fuel - fuel_burned
        self.vehicle.drive(distance)

        self.assertEqual(expected,self.vehicle.fuel)

    def test_if_refuel_method_will_throw_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1)
        self.assertEqual("Too much fuel",str(ex.exception))

    def test_if_refuel_method_works_correctly(self):
        self.vehicle.fuel = 80
        self.vehicle.refuel(20)
        self.assertEqual(100,self.vehicle.fuel)


if __name__ == "__main__":
    main()