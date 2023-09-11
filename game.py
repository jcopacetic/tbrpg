import random 
from player import Baddy 

class Game:
    def __init__(self):
        self.game_over = False 
        self.round = 0

    def new_round(self):
        self.round += 1 
        print(f"\n Round {self.round} \n")

    def check(self, player, opponent):
        if player.health < 1 and opponent.health > 0:
            player.gain_exp(4)
            self.game_over = True 
            print("\nGame Over! You lose.\n")
            return False
        elif opponent.health < 1 and player.health > 0:
            player.gain_exp(12)
            self.game_over = True 
            print("\nGame Over! You Win!\n")
            return False
        elif player.health < 1 and opponent.health < 1:
            player.gain_exp(6)
            self.game_over = True 
            print("\ngame Over! Draw!\n")
            return False
        return True 
    
    def take_turn(self, player, opponent):
        if isinstance(player, Baddy):
            user_input = "attack"
        else: 
            user_input = input("Attack or Run:   ")
        
        if user_input == "attack":
            moves = [f"[ {index + 1} ] {move['name']} atk: {move['attack']} pp: {move['pp']}" for index, move in enumerate(player.moves)]
            moves = "\n".join(moves)


            if isinstance(player, Baddy):
                available_moves = [move for move in player.moves if move["pp"] > 0]

                if available_moves:
                    move = random.choice(available_moves)
                else:
                    print("Enemy has no moves with PP > 0 available.")

            else:
                move = None 

                while not move:
                    user_input = input(f"\nchoose your attack: \n{moves}\n")
                    move = player.moves[int(user_input) - 1]
                    if move["pp"] > 0:
                        break
                    print("\nthat move is out of pp, try another\n")
                    move = None
                

            opponent.take_damage(player, move)
            
        elif user_input == "run":
            self.try_to_escape(player, opponent)
        else: 
            print("Invalid command. Try again.")

    def try_to_escape(self, player, opponent):
        escape_change = 0.3
        if random.random() < escape_change: 
            print("You successfully escaped")
            self.game_over = True 
        else: 
            print("Sorry, you can't get away!")
            self.take_turn(opponent, player)

