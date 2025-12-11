from brain_games.games.calc import play_calc_game
from brain_games.utils import welcome_user, prompt_string

username = welcome_user()
def main():
    play_calc_game()

if __name__ == "__main__":
    main()