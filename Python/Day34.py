import os, time
list__of_email = []

def pretty_print():
  os.system("cls")
  print("list__of_email")
  print()
  counter = 1
  for email in list__of_email:
    print(f"{counter}: {email}")
    counter+=1
  time.sleep(1)

def spam(max):
  for i in range(0,max):
    print(f"""Email {i+1}

Dear {list__of_email[i]}
It has come to our attention that you're missing out on the amazing Replit 100 days of code. We insist you do it right away. If you don't we will pass on your email address to every spammer we've ever encountered and also sign you up to the My Little Pony newsletter, because that's neat. We might just do that anyway.

Love and hugs,

Ian Spammington III""")
    time.sleep(1)
    os.system("cls")
while True:
  print("SPAMMER Inc.")
  menu = input("1: Add email\n2: Remove email\n3: Show emails\n4: Get SPAMMING\n> ")
  if menu == "1":
    email = input("Email > ")
    list__of_email.append(email)
  elif menu== "2":
    email = input("Email > ")
    if email in list__of_email:
      list__of_email.remove(email)
  elif menu == "3":
    pretty_print()
  elif menu =="4":
    spam(10) # ensure to add 10 emails before spamming 
  time.sleep(1)
  os.system("cls")