import random
options_to_pick_from = ['ROCK', 'PAPER', 'SCISSORS']


def decide_win(player_1, player_2):
    if player_1 in options_to_pick_from and player_2 in options_to_pick_from:
        print(f'Player_1 choice is {player_1}')
        print(f'Player_2 choice is {player_2}')
        if player_1 == player_2:
            print('Game ends in a draw.')
        elif player_1 == 'ROCK' and player_2 == 'PAPER':
            print('Player 2 wins!')
        elif player_1 == 'PAPER' and player_2 == 'ROCK':
            print('Player 1 wins!')
        elif player_1 == 'SCISSORS' and player_2 == 'ROCK':
            print('Player 2 wins!')
        elif player_1 == 'ROCK' and player_2 == 'SCISSORS':
            print('Player 1 wins!')
        elif player_1 == 'PAPER' and player_2 == 'SCISSORS':
            print('Player 2 wins!')
        elif player_1 == 'SCISSORS' and player_2 == 'PAPER':
            print('Player 1 wins!')
    else:
        print('Enter rock, paper, or scissors.')


if __name__ == '__main__':
    number_of_players = int(input("Press 1 for Computer and 2 for multiplayer: "))
    if number_of_players == 1:
        player_choice = input('Pick rock, paper, or scissors: ')
        print("Player 2 is computer")
        computer_choice = random.choice(options_to_pick_from)
        player_choice = player_choice.upper()
        decide_win(player_choice, computer_choice)
    elif number_of_players == 2:
        player_1_choice = input("Pick rock, paper, or scissors: ")
        player_1_choice = player_1_choice.upper()
        player_2_choice = input("Pick rock, paper, or scissors: ")
        player_2_choice = player_2_choice.upper()
        decide_win(player_1_choice, player_2_choice)
    else:
        print("Invalid choice. Enter 1 or 2")
