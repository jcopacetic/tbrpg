from player import Player, Baddy 
from game import Game 

def main():
    
    player = Player()

    commands = """
    
            COMMANDS:
            game - battle tower
            exit - close program  
            player - Player information  
            commands - see these commands                       
                                    
    """

    print(commands)

    while True:
        user_input = input("""enter command:  """)

        if user_input == "game":
            
            current_game = Game()
            baddy = Baddy()

            print(f"""

            Time To FIGHT!
        
            {baddy.name} ({baddy.type.name})
            hp: {baddy.health} - atk: {baddy.attack}

                VS. 
            
            {player.name} ({player.type.name})
            hp: {player.health} - atk: {player.attack}          
""")

            while not current_game.game_over:
                current_game.new_round()
                current_game.take_turn(player, baddy)
                print(f"{baddy.name}'s health = {baddy.health}\n")
                if not current_game.check(player, baddy):
                    player.heal()
                    break
                current_game.take_turn(baddy, player)
                print(f"{player.name}'s health = {player.health}\n")
            
            print("turtles")

        elif user_input == "player":
            print(f"""
                Name: {player.name}
                type: {player.type.name}
                Health: {player.health}
                Level: {player.level}
                Attack: {player.attack}
                Exp: {player.exp}
""")
           
            for move in player.moves:
                move_info = f"Name: {move['name']}, Type: {move['type'].name}, Attack: {move['attack']}, PP: {move['pp_now']}/{move['pp']}"
                print(move_info)
                    
        elif user_input == "commands":
            print(commands)
        
        elif user_input == "exit":
            print("Goodbye!")
            break

        else: 
            print("Invalid command. Try again.")



if __name__ == "__main__":
    main()
