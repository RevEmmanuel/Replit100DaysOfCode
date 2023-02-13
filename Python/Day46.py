mokedex = {}


def pretty_print():
  print("Name\tType\tHP\tMP")
  for key, value in mokedex.items():
    print(
      f"""{key:^12}|{value["type"]:^10}|{value["hp"]:^6}|{value["mp"]:^6}"""
    )


while True:
  print("Add your Beast!")
  name = input("Name > ").title()
  type = input("Type > ").title()
  hp = int(input("HP > "))
  mp = int(input("MP > "))
  mokedex[name] = {"type": type, "hp": hp, "mp": mp}
  print("----------")
  print()
  pretty_print()
  if (input("Do you want to add another beast? (y/n").lower() == "n"):
    break
