def print_board(board):
    """
    Displays the current state of the board.
    """
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print("\n")

def check_winner(board):
    """
    Checks for a winner in rows, columns, and diagonals.
    """
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return board[0][i]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    
    return None

def is_full(board):
    """
    Checks if the board is full.
    """
    return all(cell != " " for row in board for cell in row)

def get_move(player):
    """
    Prompts the current player to make a move.
    """
    while True:
        try:
            move = input(f"Player {player}, enter your move (row and column as 'row,col'): ")
            row, col = map(int, move.split(","))
            if row in range(3) and col in range(3):
                return row, col
            else:
                print("Invalid input. Row and column must be between 0 and 2.")
        except ValueError:
            print("Invalid input format. Please enter row and column as 'row,col'.")

def main():
    # Initialize the board
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    
    while True:
        # Get the player's move
        row, col = get_move(current_player)
        
        # Check if the cell is empty
        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("Cell is already occupied. Try again.")
            continue
        
        # Display the board
        print_board(board)
        
        # Check for a winner
        winner = check_winner(board)
        if winner:
            print(f"Player {winner} wins!")
            break
        
        # Check for a draw
        if is_full(board):
            print("It's a draw!")
            break
        
        # Switch players
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()
