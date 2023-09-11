import random 
from data.moves import MOVES, Move
from utils import Types, type_damage

class Player:
    def __init__(self):
        self.name = "player 1"
        self.type = random.choice(list(Types))
        self.health = 60
        self.total_health = 100
        self.attack = 12
        self.exp = 0
        self.level = 1
        self.moves = []
        random.shuffle(MOVES)
        moves = MOVES[:4]
        for move in moves:
            self.moves.append(Move(move))

    def take_damage(self, player, current_game, move):
        damage_calc = type_damage(self.type.name, player.type.name)

        if isinstance(move, dict):
            # Convert the dictionary to a Move object
            move = Move(move)
        
        print(move.attack)
        damage = move.attack if move else player.attack

        variable_damage = int(damage * random.uniform(damage_calc["min_percent"], damage_calc["max_percent"]))

        if variable_damage > self.health:
            self.health = 0
            if isinstance(self, Baddy):
                current_game.check(player, self)
            else: 
                current_game.check(self, player)
        else:
            self.health -= variable_damage

        if move:
            move.pp_now -= 1
            message = f"\n{player.name} attacks {self.name} with {move.name} for {variable_damage}"
        else: 
            message = f"{player.name} attacks {self.name} for {variable_damage}"
        
        print(message)

    def level_up(self):
        self.health += self.health * .2
        self.attack += self.attack * .2

    def gain_exp(self, exp):
        self.exp += exp
        level_thresholds = [34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986]
        print(f"experience gained: {exp}")

        exp_range = 20
        bonus_exp = random.randint(1, exp_range)  # Random bonus exp based on range
        self.exp += bonus_exp

        print(f"Bonus experience gained: {bonus_exp}")

        for x, threshold in enumerate(level_thresholds):
            if self.exp < threshold:
                new_level = x + 1
                if new_level > self.level:
                    self.level = new_level
                    self.level_up()
                    print(f"Your new level is {self.level}! {self.exp} / {threshold} total exp.")

                else:
                    print(f"{self.exp} / {threshold} total exp.")
                break

    def heal(self):
        self.health = self.total_health
        for move in self.moves:
            move.pp_now = move.pp
        

class Baddy(Player):
     def __init__(self):
        self.name = "bad guy"
        self.type = random.choice(list(Types))
        self.health = 70
        self.attack = 9
        random.shuffle(MOVES)
        self.moves = MOVES[:4]
