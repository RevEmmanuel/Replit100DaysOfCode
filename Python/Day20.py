print("List Generator")
print()

start = int(input("Start at: >"))
stop = int(input("End before: >"))
increment = int(input("Increment between values: >"))
print()

for i in range(start, stop, increment):
    print(i)