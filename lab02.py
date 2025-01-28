import random

# Define the weapons array
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]

# Roll the dice (1-6)
weaponRoll = random.randint(1, 6)

# Define hero's combat strength (example value)
combatStrength = 10

# Add weaponRoll to hero's combat strength
combatStrength += weaponRoll

# Use weaponRoll as an index into the weapons array
heroWeapon = weapons[weaponRoll - 1]

# Print out the name of the hero's weapon
print(f"The hero's weapon is: {heroWeapon}")

# Define the conditions
if weaponRoll <= 2:
    print("You rolled a weak weapon, friend.")
elif weaponRoll <= 4:
    print("Your weapon is meh.")
else:
    print("Nice weapon, friend!")

# Additional condition for Fist
if heroWeapon != "Fist":
    print("Thank goodness you didn't roll the Fist...")

# Error handling for user input
user_input = input("Enter a number between 1-6: ")
if user_input.isdigit():
    user_input = int(user_input)
    if 1 <= user_input <= 6:
        print(f"You entered a valid number: {user_input}")
    else:
        print("Error: The number must be between 1 and 6.")
else:
    print("Error: Please enter a valid number.")
