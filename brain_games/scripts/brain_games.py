import sys
from brain_games.engine import play
from brain_games.utils import welcome_user
from brain_games.scripts.brain_games import main


def choose_game(game_name):
    if game_name == 'calc':
        from brain_games.games.calc import play_calc_game
        play_calc_game()
    elif game_name == 'even':
        from brain_games.games.even import play_even_game
        play_even_game()
    elif game_name == 'gcd':
        from brain_games.games.gcd import play_gcd_game
        play_gcd_game()
    elif game_name == 'prime':
        from brain_games.games.prime import play_prime_game
        play_prime_game()
    elif game_name == 'progression':
        from brain_games.games.progression import play_progression_game
        play_progression_game()
    else:
        print("Unknown game: {}".format(game_name))

def select_game_manually():
    available_games = ['calc', 'even', 'gcd', 'prime', 'progression']
    print("Available games:")
    for idx, game in enumerate(available_games, start=1):
        print(f"{idx}. {game.capitalize()} Game")
    
    choice = None
    while True:
        try:
            choice = int(input("Choose a game (enter its number): "))
            if 1 <= choice <= len(available_games):
                selected_game = available_games[choice - 1]
                choose_game(selected_game)
                break
            else:
                print("Invalid selection. Please enter a valid number.")
        except ValueError:
            print("Please enter a valid integer.")

def main():
    args = sys.argv[1:]
    if len(args) > 0:
        choose_game(args[0].strip())
    else:
        select_game_manually()

if __name__ == "__main__":
    print("Welcome to the Brain Games!\n")
    main()

