import random
options_to_pick_from = ['ROCK', 'PAPER', 'SCISSORS']


def decide_win(player_1, player_2):
    if player_1 in options_to_pick_from and player_2 in options_to_pick_from:
        print(f'Player_1 choice is {player_1}')
        print(f'Player_2 choice is {player_2}')
        if player_1 == player_2:
            print('Game ends in a draw.')
            return "DD"
        elif player_1 == 'ROCK' and player_2 == 'PAPER':
            print('Player 2 wins!')
            return "P2"
        elif player_1 == 'PAPER' and player_2 == 'ROCK':
            print('Player 1 wins!')
            return "P1"
        elif player_1 == 'SCISSORS' and player_2 == 'ROCK':
            print('Player 2 wins!')
            return "P2"
        elif player_1 == 'ROCK' and player_2 == 'SCISSORS':
            print('Player 1 wins!')
            return "P1"
        elif player_1 == 'PAPER' and player_2 == 'SCISSORS':
            print('Player 2 wins!')
            return "P2"
        elif player_1 == 'SCISSORS' and player_2 == 'PAPER':
            print('Player 1 wins!')
            return "P1"
    else:
        print('Enter rock, paper, or scissors.')


if __name__ == '__main__':
    player_1_wins = 0
    player_2_wins = 0
    number_of_players = int(input("Press 1 for Computer and 2 for multiplayer: "))
    if number_of_players == 1:
        while player_1_wins != 3 and player_2_wins != 3:
            player_choice = input('Pick rock, paper, or scissors: ')
            print("Player 2 is computer")
            computer_choice = random.choice(options_to_pick_from)
            player_choice = player_choice.upper()
            winner = decide_win(player_choice, computer_choice)
            if winner == "P1":
                player_1_wins += 1
            elif winner == "P2":
                player_2_wins += 1
            else:
                continue
        else:
            if player_1_wins == 3:
                print("Player 1 wins!")
                print("Score is", player_1_wins, "to", player_2_wins)
            elif player_2_wins == 3:
                print("Player 2 wins!")
                print("Score is", player_2_wins, "to", player_1_wins)
    elif number_of_players == 2:
        while player_1_wins != 3 and player_2_wins != 3:
            player_1_choice = input("Pick rock, paper, or scissors: ")
            player_1_choice = player_1_choice.upper()
            player_2_choice = input("Pick rock, paper, or scissors: ")
            player_2_choice = player_2_choice.upper()
            who_won = decide_win(player_1_choice, player_2_choice)
            if who_won == "P1":
                player_1_wins += 1
            elif who_won == "P2":
                player_2_wins += 1
            else:
                continue
        else:
            if player_1_wins == 3:
                print("Player 1 wins!")
                print("Score is", player_1_wins, "to", player_2_wins)
            elif player_2_wins == 3:
                print("Player 2 wins!")
                print("Score is", player_2_wins, "to", player_1_wins)
    else:
        print("Invalid choice. Enter 1 or 2")
