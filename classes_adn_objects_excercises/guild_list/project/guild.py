from project.player import Player

class Guild:
    def __init__(self,name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player.guild == player.DEFAULT_GUILD:
            player.guild = self.name
            self.players.append(player)
            return f"Welcome player {player.name} to the guild {self.name}"
        elif player.guild != "Unaffiliated" and player.guild != self.name:
            return f"Player {player.name} is in another guild."
        return f"Player {player.name} is already in the guild."

    def kick_player(self,player_name: str):
        if any([x.name==player_name for x in self.players]):
            player_to_remove = [x for x in self.players if x.name == player_name][0]
            player_to_remove.guild = Player.DEFAULT_GUILD
            self.players.remove(player_to_remove)
            return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."
    def guild_info(self):
        result = f"Guild: {self.name}\n"
        for player in self.players:
            result += player.player_info()
        return  result