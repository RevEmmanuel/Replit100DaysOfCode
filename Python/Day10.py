bill = float(input("What was the bill?: "))
number_of_people = int(input("How many people?: "))
tip = int(input("What percent tip do you want to leave: 15, 18, or 20 percent?"))


bill_with_tip = tip / 100 * bill + bill
bill_per_person = bill_with_tip / number_of_people
final_amount = round(bill_per_person, 2)


print("You all owe", final_amount, "each")
