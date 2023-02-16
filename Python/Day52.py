import os, time
list_of_orders = []

try:
    with open("pizza_shop", "r") as file:
        data = file.read()
        list_of_orders = eval(data)
        file.close()
except Exception:
    print("No existing file found. Using empty list.")

def collect_input():
  try:
    number_of_pizza = int(input("How many pizzas? > "))
  except ValueError:
    print("You must input a numerical character, try again")
    collect_input()
  return number_of_pizza


def view_pizza():
  h1 = "Name"
  h2 = "Topping"
  h3 = "Size"
  h4 = "Quantity"
  h5 = "Total"
  print(f"{h1:^10}{h2:^20}{h3:^10}{h4:^10}{h5:^10}")
  for row in list_of_orders:
    print(f"{row[0]:^10}{row[1]:^20}{row[2]:^10}{row[3]:^10}{row[4]:^10}")
  time.sleep(2)

def add_pizza():
  time.sleep(1)
  os.system("cls")
  name = input("Name: ")
  toppings = input("Toppings: ")
  size = input("Size (s/m/l): ").lower()
  qty = collect_input()
  cost = 0
  if size=="s":
    cost = 5.99
  elif size=="m":
    cost = 9.99
  else:
    cost = 14.99
  total = cost * qty
  total = round(total, 2)
  print(f"Total is {total}")
  row = [name, toppings, size, qty, total]
  list_of_orders.append(row)

while True:
  time.sleep(1)
  os.system("cls")
  print(" 🌟Dave's Dodgy Pizzas🌟 ")
  print()
  menu = input("1: Add Pizza\n2: View Pizzas\n> ")
  if menu == "1":
    add_pizza()
  else:
    view_pizza()
  f = open("list_of_orders", "w")
  f.write(str(list_of_orders))
  f.close()

  if (input("Order again? (y/n) > ") == "n"):
    print("See you again soon!") 
    break
