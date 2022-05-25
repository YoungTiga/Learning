from  project.decoration.decoration_repository import DecorationRepository
from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish

class Controller:

    def __init__(self):
        self.decorations_repository=  DecorationRepository()
        self.aquariums = []

    def add_aquarium(self,aquarium_type: str, aquarium_name: str):
        if aquarium_type not in ["FreshwaterAquarium","SaltwaterAquarium"]:
            return "Invalid aquarium type."
        aquarium = None
        if aquarium_type == "FreshwaterAquarium":
            aquarium = FreshwaterAquarium(aquarium_name)
        elif aquarium_type == "SaltwaterAquarium":
            aquarium = SaltwaterAquarium(aquarium_name)
        self.aquariums.append(aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self,decoration_type: str):
        if decoration_type not in ["Ornament","Plant"]:
            return  "Invalid decoration type."
        decoration = None
        if decoration_type == "Ornament":
            decoration =Ornament()
        elif decoration_type == "Plant":
            decoration = Plant()
        self.decorations_repository.add(decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self,aquarium_name: str, decoration_type: str):
        decoration = self.decorations_repository.find_by_type(decoration_type)
        if decoration == "None":
            return f"There isn't a decoration of type {decoration_type}."

        self.decorations_repository.remove(decoration)
        aquarium = [x for x in self.aquariums if x.name == aquarium_name][0]
        aquarium.add_decoration(decoration)

        return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self,aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type not in ["FreshwaterFish","SaltwaterFish"]:
            return f"There isn't a fish of type {fish_type}."
        fish= None
        if fish_type == "FreshwaterFish":
            fish = FreshwaterFish(fish_name,fish_species,price)
        elif fish_type == "SaltwaterFish":
            fish = SaltwaterFish(fish_name,fish_species,price)

        aquarium = [x for x in self.aquariums if x.name == aquarium_name][0]

        if fish_type == "FreshwaterFish" and aquarium.__class__.__name__ == "SaltwaterAquarium" \
            or fish_type == "SaltwaterFish" and aquarium.__class__.__name__ == "FreshwaterAquarium":
            return "Water not suitable."

        return aquarium.add_fish(fish)

    def feed_fish(self,aquarium_name: str):
        aquarium = [x for x in self.aquariums if x.name == aquarium_name][0]

        # for fish in aquarium.fish:
        #     fish.eat()
        aquarium.feed()

        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self,aquarium_name: str):
        aquarium = [x for x in self.aquariums if x.name == aquarium_name][0]
        res = sum(x.price for x in aquarium.decorations) + sum(x.price for x in aquarium.fish)

        return f"The value of Aquarium {aquarium_name} is {res:.2f}."

    def report(self):
        res = ""
        for aquarium in self.aquariums:
            res += str(aquarium) + "\n"
        return  res.strip()