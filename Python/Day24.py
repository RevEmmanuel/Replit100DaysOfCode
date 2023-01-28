import random

def rollDice(maximum_value):
    print("You rolled", random.randint(1, maximum_value))

print("Infinity Dice")
sides = int(input("How many sides? "))
while True:
    rollDice(sides)
    print()
    again = input("Roll again? ")
    if again == "yes" or again == "Yes":
        continue
    elif again == "no" or again == "No":
        break
