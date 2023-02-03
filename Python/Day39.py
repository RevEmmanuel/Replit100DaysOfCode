import random, os, time

list_of_fruits = ["apple", "orange", "grapes", "pear"]
letter_picked = []
lives = 6

word = random.choice(list_of_fruits)

while True:
  time.sleep(1)
  os.system("cls")
  letter = input("Choose a letter: ").lower()
  
  if letter in letter_picked:
    print("You've tried that before")
    continue
    
  letter_picked.append(letter)
  
  if letter in word:
    print("You found a letter")
  else:
    print("Nope, not in there")
    lives -= 1
  
  all_letters = True
  print()
  for i in word:
    if i in letter_picked:
      print(i, end="")
    else:
      print("_", end="")
      all_letters = False
  print()

  if all_letters:
    print(f"You won with {lives} left!")
    break

  if lives <= 0:
    print(f"You ran out of lives! The answer was {word}")
    break
  else:
    print(f"Only {lives} left")
