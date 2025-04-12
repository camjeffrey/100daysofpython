import random
from game_data import data

def new_item_select(current_item):
	'''
	Select new item from data which is not equal to current item
	'''
	while True:
		new_item = random.choice(data)
		if new_item != current_item:
			return new_item

def get_guess():
	'''
	Prompt user for a guess until valid input is received
	'''
	while True:
		guess = input("Which has more followers, 'a' or 'b'?: ")
		if guess.lower() == 'a':
			return 'a'
		elif guess.lower() == 'b':
			return 'b'
		else:
			print("Invalid guess.")

def evaluate_items(current_item, new_item):
	'''
	Determine whether current_item or new_item has more followers
	'''
	if current_item['follower_count'] > new_item['follower_count']:
		return 'a'
	else:
		return 'b'

def print_items(current_item, new_item):
	'''
	Print message detailing the items for the user to compare
	'''
	print(f"Compare A: {current_item['name']}, {current_item['description']} from {current_item['country']}.\n")
	print("vs.\n")
	print(f"B: {new_item['name']}, {new_item['description']} from {new_item['country']}.\n")


def main():
	current_item = random.choice(data)
	while True:
		new_item = new_item_select(current_item)

		correct_answer = evaluate_items(current_item, new_item)

		print_items(current_item, new_item)

		user_guess = get_guess()

		if user_guess == correct_answer:
			print("Correct!")
			if new_item['follower_count'] > current_item['follower_count']:
				current_item = new_item
		else:
			print("Incorrect!")
			return

main()