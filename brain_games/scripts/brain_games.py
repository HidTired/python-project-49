from brain_games.cli import welcome_user
from .brain_games import main

if __name__ == "__main__":
    print("Welcome to the Brain Games!")

import prompt

name = prompt.string('May I have your name? ')
print(f'Hello, {name}!')