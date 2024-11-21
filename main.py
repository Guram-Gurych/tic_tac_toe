import os
import pygame

# Импортируем собственный класс Board и константыguram из модуля gameparts
from gameparts import (
    Board,
    CELL_SIZE,
    BOARD_SIZE,
    WIDTH,
    HEIGHT,
    LINE_WIDTH,
    BG_COLOR,
    LINE_COLOR,
    X_COLOR,
    O_COLOR,
    X_WIDTH,
    O_WIDTH,
    SPACE,
)

# Скрываем приветственное сообщение Pygame
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
# Инициализируем библиотеку Pygame
pygame.init()

# Создаем и настраиваем окно игры
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Крестики-нолики")
screen.fill(BG_COLOR)


def draw_lines():
    """Функция для рисования линий игрового поля."""

    for i in range(1, BOARD_SIZE):
        pygame.draw.line(
            screen, LINE_COLOR, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), LINE_WIDTH
        )
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(
            screen, LINE_COLOR, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), LINE_WIDTH
        )


def draw_figures(board):
    """Функция для отображения крестиков и ноликов на игровом поле."""
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == "X":
                # Рисуем крестик с двумя линиями
                pygame.draw.line(
                    screen,
                    X_COLOR,
                    (col * CELL_SIZE + SPACE, row * CELL_SIZE + SPACE),
                    (
                        col * CELL_SIZE + CELL_SIZE - SPACE,
                        row * CELL_SIZE + CELL_SIZE - SPACE,
                    ),
                    X_WIDTH,
                )
                pygame.draw.line(
                    screen,
                    X_COLOR,
                    (col * CELL_SIZE + SPACE, row * CELL_SIZE + CELL_SIZE - SPACE),
                    (col * CELL_SIZE + CELL_SIZE - SPACE, row * CELL_SIZE + SPACE),
                    X_WIDTH,
                )
            elif board[row][col] == "O":
                # Рисуем нолик
                pygame.draw.circle(
                    screen,
                    O_COLOR,
                    (
                        col * CELL_SIZE + CELL_SIZE // 2,
                        row * CELL_SIZE + CELL_SIZE // 2,
                    ),
                    CELL_SIZE // 2 - SPACE,
                    O_WIDTH,
                )


def save_result(result):
    """Функция для сохранения результата игры в файл."""
    with open("results.txt", "a", encoding="utf-8") as f:
        f.write(result + "\n")


def main():
    """Главная функция игры."""
    game = Board()
    current_player = "X"  # Первый ход делает игрок с крестиками
    running = True
    draw_lines()  # Рисуем линии игрового поля

    while running:
        # Обрабатываем события
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Событие закрытия окна
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:  # Событие нажатия на мышь
                mouse_y = event.pos[0]
                mouse_x = event.pos[1]

                clicked_row = mouse_x // CELL_SIZE
                clicked_col = mouse_y // CELL_SIZE

                # Если кликнули по пустой клетке
                if game.board[clicked_row][clicked_col] == " ":
                    game.make_move(
                        clicked_row, clicked_col, current_player
                    )  # Делаем ход

                    if game.check_win(
                        current_player
                    ):  # Проверяем, выиграл ли текущий игрок
                        result = f"Победили {current_player}."
                        print(result)
                        save_result(result)
                        running = False  # Завершаем игру
                    elif game.is_board_full():  # Проверяем, заполнено ли поле полностью
                        result = "Ничья!"
                        print(result)
                        save_result(result)
                        running = False  # Завершаем игру

                    # Меняем текущего игрока
                    current_player = "O" if current_player == "X" else "X"
                    draw_figures(game.board)  # Обновляем экран

        pygame.display.update()  # Обновляем окно игры

    pygame.quit()  # Завершаем работу


# Сам запуск программы
if __name__ == "__main__":
    main()
