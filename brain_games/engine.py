from brain_games.utils import welcome_user, prompt_string


def play(question_generator):
    rounds_to_win = 3
    wins = 0

    while wins < rounds_to_win:
        question, correct_answer = question_generator()
        print(f"Question: {question}")
        user_answer = prompt_string("Your answer: ").strip()
        
        if user_answer == str(correct_answer):
            print("Correct!")
            wins += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {player_name}!")
            break

    if wins >= rounds_to_win:
        print(f"Congratulations, {player_name}!")