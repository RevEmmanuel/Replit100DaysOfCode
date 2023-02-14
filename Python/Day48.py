import os, time

while True:
  print("HIGH SCORE TABLE")
  print()
  name = input("INITIALS > ").upper()
  score = input("SCORE > ")
  print()

  f = open("high_score_file", "a+")
  f.write(f"{name} {score}\n")
  f.close()

  print("ADDED")

  if (input("Add another score? (y/n)") == "n"):
    break
  time.sleep(1)
  os.system("cls")