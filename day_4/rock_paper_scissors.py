import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

print("Welcome to Rock, Paper, Scissors.")
user_choice = int(input("Type '1' for rock, '2' for paper, '3' for scissors: "))
computer_choice = random.randint(1,3)

if user_choice == 1:
    print(rock)
    print(f"\nYou chose rock.")
elif user_choice == 2:
    print(paper)
    print(f"\nYou chose paper.")
else:
    print(scissors)
    print(f"\nYou chose scissors.")



if computer_choice == 1:
    print(rock)
    print(f"The computer chose rock.\n")
elif computer_choice == 2:
    print(paper)
    print(f"The computer chose paper.\n")
elif computer_choice == 3:
    print(scissors)
    print(f"The computer chose scissors.\n")



if user_choice == computer_choice:
    print("It's a draw.")
elif user_choice == 1 and computer_choice == 2:
    print("You lose.")
elif user_choice == 1 and computer_choice == 3:
    print("You won.")
elif user_choice == 2 and computer_choice == 1:
    print("You won.")
elif user_choice == 2 and computer_choice == 3:
    print("You lose.")
elif user_choice == 3 and computer_choice == 1:
    print("You lose.")
elif user_choice == 3 and computer_choice == 2:
    print("You win.")