import os, time
to_do_list = []

def print_list():
  print()
  for item in to_do_list:
    print(item)
  print()

while True:
    choice = input("ToDoList Manager\n\nDo you want to view, add or edit the todo list?\n")
    if choice == "view":
        print_list()
    elif choice == "add":
        item = input("What do you want to add?\n")
        to_do_list.append(item)
        print("Item added successfully")
    elif choice == "edit":
        item = input("What do you want to remove?\n")
        if item in to_do_list:
            to_do_list.remove(item)
            print("Item has been removed")
        else:
            print("Item not found.")
    else:
        break
print("Done!")