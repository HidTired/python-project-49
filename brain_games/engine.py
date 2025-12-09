from brain_games.cli import welcome_user
from prompt import string


def play(game_module):
    """
    Основной цикл игры. Получает игру game_module и проводит три раунда.
    """
    player_name = welcome_user()  # Запрашиваем имя пользователя и запоминаем его
    rounds_count = 3
    
    for _ in range(rounds_count):
        question, correct_answer = game_module.generate_question_and_answer()
        
        print(f"\nQuestion: {question}")
        user_answer = string("Your answer: ").strip()
        
        if str(user_answer) != str(correct_answer):
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Lets try again, {player_name}!")
            break
        else:
            print("Correct!")
    else:
        print("\nCongratulations, {}!".format(player_name))