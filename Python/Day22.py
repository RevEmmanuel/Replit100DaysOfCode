import random

for i in range(10):
  myNumber = random.randint(1, 100)
  print(myNumber)

print("One Million To One")
print()
answer = random.randint(1, 1_000_000)
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