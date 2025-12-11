from brain_games.games.gcd import play_gcd_game
from brain_games.utils import welcome_user, prompt_string

username = welcome_user()

def main():
    play_gcd_game()

if __name__ == "__main__":
    main()