from project.player import Player
from project.supply.supply import Supply


class Controller:

    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self,*args:Player):
        added_players = []
        for player in args:
            if player not in self.players:
                added_players.append(player)
                self.players.append(player)
        return f"Successfully added: {', '.join(x.name for x in added_players)}"


    def add_supply(self,*args:Supply):
        # for supply in args:
        #     self.supplies.append(supply)
        self.supplies.extend(list(args))

    def sustain(self,player_name: str, sustenance_type: str):
        if sustenance_type in "FoodDrink":
            player = [x for x in self.players if x.name == player_name]
            supplies = [x for x in self.supplies if x.__class__.__name__ == sustenance_type]
            if player:
                if sustenance_type == "Food" and not supplies:
                    raise Exception("There are no food supplies left!")
                elif sustenance_type == "Drink" and not supplies:
                    raise Exception("There are no drink supplies left!")
                current_supply = supplies[-1]
                curr_player = player[0]

                if not curr_player.need_sustenance:
                    return f"{player_name} have enough stamina."
                if curr_player.stamina + current_supply.energy > 100:
                    curr_player.stamina = 100
                else:
                    curr_player.stamina += current_supply.energy

                index = []
                for i,value in enumerate(self.supplies):
                    if value == current_supply:
                        index.append(i)
                self.supplies.pop(max(index))
                return f"{player_name} sustained successfully with {current_supply.name}."

    def duel(self,first_player_name: str, second_player_name: str):
        first_player= [x for x in self.players if x.name == first_player_name][0]
        second_player = [x for x in self.players if x.name == second_player_name][0]
        winner = None

        players  = [first_player,second_player]

        zero_stamina = ""
        for player in players:
            if player.stamina==0:
                zero_stamina += f"Player {player.name} does not have enough stamina.\n"
        if zero_stamina:
            return zero_stamina.strip()

        players_attacking = sorted(players, key= lambda x: x.stamina)

        for player in players_attacking:
            second_player_attacking = [x for x in players_attacking if x != player][0]

            if second_player_attacking.stamina - player.stamina/2 < 0:
                second_player_attacking.stamina = 0
                winner = player
                break
            else:
                second_player_attacking.stamina -= player.stamina / 2

        winner = sorted(players_attacking, key = lambda x: -x.stamina)[0]

        return  f"Winner: {winner.name}"

    def next_day(self):
        for player in self.players:

            if player.stamina - player.age*2 < 0:
                player.stamina =0
            else:
                player.stamina -= player.age*2
            self.sustain(player.name,"Food")
            self.sustain(player.name,"Drink")

    def __str__(self):
        res = ""
        for player in self.players:
            res += player.__str__()+"\n"
        for supply in self.supplies:
            res += supply.details()+"\n"
        return res.strip()
