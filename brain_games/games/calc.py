import random
from operator import add, sub, mul
from brain_games import utils
from brain_games.utils import welcome_user, prompt_string
from brain_games.engine import play
import sys  

print("What is the result of the expression?")

OPERATIONS = {
    '+': add,
    '-': sub,
    '*': mul
}

def generate_question_and_answer():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operation = random.choice(list(OPERATIONS.keys()))
    
    question = f"{num1} {operation} {num2}"
    correct_answer = OPERATIONS[operation](num1, num2)
    return question, correct_answer

def play_calc_game():
    play(generate_question_and_answer)
    print("What is the result of the expression?")
    rounds_to_win = 3
    current_round = 0
    
    while current_round < rounds_to_win:
        question, correct_answer = generate_question_and_answer()
        print(f"\nQuestion: {question}") 
        
        user_answer = prompt_string("Your answer: ").strip() 
        
        try:
            user_answer_int = int(user_answer)
        except ValueError:
            print("Please provide a numeric answer.")
            continue
            
        if user_answer_int == correct_answer:
            print("Correct!")
            current_round += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {utils.name}!")
            return
    
    print(f"Congratulations, {utils.name}!")




if __name__ == "__main__":
    play_calc_game()