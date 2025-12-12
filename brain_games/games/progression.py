import random

law = 'What number is missing in the progression?'


def generate_sequence():
    initial_value = random.randint(1, 20)
    seq_len = random.randint(5, 10)
    increment_step = random.randint(2, 10)
    
    sequence = [initial_value]
    for _ in range(seq_len - 1):
        next_val = sequence[-1] + increment_step
        sequence.append(next_val)
    
    return sequence


def game_concept():
    sequence = generate_sequence()
    secret_number = random.choice(sequence)
    hidden_idx = sequence.index(secret_number)
    sequence[hidden_idx] = '..'
    
    question = ' '.join(map(str, sequence))
    correct_answer = str(secret_number)
    
    return question, correct_answer