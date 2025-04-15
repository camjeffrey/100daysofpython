import sys
from machine_data import menu, resources, funds

def get_selection():
	'''
	Prompt user for menu selection, continue until valid input received
	'''
	while True:
		selection = input("'Cappuccino', 'Latte', or 'Espresso'?: ")
		if selection.lower() == "cappuccino":
			return "cappuccino"
		elif selection.lower() == "latte":
			return "latte"
		elif selection.lower() == "espresso":
			return "espresso"
		elif selection.lower() == "off":
			sys.exit("Powering off...")
		elif selection.lower() == "report":
			return "report"
		elif selection.lower() == "top-up":
			return "top-up"
		else:
			print("Invalid selection.")

def resource_check(selection, resources):
	'''
	Cycle through resources and ingredients required, return false if resources not equal to or greater than requirements
	'''
	for resource in ['water', 'milk', 'coffee']:
		if resource in selection['ingredients']:
			if not resources[resource] >= selection['ingredients'][resource]:
				print("Error -- insufficient resources available.")
				return False
	return True

def output_report():
	'''
	Print resources remaining
	'''
	print(f"Water: {resources['water']}")
	print(f"Milk: {resources['milk']}")
	print(f"Coffee: {resources['coffee']}")
	print(f"Funds: {funds}")

def process_payment(selection):
	'''
	Prompt user to insert payment, refund if insufficient, provide change if required
	'''
	total_payment = 0
	while True:
		try:
			quarters = int(input("Quarters: "))
			dimes = int(input("Dimes: "))
			nickels = int(input("Nickels: "))
			pennies = int(input("Pennies: "))
		except ValueError:
			print("Error -- Please enter whole numbers only!")
		else:
			total_payment = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
			break

	if total_payment < selection['cost']:
		print("Insufficient payment. Refunding...")
		return False
	elif total_payment == selection['cost']:
		print("Exact change received. Brewing...")
		return True
	elif total_payment > selection['cost']:
		print(f"Dispensing change: ${total_payment - selection['cost']:.2f}. Brewing...")
		return True

def update_machine_data(selection, resources, funds):
	'''
	Process changes to resource and fund levels inside machine
	'''
	funds += selection['cost']
	for resource in ['water', 'milk', 'coffee']:
		if resource in selection['ingredients']:
			resources[resource] -= selection['ingredients'][resource]
	return funds

def add_resources(resources):
	'''
	Add to machine resources
	'''
	while True:
		try:
			water_to_add = int(input("Water added: "))
			milk_to_add = int(input("Milk added: "))
			coffee_to_add = int(input("Coffee added: "))
		except ValueError:
			print("Error -- Please enter whole numbers only!")
		else:
			resources['water'] += water_to_add
			resources['milk'] += milk_to_add
			resources['coffee'] += coffee_to_add
			return "Top-up successful!"

def main():
	'''
	Begin main logic
	'''
	global funds
	
	selection = selection_string = get_selection()
	if selection == "report":
		output_report()
		return
	elif selection == "top-up":
		add_resources(resources)
		return
	else:
		selection = menu[selection]

	if not resource_check(selection,resources):
		return

	if process_payment(selection):
		print(f"Dispensing your {selection_string}... Enjoy!")
		funds = update_machine_data(selection, resources, funds)
		return

# Intialise program
while True:
	main()














