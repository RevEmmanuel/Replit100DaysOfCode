import os, time
inventory = []

try:
  f = open("inventory", "r")
  inventory = eval(f.read())
  f.close()
except:
  pass

def add_item():
  time.sleep(1)
  os.system("cls")
  print("INVENTORY")
  print("=========")
  print()
  item = input("Item to add > ").capitalize()
  inventory.append(item)
  print("Added")

def view_item():
  time.sleep(1)
  os.system("cls")
  print("INVENTORY")
  print("=========")
  print()
  seen = []
  for item in inventory:
    if item not in seen:
      print(f"{item} {inventory.count(item)}")
      seen.append(item)

  time.sleep(2)

def remove_item():
  time.sleep(1)
  os.system("cls")
  print("INVENTORY")
  print("=========")
  print()
  item = input("Item to remove > ").capitalize()
  if item in inventory:
    inventory.remove(item)
    print("Removed")
  else:
    print("You don't have that item")


while True:
  time.sleep(1)
  os.system("cls")
  print("INVENTORY")
  print("=========")
  print()
  menu = input("1: Add\n2: View\n3: Remove\nElse: Exit\n> ")
  if menu=="1":
    add_item()
  elif menu=="2":
    view_item()
  elif menu == "3":
    remove_item()
  else:
    f = open("inventory.txt", "w")
    f.write(str(inventory))
    f.close()
    break

  f = open("inventory.txt", "w")
  f.write(str(inventory))
  f.close()
