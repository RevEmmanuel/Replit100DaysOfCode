import random

bingo = []

def random_number():
  number = random.randint(1,90)
  return number

def pretty_print():
  for row in bingo:
    print(row)

numbers = []
for i in range(8):
  numbers.append(random_number())

numbers.sort()

bingo = [ [ numbers[0], numbers[1], numbers[2]],
          [ numbers[3], "BINGO", numbers[4] ],
          [ numbers [5], numbers[6], numbers[7]]
        ]

pretty_print()