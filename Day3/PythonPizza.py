# Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.

# Based on a user's order, work out their final bill. Use the input() function to get a user's preferences and then add up the total for their order and tell them how much they have to pay.

# Small pizza (S): $15

# Medium pizza (M): $20

# Large pizza (L): $25

# Add pepperoni for small pizza (Y or N): +$2

# Add pepperoni for medium or large pizza (Y or N): +$3

# Add extra cheese for any size pizza (Y or N): +$1

# Example Interaction
# Welcome to Python Pizza Deliveries!
# What size pizza do you want? S, M or L: L
# Do you want pepperoni on your pizza? Y or N: Y
# Do you want extra cheese? Y or N: N
# Your final bill is: $28.
#  Hint 
# Don't change any of the starting code and make sure that the final sentence says "Your final bill is: $." including the full stop and the same wording. Otherwise, the tests will not pass.
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").upper()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()

# Set the base price for the pizza
if size == 'S':
    pizza_price = 15
elif size == 'M':
    pizza_price = 20
elif size == 'L':
    pizza_price = 25
else:
    print("Invalid pizza size.")
    pizza_price = 0

# Add pepperoni cost based on pizza size
if pepperoni == 'Y':
    if size == 'S':
        pizza_price += 2
    else:
        pizza_price += 3

# Add extra cheese cost
if extra_cheese == 'Y':
    pizza_price += 1

# Print the final bill
print(f"Your final bill is: ${pizza_price}.")



