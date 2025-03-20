print("Welcome to the tip calculator.")

bill = float(input("What was the total bill?\n$"))
tip = int(input("What percent tip would you like to leave?\n"))

bill_with_tip = bill * (1 + tip / 100)

print(f"Total bill is ${bill_with_tip:.2f}.")

number_of_splits = int(input("How many people are splitting the bill?\n"))

split = bill_with_tip / number_of_splits
print(f"Each person pays ${split:.2f}.")
