"""
Purpose: Create a Tic Tac Toe game with a bot that uses the minimax algorithm. The player can choose to play as X or O.
Tools: Numpy, Minimax Algorithm
"""
import numpy as np


# Take side choice
choice = input("Would you like to play as X or O? ")
if choice.upper() == "X":
    player = "X"
    computer = "O"
elif choice.upper() == "O":
    player = "O"
    computer = "X"
else:
    while choice != "X" and choice != "O":
        print("Invalid Input. Try again. ")
        choice = input("Would you like to play as X or O? ")

# Model board so player can input 1-9 for their move
num_board = np.array([["1", "2", "3"],
                  ["4", "5", "6"],
                  ["7", "8", "9"]])

# Actual board for the game
board = np.array([[" ", " ", " "],
                  [" ", " ", " "],
                  [" ", " ", " "]])

scores = {computer: 1, player: -1, "tie": 0}
moves_played = []


# Initialize the game and control the flow
def start_game():
    for i in range(0, 2):
        if player == "X":
            player_turn()
            computer_turn()
        else:
            computer_turn()
            player_turn()

    # Win is possible after 2 moves
    while check_winner() is None:
        if player == "X":
            player_turn()
            # Check for winner after each move
            if check_winner() is not None:
                break
            computer_turn()
            
        else:
            computer_turn()
            # Check for winner after each move
            if check_winner() is not None:
                break
            player_turn()
    
    # Print the result after a winner is found
    if check_winner() == "tie":
        print("Tie Game!")
    else:
        print(check_winner() + " wins!")
    
    
# Player pick their move using the number board. Check if the move is valid and update the board
def player_turn():
    display_board()

    try:
        player_choice = int(input("Where would you like to play? (1-9) "))
        if 0 < player_choice < 10 and valid_move(player_choice):
            play(player_choice, player)
        else:
            raise ValueError("Invalid Input");

    # Catch invalid inputs
    except ValueError:
        print("Invalid move. Try again.")
        player_turn()


# Run the Minimax algorithm on all possible moves and choose the best one
def computer_turn():
    best_score = -1000

    for i in range(0, 3):
        for j in range(0, 3):
            # Run minimax on a valid move
            if board[i, j] == " ":
                board[i, j] = computer
                score = minimax(board, 0, False)
                board[i, j] = " "
                # Choose the best move
                if score > best_score:
                    best_score = score
                    move = [i, j]

    board[move[0], move[1]] = computer


# Minimax algorithm used to determine the best move for the computer by recursively checking all possible moves
# and evaluating the score of each move by "maximizing" the computer's score and "minimizing" the player's score
def minimax(given_board, depth, is_maximizing):
    result = check_winner()
    
    # Check if a board is a terminal state, return the score
    if result is not None:
        return scores[result]
    
    # Maximize the computer's score
    if is_maximizing:
        best_score = -1000
        for i in range(0, 3):
            for j in range(0, 3):
                if given_board[i, j] == " ":
                    given_board[i, j] = computer
                    # Recursively call minimax on the next move
                    score = minimax(given_board, depth + 1, False)
                    given_board[i, j] = " "
                    best_score = max(score, best_score)
        return best_score

    # Minimize the player's score
    else:
        best_score = 1000
        for i in range(0, 3):
            for j in range(0, 3):
                if given_board[i, j] == " ":
                    given_board[i, j] = player
                    # Recursively call minimax on the next move
                    score = minimax(given_board, depth + 1, True)
                    given_board[i, j] = " "
                    best_score = min(score, best_score)
        return best_score


# Check if there are any possible moves left to determine a tie game
def possible_moves():
    count = 0

    for i in range(0,3):
        for j in range(0,3):
            if board[i,j] == " ":
                count += 1
    return count


# Check for 3 in a row to determine a winner
def equals3(a, b, c):
    return a == b and b == c and a != " "


# Check for a winner by checking rows, columns, and diagonals using equals3() and possible_moves()
def check_winner():
    winner = None

    # Check Rows
    for i in range(0, 3):
        if equals3(board[i, 0], board[i, 1], board[i, 2]):
            winner = board[i, 0]

    # Check Columns
    for i in range(0, 3):
        if equals3(board[0, i], board[1, i], board[2, i]):
            winner = board[0, i]

    # Check Diagonals
    if equals3(board[0, 0], board[1, 1], board[2, 2]):
        winner = board[0, 0]
    if equals3(board[2, 0], board[1, 1], board[0, 2]):
        winner = board[2, 0]

    # Check tie
    if winner is None and possible_moves() == 0:
        winner = "tie"

    # Return the winning statement or None
    return winner


# Check if the move is valid
def valid_move(num):
    if num in moves_played:
        return False
    else:
        moves_played.append(num)
        return True


# Convert the player's move from the number board to the actual board
def play(num, user):
    if num == 1:
        board[0, 0] = user
    elif num == 2:
        board[0, 1] = user
    elif num == 3:
        board[0, 2] = user
    elif num == 4:
        board[1, 0] = user
    elif num == 5:
        board[1, 1] = user
    elif num == 6:
        board[1, 2] = user
    elif num == 7:
        board[2, 0] = user
    elif num == 8:
        board[2, 1] = user
    elif num == 9:
        board[2, 2] = user
    else:
        print("Invalid move. Try again.")
        player_turn()


# Display the updated boards and number board for the player
def display_board():
    print(num_board[0, 0] + "|" + num_board[0, 1] + "|" + num_board[0, 2], end="\t")
    print(board[0, 0] + "|" + board[0, 1] + "|" + board[0, 2])
    print("-+-+-", end="\t")
    print("-+-+-")
    print(num_board[1, 0] + "|" + num_board[1, 1] + "|" + num_board[1, 2], end="\t")
    print(board[1, 0] + "|" + board[1, 1] + "|" + board[1, 2])
    print("-+-+-", end="\t")
    print("-+-+-")
    print(num_board[2, 0] + "|" + num_board[2, 1] + "|" + num_board[2, 2], end="\t")
    print(board[2, 0] + "|" + board[2, 1] + "|" + board[2, 2])
    print()

# Start the game and keeping going until user decides to quit
again = True
while again:
    start_game()
    play_again = input("Would you like to play again? (Y/N) ")
    if play_again.upper() == "Y":
        board = np.array([[" ", " ", " "],
                          [" ", " ", " "],
                          [" ", " ", " "]])
        moves_played = []

    else:
        again = False
