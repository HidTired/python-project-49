import sys
from brain_games.engine import play
from brain_games.utils import welcome_user

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
        print(f"Unknown game: {game_name}")

if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) > 0:
        choose_game(args[0].strip())
    else:
        print("Please specify which game to play.")