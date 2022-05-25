from project.driver import Driver
from project.race import Race
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar


class Controller:

    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type == "MuscleCar" or car_type == "SportsCar":
            if any([x.model == model for x in self.cars]):
                raise Exception(f"Car {model} is already created!")
            if car_type == "SportsCar":
                car = SportsCar(model, speed_limit)
                self.cars.append(car)
            elif car_type == "MuscleCar":
                car = MuscleCar(model, speed_limit)
                self.cars.append(car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        if any([x.name == driver_name for x in self.drivers]):
            raise Exception(f"Driver {driver_name} is already created!")
        driver = Driver(driver_name)
        self.drivers.append(driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if any([x.name==race_name for x in self.races]):
            raise Exception(f"Race {race_name} is already created!")
        race = Race(race_name)
        self.races.append(race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        if not any([x.name == driver_name for x in self.drivers]):
            raise Exception(f"Driver {driver_name} could not be found!")

        if car_type in ["MuscleCar", "SportsCar"]:
            if not any([x.__class__.__name__ == car_type and not x.is_taken for x in self.cars[::-1]]):
                raise Exception(f"Car {car_type} could not be found!")

        driver = [x for x in self.drivers if x.name == driver_name][0]
        car = [x for x in self.cars if x.__class__.__name__ == car_type and not x.is_taken][-1]
        # if car.is_taken:
        #     raise Exception(f"Car {car_type} could not be found!")
        if driver.car is None:
            driver.car = car
            car.is_taken = True
            return f"Driver {driver_name} chose the car {car.model}."
        else:
            old_model = driver.car
            old_model.is_taken = False
            driver.car = car
            car.is_taken = True
            return f"Driver {driver_name} changed his car from {old_model.model} to {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        if not any([x.name == race_name for x in self.races]):
            raise Exception(f"Race {race_name} could not be found!")
        if not any([x.name == driver_name for x in self.drivers]):
            raise Exception(f"Driver {driver_name} could not be found!")
        driver = [x for x in self.drivers if x.name == driver_name][0]
        race = [x for x in self.races if x.name == race_name][0]
        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")
        if any([x.name == driver.name for x in race.drivers]):
            return f"Driver {driver_name} is already added in {race_name} race."
        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        if not any([x.name == race_name for x in self.races]):
            raise Exception(f"Race {race_name} could not be found!")
        race = [x for x in self.races if x.name == race_name][0]
        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")
        fastest = sorted(race.drivers, key=lambda x: -x.car.speed_limit)
        res = ""
        for i in range(3):
            fastest[i].number_of_wins += 1
            res += f"Driver {fastest[i].name} wins the {race_name} race with a speed of {fastest[i].car.speed_limit}.\n"
        return res.strip()
