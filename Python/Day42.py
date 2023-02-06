beast_name = {"Beast Name": None, "Type": None, "Special Move": None, "HP": None, "MP": None}

print("MokéBeast")
print()

for name, value in beast_name.items():
  beast_name[name] = input(f"{name}:\t").strip().title()

if beast_name["Type"]=="Earth":
  print("\033[32m", end="")
elif beast_name["Type"]=="Air":
  print("\033[37m", end="")
elif beast_name["Type"]=="Fire":
  print("\033[31m", end="")
elif beast_name["Type"]=="Water":
  print("\033[34m", end="")
else:
  print("\033[33m", end="")

for name, value in beast_name.items():
  print(f"{name:<15}: {value}")