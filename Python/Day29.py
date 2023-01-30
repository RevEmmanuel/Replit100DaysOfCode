def color_print(color, text):
  if color=="red":
    print("\033[31m", text, sep="", end="")
  elif color=="green":
    print("\033[32m", text, sep="", end="")
  elif color=="blue":
    print("\033[34m", text, sep="", end="")
  else:
    print("\033[0m", text, sep="", end="")

print("Super Subroutine")
print("With my ", end="")
color_print("red", "new program")
color_print("reset", " I can just call red('and') ")
color_print("red", "it will print in red ")
color_print("blue", "or even blue")