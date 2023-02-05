name = input("Name: ").strip().capitalize()
date_of_birth = input("Date of Birth: ").strip()
telephone_number = input("Telephone number: ").strip()
email = input("Email: ")
address = input("Address: ")
contact = {"name": name, "date_of_birth": date_of_birth, "telephone_number": telephone_number, "email": email, "address": address}

print()
print(f"""Name: {contact["name"]}""")
print(f"""DOB: {contact["date_of_birth"]}""")
print(f"""Tel: {contact["telephone_number"]}""")
print(f"""Email: {contact["email"]}""")
print(f"""Address: {contact["address"]}""")