# Сделал доску
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


# Сделал проверку на победителей
def check_winner(board):
    # Проверка строк
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]

    # Проверка столбцов
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    # Проверка диагоналей
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None
