def display_board(board):
    print("\n")
    for i in range(3):
        print("       " + " | ".join(board[i]))
        if i < 2:
            print("      ---+---+---")
    print()


def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True

        if all(board[j][i] == player for j in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def board_full(board):
    return all(cell != " " for row in board for cell in row)


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("=" * 35)
    print("          TIC-TAC-TOE")
    print("            1WN24CS158")
    print("=" * 35)
    print("Instructions: Enter row and column (1-3).")
    print("Player X goes first, followed by Player O.")

    while True:
        display_board(board)

        try:
            row = int(input(f"Player {current_player}, enter row (1-3): "))
            col = int(input(f"Player {current_player}, enter column (1-3): "))

            if row not in range(1, 4) or col not in range(1, 4):
                print("\nInvalid position! Choose numbers from 1 to 3.")
                continue

            row -= 1
            col -= 1

            if board[row][col] != " ":
                print("\nThat cell is already occupied! Try again.")
                continue

            board[row][col] = current_player

            if check_winner(board, current_player):
                display_board(board)
                print("=" * 35)
                print(f"       PLAYER {current_player} WINS!")
                print("=" * 35)
                break

            if board_full(board):
                display_board(board)
                print("=" * 35)
                print("             IT'S A DRAW!")
                print("=" * 35)
                break

            current_player = "O" if current_player == "X" else "X"

        except ValueError:
            print("\nInvalid input! Please enter numbers only.")


if __name__ == "__main__":
    main()