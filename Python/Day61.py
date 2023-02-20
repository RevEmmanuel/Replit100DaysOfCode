import os, datetime, time

tweets_list = []
try:
    with open("tweets", "x") as file:
        file = open("tweets", "r")
        data = file.read()
        tweets_list = eval(data)
        file.close()
except FileExistsError:
    with open("tweets", "r") as file:
        data = file.read()
        tweets_list = eval(data)
        file.close()

def add_tweet():
    the_tweet = input("Enter the tweet : > ").strip()
    time_created = datetime.datetime.now()
    new_tweet = {time_created : the_tweet}
    tweets_list.append(new_tweet)
    print("Added tweet")
    time.sleep(1)
    os.system("cls")

def view_tweets():
    count = 0
    for a_tweet in tweets_list[::-1]:
        if count != 0:
            if count % 10 == 0:
                time.sleep(2)
                os.system("cls")
                if (input("Do you want to see another 10 tweets? (y/n): ") == "n"):
                    time.sleep(3)
                    os.system("cls")
                    main_menu()
            else:
                time.sleep(1)
                print(a_tweet)
        else:
            print(a_tweet)
        count += 1
    time.sleep(2)
    os.system("cls")


def main_menu():
    os.system("cls")
    while True:
        choice = input("1. Add tweets \n2. View tweets \nElse: Exit\n")
        if choice == "1":
            add_tweet()
        elif choice == "2":
            view_tweets()
        else:
            break
    f = open("tweets", "w")
    f.write(str(tweets_list))
    f.close()

main_menu()
time.sleep(3)
os.system("cls")
print("Thanks for using our Twitter")