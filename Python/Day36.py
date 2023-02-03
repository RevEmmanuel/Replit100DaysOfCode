list_of_names = []

def printList():
  print()
  for name in list_of_names:
    print(name)
  print()

while True:
  first_name = input("First Name: ").strip().capitalize()
  last_name = input("Last Name: ").strip().capitalize()
  name = f"{first_name} {last_name}"
  if name not in list_of_names:
    list_of_names.append(name)
  else:
    print("ERROR: Duplicate name")
  printList()