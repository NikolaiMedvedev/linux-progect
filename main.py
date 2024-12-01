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

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Игрок {current_player}, введите номер клетки (1-9): ")

        try:
            cell = int(input())

            if cell < 1 or cell > 9:
                print("Неверный номер клетки. Попробуйте еще раз.")
                continue

            row, col = divmod(cell - 1, 3)

            if board[row][col] != " ":
                print("Эта клетка уже занята. Попробуйте другую.")
                continue