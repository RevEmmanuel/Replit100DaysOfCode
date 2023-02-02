import os, time, playsound

while True:
    print("My POD Music Player")
    time.sleep(1)
    os.system("cls")
    print("Press anything else to view the menu option again OR")
    time.sleep(1)
    choice = int(input("Press 1 to Play \nPress 2 to exit: \n"))
    if choice == 2:
        exit()
    elif choice == 1:
        print("Playing some proper tunes!")
        playsound.playsound("Asake - Yoga (Official Video).mp3")
        if (int(input("Press 2 to exit: \n")) == 2):
            exit()
    else:
        os.system("cls")
        continue
