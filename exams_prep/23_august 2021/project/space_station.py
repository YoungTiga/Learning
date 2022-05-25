from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.astronaut.astronaut_repository import AstronautRepository
from project.planet.planet_repository import Planet
from project.planet.planet_repository import PlanetRepository
class SpaceStation:
    successful_missions = 0
    failed_missions = 0
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()


    def add_astronaut(self,astronaut_type: str, name: str):
        if astronaut_type not in ["Biologist", "Geodesist", "Meteorologist"]:
            raise Exception("Astronaut type is not valid!")
        for astronaut in self.astronaut_repository.astronauts:
            if astronaut.name == name:
                return f"{name} is already added."
        if astronaut_type == "Biologist":
            astronaut = Biologist(name)
            self.astronaut_repository.add(astronaut)
        elif astronaut_type == "Geodesist":
            astronaut = Geodesist(name)
            self.astronaut_repository.add(astronaut)
        elif astronaut_type == "Meteorologist":
            astronaut = Meteorologist(name)
            self.astronaut_repository.add(astronaut)
        return f"Successfully added {astronaut_type}: {name}."
        # pass
    def add_planet(self,name: str, items: str):
        for planet in self.planet_repository.planets:
            if planet.name == name:
                return f"{name} is already added."
        planet = Planet(name)
        planet.items = items.split(", ")
        self.planet_repository.add(planet)
        return f"Successfully added Planet: {name}."


    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)
        if astronaut == None:
            raise Exception(f"Astronaut {name} doesn't exist!")
        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)
        if not planet:
            raise Exception("Invalid planet name!")
        filtered = [x for x in self.astronaut_repository.astronauts if x.oxygen > 30]
        if len(filtered) == 0:
            raise Exception("You need at least one astronaut to explore the planet!")
        suitable_astronauts = sorted(filtered, key=lambda x: x.oxygen, reverse=True)[:5]
        participated = 0
        for astronaut in suitable_astronauts:
            if not planet.items:
                break
            participated += 1
            while planet.items and astronaut.oxygen>0:
                astronaut.breathe()
                astronaut.backpack.append(planet.items.pop())


        if not planet.items:
            self.successful_missions += 1
            return f"Planet: {planet_name} was explored. {participated} astronauts participated in collecting items."
        self.failed_missions += 1
        return "Mission is not completed."
        # pass

    def report(self):
        res = f"{self.successful_missions} successful missions!\n"
        res += f"{self.failed_missions} missions were not completed!\n"
        res += "Astronauts' info:\n"
        for astronaut in self.astronaut_repository.astronauts:
            res += f"Name: {astronaut.name}\n"
            res += f"Oxygen: {astronaut.oxygen}\n"
            if not astronaut.backpack:
                res += f'Backpack items: none\n'
            else:
                res += f"Backpack items: {', '.join(astronaut.backpack)}\n"
        return res.strip()

    # def __find_suitable_astronauts(self, count, min_oxygen):
    #     astronauts = sorted([x for x in self.astronaut_repository.astronauts
    #                          if x.oxygen > min_oxygen],
    #                         key=lambda x: x.oxygen, reverse=True)[0: count]
    #
    #     return astronauts
