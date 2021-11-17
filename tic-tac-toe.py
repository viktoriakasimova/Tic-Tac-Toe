from IPython.display import clear_output
from random import randint

def display_board(board):
    # Print out the board
    clear_output()
    print("    ||   ||    ")
    print("  "+board[1]+" || "+board[2]+" || "+board[3]+"  ")
    print("----||---||----")
    print("  "+board[4]+" || "+board[5]+" || "+board[6]+"  ")
    print("----||---||----")
    print("  "+board[7]+" || "+board[8]+" || "+board[9]+"  ")
    print("    ||   ||    ")
    
def player_input():
    
    first_player = "wrong"
    # Keep asking the first player to choose X or O as their marker
    while first_player not in ["X", "O"]:
        first_player = input("Player 1, choose your marker (X/O): ").upper()     
        if first_player not in ["X", "O"]:
            clear_output()
            print("Invalid input. Please choose X or O.")
            
    # Assign the second player a marker
    if first_player == "X":
        second_player = "O"
    else:
        second_player = "X" 
    return(first_player, second_player)

def place_marker(board, marker, position):
    
    # Place a marker on the board
    board[position] = marker
    return board

def win_check(board, mark):
    
    # Check all rows to see if any of them is filled with the same marker
    for i in [1, 4, 7]:
        if board[i] == board[i+1] == board[i+2] == mark:
            return True
    
    # Check all rows to see if any of them is filled with the same marker
    for i in [1, 2, 3]:
        if board[i] == board[i+3] == board[i+6] == mark:
            return True
    
    # Check both diagonals to see if any of them is filled with the same marker
    if (board[1] == board[5] == board[9] == mark) or (board[3] == board[5] == board[7] == mark):
        return True
    return False

def choose_first():
    
    # Choose who goes first
    goes_first = randint(0, 1)
    if goes_first == 0:
        return "Player 1"
    return "Player 2"

def space_check(board, position):
    
    # Check if the position on the board is available
    return board[position] == " "

def full_board_check(board):
    
    # Check if the board is full
    for i in range(1, 10):
        if board[i] == " ":
            return False    
    return True

def player_choice(board):
    
    # Ask a player to choose a position for their marker
    next_position = 0
    while next_position not in range(1,10) or not space_check(board, next_position):
        try:
            next_position = int(input("Choose a position (1-9): "))
        except ValueError:
            print("You need to type a number.")
        if next_position not in range(1,10):
            clear_output()
            print("Invalid input. Please choose position 1-9.")
        if next_position in range(1,10):
            if space_check(board, next_position):
                return next_position
            else:
                clear_output()
                print("Sorry, this position is occupied. Please choose another one.")
                continue


def replay():
    
    # Ask a player if they want to play again
    play = "wrong"
    while play not in ["Yes", "No"]:
        play = input("Do you want to play again (Yes/No)? ").capitalize()
        if play not in ["Yes", "No"]:
            clear_output()
            print("Invalid input. Please choose Yes or No.")        
    return play == "Yes"


print('Welcome to Tic Tac Toe!')
while True:
    
    # Set the game up (dislay the board, players choose markers, define who goes first)
    the_board = [' '] * 10   
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + " will go first.")
    
    # Start the game
    start_game = " "
    while start_game not in ["Yes", "No"]:
        start_game = input("Want to start playing? (Yes/No)? ").capitalize()
        if start_game not in ["Yes", "No"]:
            clear_output()
            print("Invalid input. Please choose Yes or No.")
        elif start_game == "Yes":
            game_on = True
        else:
            game_on = False
            
    while game_on:
            
        # Player 1 turn 
        if turn == "Player 1":
            # Display the board
            display_board(the_board)
            # Choose a  position
            position = player_choice(the_board)
            # Assign the position to the board
            place_marker(the_board, player1_marker, position)
            # Check for a win
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print("Player 1 has won!")    
                break
            # Check for a tie
            if full_board_check(the_board):
                display_board(the_board)
                print("It's a tie!")
                break
            #If not win and not tie, it's Player 2 turn
            turn = "Player 2"
             
        # Player 2 turn
        else:
            # Display the board
            display_board(the_board)
            # Choose a  position
            position = player_choice(the_board)
            # Assign the position to the board
            place_marker(the_board, player2_marker, position)
            # Check for a win
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print("Player 2 has won!")    
                break
            # Check for a tie
            if full_board_check(the_board):
                display_board(the_board)
                print("It's a tie!")
                break
            #If not win and not tie, it's Player 1 turn
            turn = "Player 1"
                
    # Check if players want to play again
    if not replay():
        break
