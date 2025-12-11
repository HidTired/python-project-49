import random
from brain_games.utils import welcome_user, prompt_string
from brain_games.engine import play

def create_arithmetic_progression(length, start, step):
    return [start + i * step for i in range(length)]

def hide_element(progression):

    hidden_position = random.randrange(len(progression))
    progression[hidden_position] = '..'
    return progression, hidden_position

username = welcome_user()

def play_progression_game():
    print("What number is missing in the progression?")

    correct_answers_needed = 3
    current_correct_answers = 0

    while current_correct_answers < correct_answers_needed:
        length = random.randint(5, 10)  
        start = random.randint(1, 50)  
        step = random.randint(1, 10)    

        progression = create_arithmetic_progression(length, start, step)
        progression_with_hidden, hidden_position = hide_element(progression[:])

        print("Question:", " ".join(map(str, progression_with_hidden)))
        user_answer = prompt_string("Your answer: ")

        correct_answer = progression[hidden_position]

        if int(user_answer.strip()) == correct_answer:
            print("Correct!")
            current_correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {username}!")
            return

    print(f"Congratulations, {username}!")

if __name__ == "__main__":
    play_progression_game()