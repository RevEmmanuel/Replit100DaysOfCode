
print("STAR WARS NAME GENERATOR")

first_name = input("Enter your first name: > ")
last_name = input("Enter your last name: > ")
mother_maiden_name = input("Enter your mother's maiden name: > ")
city = input("Enter the city you were born in: > ")

name = f"{first_name[:3].title()}{last_name[:3].lower()} {mother_maiden_name[:2].title()}{city[-3:].lower()}"

print(f"Your Star Wars name is {name}")