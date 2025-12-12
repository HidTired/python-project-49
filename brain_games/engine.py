import prompt



def play(game):
    rounds_to_win = 3
    wins = 0
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.law)



    while wins < rounds_to_win:
        question, correct_answer = game.game_concept()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ").strip()
        
        if user_answer == str(correct_answer):
            print("Correct!")
            wins += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break

    if wins >= rounds_to_win:
        print(f"Congratulations, {name}!")