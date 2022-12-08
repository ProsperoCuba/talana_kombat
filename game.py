from player import Player, PlayerBuilder


class Game:

    def __init__(self, sequences):
        self.player1 = PlayerBuilder.build_player(PlayerBuilder.PLAYER_1, sequences.get("player1"), "Tonyn Stallone")
        self.player2 = PlayerBuilder.build_player(PlayerBuilder.PLAYER_2, sequences.get("player2"), "Arnaldor Shuatseneguer")

    def get_start(self):
        """
        Method to start which player starts
        :return: <Player>
        """
        if self.player1.get_total_movements() > self.player2.get_total_movements():
            return self.player2
        elif self.player1.get_total_movements() < self.player2.get_total_movements():
            return self.player1
        else:
            if self.player1.get_cant_movements() > self.player2.get_cant_movements():
                return self.player2
            elif self.player1.get_cant_movements() < self.player2.get_cant_movements():
                return self.player1
            else:
                if self.player1.get_cant_hits() > self.player2.get_cant_hits():
                    return self.player2
                elif self.player1.get_cant_hits() < self.player2.get_cant_hits():
                    return self.player1
        
        return self.player1

    def get_player1(self):
        """Method to return Player 2"""
        return self.player1

    def get_player2(self):
        """Method to return Player 2"""
        return self.player2

    def get_winner(self):
        """Method that determines which player wins"""

        if self.player1.get_energy() <= 0:
            return self.player2
        elif self.player2.get_energy() <= 0:
            return self.player1

        return None

    def movs(self, first_to_play):
        """
        Method to build the total moves of the two players
        :param first_to_play: Player
        :return: []
        """
        total_movs = []

        if first_to_play.type == 1:
            first_movs = {"player": self.get_player1().get_name(), "movs": self.get_player1().get_player_combinations(), "player_type": 1}
            second_movs = {"player": self.get_player2().get_name(), "movs": self.get_player2().get_player_combinations(), "player_type": 2}
        else:
            first_movs = {"player": self.get_player2().get_name(), "movs": self.get_player2().get_player_combinations(), "player_type": 2}
            second_movs = {"player": self.get_player1().get_name(), "movs": self.get_player1().get_player_combinations(), "player_type": 1}

        len_player1 = self.get_player1().get_player_combinations()
        len_player2 = self.get_player2().get_player_combinations()
        max_len_player = len_player1 if len(len_player1) > len(len_player2) else len_player2

        for i in range(len(max_len_player)):
            if i < len(first_movs.get("movs")):
                total_movs.append({
                    "player": first_movs.get("player"),
                    "mov": first_movs.get("movs")[i],
                    "player_type": first_movs.get("player_type")
                })
            if i < len(second_movs.get("movs")):
                total_movs.append({
                    "player": second_movs.get("player"),
                    "mov": second_movs.get("movs")[i],
                    "player_type": second_movs.get("player_type")
                })

        return total_movs

    def play(self, movs):
        """
        Method to run the simulation
        :param movs: []
        :return: str
        """
        winner = self.get_winner()
        if winner:
            return winner.get_name()

        message = ""
        for x in movs:
            if x.get("player_type") == 1:
                self.get_player2().change_energy(self.get_player1().get_damage(x.get("mov")))
            elif x.get("player_type") == 2:
                self.get_player1().change_energy(self.get_player2().get_damage(x.get("mov")))

            if self.get_winner():
                    message = self.get_winner().get_name()
                    return message

        return self.play(movs)




    

        