def print_board(board):
    print("Доска:")
    display_board = []
    for i in range(3):
        row = []
        for j in range(3):
            cell = board[i][j]
            row.append(cell if cell != " " else str(i * 3 + j + 1))
        display_board.append(" | ".join(row))
    print("\n".join(display_board))
    print("-" * 9)