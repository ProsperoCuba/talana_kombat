class Player:

    def __init__(self, combinations, sequences, name, player_type):
        self.energy = 6
        self.name = name
        self.combinations = combinations
        self.movements = sequences.get('movimientos')
        self.hits = sequences.get('golpes')
        self.player_combinations = list(zip(self.movements, self.hits))
        self.type = player_type


    def get_energy(self):
        return self.energy

    def change_energy(self, energy):
        self.energy -= energy
        return self.energy

    def get_movements(self):
        return self.movements

    def get_hits(self):
        return self.hits

    def get_total_movements(self):
        """Method to obtain the total number of movements"""

        return self.get_cant_movements() + self.get_cant_hits()

    def get_cant_movements(self):
        """Method to obtain the number of movements"""

        c = 0
        for x in self.get_movements():
            if x != "":
                c += 1
        return c

    def get_cant_hits(self):
        """Method to obtain the number of strokes"""
        c = 0
        for x in self.get_hits():
            if x != "":
                c += 1
        return c

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_player_combinations(self):
        return self.player_combinations

    def get_damage(self, mov):
        """
        Method to obtain the damage according to the movement passed by parameter
        :param mov: ()
        :return: int
        """
        for c in self.combinations:
            if any([mov[0] == "" and mov[1] == "", mov[1] == ""]):
                return 0
            elif mov[0] == "" and mov[1] in ["P", "K"]:
                return 1
            else:

                if c.get("key")[0] in mov[0] and mov[1] == c.get("key")[1]:
                    return c.get("damage")
                elif mov[1] in ["P", "K"]:
                    return 1

        return 0             
    
    def get_type(self):
        return self.type


class PlayerBuilder:
    PLAYER_1 = 1
    PLAYER_2 = 2
    combinations = {
        PLAYER_1: [
            {
                "damage": 3,
                "key": ("DSD", "P")
            },
            {
                "damage": 2,
                "key": ("SD", "K")
            },
            {
                "damage": 1,
                "key": ("", "P")
            },
            {
                "damage": 1,
                "key": ("", "K")
            }
        ],
        PLAYER_2: [
            {
                "damage": 3,
                "key": ("SA", "K")
            },
            {
                "damage": 2,
                "key": ("ASA", "P")
            },
            {
                "damage": 1,
                "key": ("", "P")
            },
            {
                "damage": 1,
                "key": ("", "K")
            }
        ]
    }

    @classmethod
    def build_player(cls, type, sequences, name):
        if type not in [cls.PLAYER_1, cls.PLAYER_2]:
            raise Exception("Player type not recognized")
        return Player(cls.combinations.get(type), sequences, name, type)

