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

def mode_selection():
    while True:
        mode = input("Select difficulty: type 'easy' for 10 guesses, type 'hard' for 5: ")
        if mode.lower() != 'easy' and mode.lower() != 'hard':
            print("Invalid selection.")
        elif mode.lower() == 'easy':
            lives = difficulty('easy')
            return 'easy'
        else:
            lives = difficulty('hard')
            return 'hard'

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

    # Begin game loop

    answer = random_number()

    print("I'm thinking of a number between 0 - 100 (inclusive)...\n")

    lives = difficulty(mode_selection()) # mode_selection() returns 'easy' or 'hard', which is then assessed by difficulty()
        
    while lives > 0:

        guess = get_guess()
        if guess_checker(guess, answer):
            break
        else: 
            lives -= 1
            print(f"Guesses remaining: {lives}")

    if lives == 0:
        print(f"The number was {answer}.\n")
    play_again = input("Type 'y' to play again!: ")
    if play_again == 'y':
        continue
    else:
        break