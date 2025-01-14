import time

board = [["-" for _ in range(3)] for _ in range(3)]

def show_board():
    for row in board:
        print(" ".join(row))
    print()

def check_winner():
    for row in board:
        if row[0] == row[1] == row[2] != "-":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "-":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != "-":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "-":
        return board[0][2]
    return None

def player_move():
    while True:
        try:
            row, column = map(int, input("Enter row and column (1-3): ").split())
            row -= 1
            column -= 1
            if board[row][column] == "-":
                board[row][column] = "X"
                break
            else:
                print("This spot is taken! Choose another one.")
        except (ValueError, IndexError):
            print("Invalid input! Please enter a number between 1 and 3.")

def computer_move():
    for row in range(3):
        for column in range(3):
            if board[row][column] == "-":
                board[row][column] = "O"
                return

show_board()
while True:
    player_move()
    show_board()
    winner = check_winner()
    if winner:
        print(f"{winner} wins!")
        break

    time.sleep(1)

    computer_move()
    show_board()
    winner = check_winner()
    if winner:
        print(f"{winner} wins!")
        break

    if all(board[row][column] != "-" for row in range(3) for column in range(3)):
        print("It's a tie!")
        break

# MADE BY KEMAL DENİZ TAŞTAN 2025
