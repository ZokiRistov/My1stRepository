
"""Tic Tac Toe Game"""

game_state = True

the_game_board = [' ']*9

player_1 = ''
player_2 = ''

play_again_response = ""

def reset_board():
    """Resets the board"""

    global the_game_board, game_state

    the_game_board = [' ']*9
    game_state = True

def display_board(board):
    """Displays the board in its current condition"""

    print("\n"*10)

    print(board[0] + " | " + board[1] + " | " + board[2]
          + "\n---------\n" +
          board[3] + " | " + board[4] + " | " + board[5]
          + "\n---------\n" +
          board[6] + " | " + board[7] + " | " + board[8])

def check_for_win(board, player):
    """Checks to see if a player has won"""

    return (board[0] == board[1] == board[2] == player) or \
           (board[0] == board[3] == board[6] == player) or \
           (board[0] == board[4] == board[8] == player) or \
           (board[1] == board[4] == board[7] == player) or \
           (board[2] == board[5] == board[8] == player) or \
           (board[2] == board[4] == board[6] == player) or \
           (board[3] == board[4] == board[5] == player) or \
           (board[6] == board[7] == board[8] == player)

def check_if_board_is_full(board):
    """If there are any blank spaces in the board, returns False, otherwise returns True, meaning the board is full"""

    return not ' ' in board[1:]

def assign_mark_to_players():
    """Randomly assigns the X and O marks to the players"""

    global player_1, player_2

    ask = "Which marker would you like? : "

    cond = True
    while cond:
        try:
            choice = str (input(ask))

            if choice != 'X' and choice != 'O':
                print("Please enter 'X' or 'O'")
                continue

            else:
                cond = False
                player_1 = choice

        except(ValueError):
            print ("Please enter 'X' or 'O'")
            continue

    if player_1 == 'X': player_2 = 'O'
    else: player_2 = 'X'

    return player_1, player_2


def place_marker(marker):
    """Places a mark on a chosen position by the player"""

    global the_game_board

    ask = "Where do you wanna place your mark " + marker + "? : "

    cond = True
    while cond:

        try:
            choice = int (input(ask))

            if choice != 1 and choice != 2 and choice != 3 and choice != 4 and \
               choice != 5 and choice != 6 and choice != 7 and choice != 8 and choice != 9:

                print ("You must input an integer from 1 to 9. Try again")
                continue

            else: cond = False

        except ValueError:
            print ("Wrong input. You must input an integer from 1 to 9. Try again")
            continue

    if the_game_board[choice - 1] == ' ': the_game_board[choice - 1] = marker

    else:
        print ("The position is taken. Choose another position")
        place_marker(marker)


    return the_game_board, marker



def play_again():
    """Ask to play again"""

    global play_again_response

    while not (play_again_response == "y" or play_again_response == "n"):
        play_again_response = input("Would you like to play again? Please answer with 'y' or 'n'': ")

    else:
        return play_again_response


def play_game():

    global the_game_board, game_state, player_1, player_2

    print("The game starts now")

    counter = 0

    assign_mark_to_players()

    while game_state:

        counter += 1

        display_board(the_game_board)

        if counter%2 == 1:
            place_marker(player_1)
            if not game_state:
                break

        if counter%2 == 0:
            place_marker(player_2)
            if not game_state:
                break

        if check_for_win(the_game_board, player_1):
            game_state = False
            print("Player with mark " + player_1 + " has won!")
            play_again()

        if check_for_win(the_game_board, player_2):
            game_state = False
            print("Player with mark " + player_2 + " has won!")
            play_again()

        if check_if_board_is_full(the_game_board) and not ( check_for_win(the_game_board, player_1) or check_for_win(the_game_board, player_2) ):
            game_state = False
            print("There are no places left on the board. No one has won, the game is a tie.")
            play_again()


    if play_again_response == 'y':
        reset_board()
        game_state = True
        play_game()

    if play_again_response == 'n':
        print ("Bye :)")
        exit(0)


play_game()