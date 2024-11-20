class Board:
    """Класс, который описывает игровое поле."""

    # Размер поля
    field_size = 3

    def __init__(self):
        # Создает пустое поле
        self.board = [
            [" " for _ in range(self.field_size)] for _ in range(self.field_size)
        ]

    def make_move(self, row, col, player):
        """Метод для выполнения хода."""
        self.board[row][col] = player

    def is_board_full(self):
        """Метод для проверки, заполнено ли поле полностью."""

        # Если на поле есть хотя бы одна пустая клетка (" "), возвращает False.
        for i in range(self.field_size):
            for j in range(self.field_size):
                if self.board[i][j] == " ":
                    return False
        return True

    def check_win(self, player):
        """Метод для проверки выйграл ли игрок."""
        # Проверка строк и столбцов на совпадение всех клеток с символом игрока
        for i in range(3):
            if all([self.board[i][j] == player for j in range(3)]) or all(
                [self.board[j][i] == player for j in range(3)]
            ):
                return True
        # Проверка диагоналей на совпадение всех клеток с символом игрока
        if (
            self.board[0][0] == self.board[1][1] == self.board[2][2] == player
            or self.board[0][2] == self.board[1][1] == self.board[2][0] == player
        ):
            return True

        return False
