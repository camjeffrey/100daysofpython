import random
import string

print("Welcome to the password generator.\nEnter how many letters, numbers, and symbols you would like in your password.")
num_letters = int(input("Letters: "))
num_numbers = int(input("Numbers: "))
num_symbols = int(input("Symbols: "))

password = []

for letter in range(0, num_letters + 1):
	password.append(random.choice(string.ascii_letters))

for number in range(0, num_numbers + 1):
	password.append(random.choice(string.digits))

for symbol in range(0, num_symbols + 1):
	password.append(random.choice(string.punctuation))

random.shuffle(password)

print(''.join(password))
