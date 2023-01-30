print("30 Days down, what did you think? ")

for i in range(1, 31):
    thought = input(f"Day {i}: \n")
    default_text = f"You thought Day {i} was"
    print(f"{default_text:^35}")
    print(f"{thought:^35}")
print("Thanks for joining us!")