print("One Million To One")
print()
answer = 74292045
number_of_trials = 1
while True:
    guess = int(input("What is your guess? "))
    if guess < 0:
        print("I'm done!")
        exit(0)
    elif guess == answer:
        print("Correct! ")
        print("It took you", number_of_trials, "guesses to get it right!")
        break
    elif guess < answer:
        print("Too low.")
    elif guess > answer:
        print("Too high.")
    number_of_trials += 1