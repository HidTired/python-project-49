import random
from math import gcd

law = "Find the greatest common divisor of given numbers."


def game_concept():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f"{num1} {num2}"
    correct_answer = str(gcd(num1, num2))
    return question, correct_answer
