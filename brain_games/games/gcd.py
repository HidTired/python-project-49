import random
from math import gcd
from brain_games.utils import welcome_user, prompt_string
from brain_games.engine import play

def generate_question_and_answer():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f"{num1} {num2}"
    correct_answer = str(gcd(num1, num2))
    return question, correct_answer

def play_game():
    from brain_games.games import gcd as game_module
    play(game_module)

def generate_numbers():
    return random.randint(1, 100), random.randint(1, 100)


#username = welcome_user()

def play_gcd_game():

    print("Find the greatest common divisor of given numbers.")

    correct_answers_needed = 3
    current_correct_answers = 0

    while current_correct_answers < correct_answers_needed:
        num1, num2 = generate_numbers()
        print(f"Question: {num1} {num2}")
        user_answer = int(prompt_string("Your answer: "))

        correct_answer = gcd(num1, num2)

        if user_answer == correct_answer:
            print("Correct!")
            current_correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {username}!")
            return

    print(f"Congratulations, {username}!")

if __name__ == "__main__":
    play_gcd_game()
