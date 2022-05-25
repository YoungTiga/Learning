from project.pokemon import  Pokemon


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())


class Trainer:
    def __init__(self,name):
        self.name = name
        self.pokemons = {}
    def add_pokemon(self, pokemon):
        if pokemon.pokemon_name not in self.pokemons:
            #pokemon.pokemon_name - името на покемона като стринг "Charizard" "Pikachu" и т.н.
            # self.pokemons.append(pokemon)
            self.pokemons[pokemon.pokemon_name] = pokemon
            return  f"Caught {pokemon.pokemon_name} with health {pokemon.pokemon_health}"
        else:
            return "This pokemon is already caught"

    def release_pokemon(self, pokemon):
        # for remove_pokemon in self.pokemons:
        #     if remove_pokemon.pokemon_name == pokemon:
        #         self.pokemons.remove(remove_pokemon)
        #         return f"You have released {pokemon}"
        if pokemon in self.pokemons:
            del self.pokemons[pokemon]
            return f"You have released {pokemon}"
        else:
            return "Pokemon is not caught"
    def trainer_data(self):
        result = ""
        result += f"Pokemon Trainer {self.name}\n"
        result += f"Pokemon count {len(self.pokemons)}\n"
        for got_pokemon_name, pokemon_class in self.pokemons.items():
            result += f"- {pokemon_class.pokemon_details()}\n"
        return  result

trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
