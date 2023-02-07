import random, os, time

bingo = []

def random_number():
  number = random.randint(1,90)
  return number

def pretty_print():
  for row in bingo:
    for item in row:
      print(item, end="\t|\t")
    print()

def create_card():
  global bingo
  numbers = []
  for i in range(8):
    num = random_number()
    while num in numbers:
      num = random_number()
    numbers.append(random_number())
  
  numbers.sort()
  
  bingo = [ [ numbers[0], numbers[1], numbers[2]],
            [ numbers[3], "BG", numbers[4] ],
            [ numbers [5], numbers[6], numbers[7]]
          ]

create_card()
while True:
  pretty_print()
  num = int(input("Next Number: "))
  for row in range(3):
    for item in range(3):
      if bingo[row][item] == num:
        bingo[row][item] = "X"

  exes = 0
  for row in bingo:
    for item in row:
      if item=="X":
        exes+=1

  if exes == 8:
    print("You have won")
    break

  time.sleep(1)
  os.system("clear")