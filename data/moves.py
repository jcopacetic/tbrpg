from utils import Types 

MOVES = [
    {
        "id": 1,
        "name": "swipe",
        "type": Types.normal,
        "attack": 10,
        "pp": 30,
        "pp_now": 30
    },
    {
        "id": 2,
        "name": "tackle",
        "type": Types.normal,
        "attack": 15,
        "pp": 20,
        "pp_now": 20
    },
    {
        "id": 3,
        "name": "body slam",
        "type": Types.normal,
        "attack": 20,
        "pp": 5,
        "pp_now": 5
    },
    {
        "id": 4,
        "name": "body slam",
        "type": Types.normal,
        "attack": 20,
        "pp": 5,
        "pp_now": 5
    },
    {
        "id": 5,
        "name": "Power Slam",
        "type": Types.normal,
        "attack": 30,
        "pp": 1,
        "pp_now": 1
    }

]

class Move:
    def __init__(self, move):
        self.name = move["name"]
        self.type = move["type"]
        self.attack = move["attack"]
        self.pp = move["pp"]
        self.pp_now = move["pp_now"]