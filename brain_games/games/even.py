import random
from brain_games import utils
from brain_games.utils import welcome_user, prompt_string
from brain_games.engine import play

def generate_random_number():
    return random.randint(1, 100)

def is_even(num):
    return num % 2 == 0


def play_even_game():
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    rounds_to_win = 3
    current_round = 0
    

    while current_round < rounds_to_win:
        number = generate_random_number()
        print(f"\nQuestion: {number}")
        
        user_answer = prompt_string("Your answer: ").strip().lower()
        
        correct_answer = "yes" if is_even(number) else "no"
        
        if user_answer == correct_answer:
            print("Correct!")
            current_round += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {utils.name}!")
            return
    
    print(f"Congratulations, {utils.name}!")

def generate_question_and_answer():
    number = random.randint(1, 100)
    question = str(number)
    answer = "yes" if number % 2 == 0 else "no"
    return question, answer

def play_game():
    from brain_games.games import even as game_module
    play(game_module)

if __name__ == "__main__":
    play_even_game()
