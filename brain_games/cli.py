import prompt


def welcome_user():
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name

def prompt_string(prompt_text):
    return input(prompt_text)