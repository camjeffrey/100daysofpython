import random

def random_number():
    number = random.randint(0, 100)
    return number

def guess_checker(guess, number):
    if guess < number:
        print("Higher.\n")
        return False
    elif guess > number:
        print("Lower.\n")
        return False
    else:
        print("Correct!\n")
        return True

def difficulty(mode):
    if mode == 'easy':
        lives = 10
    elif mode == 'hard':
        lives = 5
    return lives

def get_guess():
    while True:
        try:
            guess = int(input("Enter a guess: "))
        except ValueError:
            print("Invalid guess, please guess a whole number.")
        else:
            break
    return guess


while True:

    answer = random_number()

    print("I'm thinking of a number between 0 - 100 (inclusive)...\n")
    print(f"DEBUG: The answer is {answer}")

    while True:
        mode = input("Select difficulty: type 'easy' for 10 guesses, type 'hard' for 5: ")
        if mode.lower() != 'easy' and mode.lower() != 'hard':
            print("Invalid selection.")
        elif mode == 'easy':
            lives = difficulty('easy')
            break
        else:
            lives = difficulty('hard')
            break
        
    while lives > 0:

        guess = get_guess()
        if guess_checker(guess, answer):
            break
        else: 
            lives -= 1
            print(f"Guesses remaining: {lives}")

    play_again = input("Type 'y' to play again!: ")
    if play_again == 'y':
        continue
    else:
        break