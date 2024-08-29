#Tip Calculator
print("Welcome to the Tip Calculator.")

# Get the bill amount from the user
bill = float(input("What was the total bill? $"))

# Get the tip percentage from the user
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

# Get the number of people to split the bill
people = int(input("How many people to split the bill? "))

# Calculate the tip amount as a percentage of the bill
tip_as_percent = tip / 100

# Calculate the total tip amount
total_tip_amount = bill * tip_as_percent

# Calculate the total bill
total_bill = bill + total_tip_amount

# Calculate the bill per person
bill_per_person = total_bill / people

# Round the final amount to 2 decimal places
final_amount = round(bill_per_person, 2)

# Display the final result
print(f"Each person should pay: ${final_amount}")

