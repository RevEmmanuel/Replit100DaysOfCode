import os, time, random

def show():
  os.system("cls")
  f = open("idea_file", "r")
  ideas = f.read().split("\n")
  f.close()
  idea = random.choice(ideas)
  print(idea)

while True:
    print(" 🌟Idea Storage🌟 ")
    idea = open("idea_file", "a+")

    option = input("Add an idea or see a random idea? a/r (Enter anything else to quit) > ").lower()
    if option == "a":
        os.system("cls")
        idea.write(input("Enter your idea: > ") + "\n")
        print("Nice! Your idea has been stored.")
        time.sleep(1)
    elif option == "r":
        show()
        time.sleep(2)
    else:
        print("Please enter a valid choice.")
        break
    idea.close()
    os.system("cls")
    time.sleep(3)