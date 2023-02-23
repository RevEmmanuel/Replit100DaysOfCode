import tkinter as tk

window = tk.Tk()
window.title("Calculator")
window.geometry("400x200")

answer = 0
last_number = 0
operator = None


def type_answer(value):
  global answer
  answer = f"{answer}{value}"
  answer = int(answer)
  hello["text"] = answer


def calc_answer(this_op):
  global answer, last_number, operator
  last_number = answer
  answer = 0
  if this_op == "+":
    operator = "+"
  elif this_op == "-":
    operator = "-"
  elif this_op == "*":
    operator = "*"
  elif this_op == "/":
    operator = "/"
  hello["text"] = answer


def calc():
  global answer, last_number, operator
  print(f"{last_number}\t{answer}\t{operator}")
  if operator == "+":
    total = last_number + answer
  elif operator == "-":
    total = last_number - answer
  elif operator == "*":
    total = last_number * answer
  elif operator == "/":
    total = last_number / answer
  answer = total
  hello["text"] = answer


hello = tk.Label(text=answer)
hello.grid(row=0, column=1)

one = tk.Button(text="1", command=lambda: type_answer(1))
one.grid(row=1, column=0)

two = tk.Button(text="2", command=lambda: type_answer(2))
two.grid(row=1, column=1)

three = tk.Button(text="3", command=lambda: type_answer(3))
three.grid(row=1, column=2)

four = tk.Button(text="4", command=lambda: type_answer(4))
four.grid(row=2, column=0)

five = tk.Button(text="5", command=lambda: type_answer(5))
five.grid(row=2, column=1)

six = tk.Button(text="6", command=lambda: type_answer(6))
six.grid(row=2, column=2)

seven = tk.Button(text="7", command=lambda: type_answer(7))
seven.grid(row=3, column=0)

eight = tk.Button(text="8", command=lambda: type_answer(8))
eight.grid(row=3, column=1)

nine = tk.Button(text="9", command=lambda: type_answer(9))
nine.grid(row=3, column=2)

zero = tk.Button(text="0", command=lambda: type_answer(0))
zero.grid(row=4, column=1)

add = tk.Button(text="+", command=lambda: calc_answer("+"))
add.grid(row=1, column=4)

minus = tk.Button(text="-", command=lambda: calc_answer("-"))
minus.grid(row=1, column=5)

multiply = tk.Button(text="*", command=lambda: calc_answer("*"))
multiply.grid(row=2, column=4)

divide = tk.Button(text="/", command=lambda: calc_answer("/"))
divide.grid(row=2, column=5)


equals = tk.Button(text="=", command=calc)
equals.grid(row=4, column=4)


tk.mainloop()
