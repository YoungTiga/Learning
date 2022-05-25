from project.player import Player

class Team:
    def __init__(self,name: str,rating: int):
        self.__name = name
        self.__rating = rating
        self.__players = []

    def add_player(self,player: Player):
        if any([x.name == player.name for x in self.__players]):
            return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"
    def remove_player(self,player_name: str):
        if not any([x.name == player_name for x in self.__players]):
            return f"Player {player_name} not found"
        player_to_remove = [x for x in self.__players if x.name == player_name][0]
        self.__players.remove(player_to_remove)
        return player_to_remove