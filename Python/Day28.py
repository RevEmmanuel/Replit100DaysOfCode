import random, os, time, math

def roll_dice(side):
    result = random.randint(1,side)
    return result

def get_health():
    return ((roll_dice(6) * roll_dice(12)) / 2) + 10

def get_strength():
    return (roll_dice(6) * roll_dice(8)) / 2 + 12

def create_character():
    name = input("Name your Legend:\n")
    type = input("Character Type (Human, Elf, Wizard, Orc):\n")
    return name, type

def display_details(name, health, strength):
    print()
    print(name)
    print("HEALTH:", health)
    print("STRENGTH:", strength, "\n")

def determine_blow(strength_1, second_strength):
    return abs(strength_1 - second_strength)

def determine_who_plays():
    value_1, value_2 = roll_dice(6), roll_dice(6)
    while value_1 == value_2:
        value_1, value_2 = roll_dice(6), roll_dice(6)
    else:
        return value_1, value_2

def start():
    import time
    print("\033[?25l", end="")
    print("⚔️ CHARACTER BUILDER ⚔️")
    time.sleep(1)
    print()
    name, type = create_character()
    health = get_health()
    strength = get_strength()
    display_details(name, health, strength)
    print("Who are they battling?\n")
    name_2, type_2 = create_character()
    second_health = round(get_health(), 0)
    second_strength = round(get_strength(), 0)
    display_details(name_2, second_health, second_strength)
    time.sleep(1)
    os.system("cls")
    time.sleep(1)
    number_of_rounds = 0
    blow_to_be_dealt = determine_blow(strength, second_strength)
    print("⚔️ Let the battle begin!!!! ⚔️")
    time.sleep(4)
    while health != 0 and second_health != 0:
        number_of_rounds += 1
        os.system("cls")
        time.sleep(1)
        print("⚔️ Battle Continues ⚔️")
        print("Round", number_of_rounds)
        player_1_number, player_2_number = determine_who_plays()
        time.sleep(1)
        if player_1_number > player_2_number:
            print(name, "wins round", number_of_rounds)
            print(name_2, "takes a hit with", blow_to_be_dealt, "damage")
            second_health -= blow_to_be_dealt
        else:
            print(name_2, "wins round", number_of_rounds)
            print(name, "takes a hit with", blow_to_be_dealt, "damage")
            health -= blow_to_be_dealt
        time.sleep(1)
        display_details(name, health, strength)
        display_details(name_2, second_health, second_strength)
        time.sleep(1)
        if health <= 0:
            print("Oh  no,", name, "the", type_2, "has died")
            time.sleep(2)
            os.system("cls")
            print("⚔️ Winner winner! ⚔️")
            time.sleep(1)
            print(name_2, "the", type_2, "destroyed", name, "after", number_of_rounds, "rounds")
            break
        elif second_health <= 0:
            print("Oh no,", name_2, "the", type_2, "has died")
            time.sleep(2)
            os.system("cls")
            print("⚔️ Winner winner! ⚔️")
            time.sleep(1)
            print(name, "the", type, "destroyed", name_2, "after", number_of_rounds, "rounds")
            break
        else:
            print("And they're both standing for the next round!")
            time.sleep(1)
        if number_of_rounds == 5:
            print("After", number_of_rounds, "rounds,", "it ends in a draw!!!")
            break

while True:
    start()
    again = input("Again?:\n")
    if again == "No" or again == "no":
        exit()
    time.sleep(1)
    os.system("cls")