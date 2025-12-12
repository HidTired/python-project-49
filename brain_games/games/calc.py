import random
from operator import add, sub, mul

law = "What is the result of the expression?"

OPERATIONS = {
    '+': add,
    '-': sub,
    '*': mul
}


def game_concept():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operation = random.choice(list(OPERATIONS.keys()))
    
    question = f"{num1} {operation} {num2}"
    correct_answer = OPERATIONS[operation](num1, num2)
    return question, correct_answer



