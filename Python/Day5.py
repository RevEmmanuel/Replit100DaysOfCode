print("Marvel Movie Character Creator")
print("---")
print()
hang_around = input("Do you like 'hanging around'?: ")
if hang_around == "No" or hang_around == "no":
    print("Then you're not Spider-man")
    gravelly_voice = input("Do you have a 'gravelly' voice?: ")
    if gravelly_voice == "No" or gravelly_voice == "no":
        print("Aww, then you're not Korg")
        marvelous = input("Do you often feel marvelous?: ")
        if marvelous == "No" or marvelous == "no":
            name = input("Then who are you?!!")
            print("Oh, hi", name)
        else:
            print("Aha! You are Captain Marvel! Hi!")
    else:
        print("Nice to meet you, Korg!")
else:
    print("Hi, Peter Parker")