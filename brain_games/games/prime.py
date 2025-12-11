import random
from brain_games.utils import welcome_user, prompt_string
from brain_games.engine import play

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True

#username = welcome_user()

def play_prime_game():
    print("Answer 'yes' if given number is prime. Otherwise answer 'no'.")

    correct_answers_needed = 3
    current_correct_answers = 0

    while current_correct_answers < correct_answers_needed:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        user_answer = prompt_string("Your answer: ").strip().lower()

        correct_answer = "yes" if is_prime(number) else "no"

        if user_answer == correct_answer:
            print("Correct!")
            current_correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {username}!")
            return

    print(f"Congratulations, {username}!")

if __name__ == "__main__":
    play_prime_game()