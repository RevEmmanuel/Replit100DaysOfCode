import os, time
to_do_list = []

def print_list():
  print()
  for items in to_do_list:
    print(items)
  print()

while True:
  menu = input("ToDo List Manager\nDo you want to view, add, edit, remove or delete the todo list?\n")
  if menu == "view":
    print_list()
  elif menu== "add" :
    item = input("What do you want to add?\n").title()
    to_do_list.append(item)
  elif menu == "remove":
    item = input("What do you want to remove?\n").title()
    check = input("Are you sure you want to remove this?\n")
    if check[0] == "y":
      if item in to_do_list:
        to_do_list.remove(item)
    else:
        print(f"Item {item} not found.")
  elif menu=="edit":
    item = input("What do you want to edit?\n").title()
    new = input("What do you want to change it to?\n").title()
    for i in range(0,len(to_do_list)):
      if to_do_list[i] == item:
        to_do_list[i] = new
  elif menu == "delete":
    to_do_list = []
  time.sleep(1)
  os.system('cls')