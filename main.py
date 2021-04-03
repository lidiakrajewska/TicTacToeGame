# A complete Tic Tac Toe Game
import re


def main():
    # Give info about game and get users' names
    print("Hi! Let's play Tic Tac Toe game!")
    p_1_name = input("Player 1 name: ")
    p_2_name = input("Player 2 name: ")

    # Users decide on symbols
    p_1_symbol = choose_symbol(p_1_name)
    # Player 2 gets the remaining symbol
    if p_1_symbol == "x":
        p_2_symbol = "o"
    else:
        p_2_symbol = "x"

    # Set users' scores
    p_1_score = 0
    p_2_score = 0

    while True:
        # One tally of the game
        tally_winner = tally(p_1_name, p_1_symbol, p_2_name, p_2_symbol)

        # Update scores after each tally
        if tally_winner == p_1_name:
            p_1_score += 1
            print(f"{p_1_name} won this tally.")
        elif tally_winner == p_2_name:
            p_2_score += 1
            print(f"{p_2_name} won this tally.")
        else:
            print("This tally has no winner.")

        # Ask if users want to play again
        again = repeat()
        # If users want to play another tally, start a new one
        if again == 1:
            continue
        # If users don't want to play again, quit
        elif again == 0:
            overall_winner(p_1_name, p_1_score, p_2_name, p_2_score)
            break


# Get a valid symbol for the user
def choose_symbol(p_name):
    while True:
        p_symbol = input(f"{p_name}'s symbol (x/o): ")
        if p_symbol.lower() == "x":
            return "x"
        elif p_symbol.lower() == "o":
            return "o"
        else:
            print("Incorrect symbol. You can only use 'x' or 'o'")


# Printing a whole clear game board
def draw(game):
    for n in range(3):
        horizontal()
        print()
        vertical(game, n)
        print()
    horizontal()
    print()


# Printing -----
def horizontal():
    for x in range(3):
        print(" ", end='')
        for y in range(3):
            print("-", end='')
    print(" ", end='')


# Printing | | | and symbols
def vertical(game, row):
    for x in range(3):
        print("|", end='')
        if game[row][x] == 0:
            print(" " * 3, end='')
        elif game[row][x] == "x":
            print(" ", end='')
            print("x", end='')
            print(" ", end='')
        else:
            print(" ", end='')
            print("o", end='')
            print(" ", end='')
    print("|", end='')


# One tally of the game
def tally(p_1_name, p_1_symbol, p_2_name, p_2_symbol):
    # Prepare a clear game board
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    draw(game)
    zeros = 9
    won = 0
    print("Each player has to give coordinates for their move (row,column). Indices starting at 1.")

    # Ask users for next move as long as it's possible and no one has won yet
    while zeros > 1 and won == 0:

        # Player 1 move
        while won == 0:
            pl_1 = input(f"{p_1_name}:")
            p_1_move = pl_1.split(",")

            # If move is possible check if it leads to win
            if move(game, p_1_move, p_1_symbol):
                won = winner(game, p_1_name, p_1_symbol, p_2_name)
                break

        # Player 2 move
        while won == 0:
            pl_2 = input(f"{p_2_name}: ")
            p_2_move = pl_2.split(",")

            # If move is possible check if it leads to win
            if move(game, p_2_move, p_2_symbol):
                won = winner(game, p_1_name, p_1_symbol, p_2_name)
                break

        # Show current board state
        draw(game)

        # Update number of available moves
        zeros -= 2

    # Return winner (if is any)
    return won


# Placing xs and os
def move(game, coordinates, symbol):
    # Extract coordinates (x - row, y - column)
    x = int(coordinates[0]) - 1
    y = int(coordinates[1]) - 1

    # Save move, if possible
    if x in range(3) and y in range(3):
        if game[x][y] == 0:
            game[x][y] = symbol
            return True

    print("Move impossible")
    return False


# Check if there's a winner
def winner(game, p_1_name, p_1_symbol, p_2_name):
    hor = horizontal_win(game)
    if hor != 0:
        if hor == p_1_symbol:
            return p_1_name
        else:
            return p_2_name

    ver = vertical_win(game)
    if ver != 0:
        if ver == p_1_symbol:
            return p_1_name
        else:
            return p_2_name

    diag = diagonal_win(game)
    if diag != 0:
        if diag == p_1_symbol:
            return p_1_name
        else:
            return p_2_name

    return 0


# Horizontal winner check
def horizontal_win(game):
    for n in range(3):
        if game[n][0] == game[n][1] == game[n][2] != 0:
            return game[n][0]

    return 0


# Vertical winner check
def vertical_win(game):
    for n in range(3):
        if game[0][n] == game[1][n] == game[2][n] != 0:
            return game[0][n]

    return 0


# Diagonal winner check
def diagonal_win(game):
    d_1 = game[0][0] == game[1][1] == game[2][2] != 0
    d_2 = game[0][2] == game[1][1] == game[2][0] != 0
    if d_1:
        return game[0][0]
    elif d_2:
        return game[0][2]

    return 0


# Check if players want to play again
def repeat():
    again = input("Do you want to play again? (y/n)")
    while True:
        if re.search("y(es)?", again, re.IGNORECASE):
            print("Let's start then!")
            return 1
        elif re.search("n(o)?", again, re.IGNORECASE):
            print("Ok, let's show you your scores.")
            return 0
        else:
            print("Incorrect answer.")
            again = input("Make up your mind... : ")


# Check who won overall
def overall_winner(p_1_name, p_1_score, p_2_name, p_2_score):
    # Show points to players
    print(f"{p_1_name}'s score: {p_1_score}, {p_2_name}'s score: {p_2_score}.")

    # Print congrats
    if p_1_score > p_2_score:
        print(f"Congrats to {p_1_name}!")
    elif p_2_score > p_1_score:
        print(f"Congrats to {p_2_name}!")
    else:
        print(f"Congrats to both of of you! It's a draw.")


if __name__ == '__main__':
    main()
