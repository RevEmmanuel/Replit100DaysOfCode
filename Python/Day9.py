print("What generation are you a part of?: ")
year = int(input("What year were you born? "))
if year <= 1946:
  print("You are a Traditionalist.")
elif year >= 1947 and year <= 1964:
  print("Hey, Baby Boomer! How you doing?")
elif year >= 1965 and year <= 1981:
  print("Gen X! What's up?")
elif year >= 1982 and year <= 1995:
  print("Millenials! The age of tech!")
elif year >= 1996:
  print("Hey, Gen Z! TikTok much?")
else: 
  print("Try again!")
  