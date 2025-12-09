import random
from operator import add, sub, mul
from brain_games.engine import play  

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

def play_game():
    from brain_games.games import calc as game_module
    play(game_module)