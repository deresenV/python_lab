import tkinter as tk
from tkinter import messagebox, simpledialog
import random

TIMER_DEFAULT = 10        # Таймер по умолчанию (в секундах)
MIN_BOARD_SIZE = 3
MAX_BOARD_SIZE = 7
BOARD_SIZE_DEFAULT = 5    # Размер поля
CELL_SIZE_DEFAULT = 85    # Размер одной клетки в пикселях

def template_random_walk(size):
    """
    Генерация пути
    """
    path = []
    visited = set()
    stack = [(0, 0)]  # Начинаем с левого верхнего угла

    while stack:
        r, c = stack.pop()
        if (r, c) not in visited:
            visited.add((r, c))
            path.append((r, c))
            # Соседи в случайном порядке
            neighbors = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
            random.shuffle(neighbors)
            for nr, nc in neighbors:
                if 0 <= nr < size and 0 <= nc < size and (nr, nc) not in visited:
                    stack.append((nr, nc))
    return path

class Tile:
    """
    Описывает одну клетку на поле. У клетки есть тип и ориентация.
    Типы: 'vertical', 'horizontal', 'corner'.
    Ориентация: 0 (стандартная), 1 (90°), 2 (180°), 3 (270°).
    """
    def __init__(self, shape_type, orientation=0):
        self.shape_type = shape_type  # Тип клетки
        self.orientation = orientation  # Угол поворота

    def rotate(self):
        """Вращает клетку на 90° по часовой стрелке."""
        self.orientation = (self.orientation + 1) % 4

    def get_dirs(self):
        """
        Определяет, куда ведут соединения клетки с учётом её поворота.
        Возвращает set с направлениями ('up', 'right', 'down', 'left').
        """
        # Определяем базовые направления для каждого типа
        if self.shape_type == 'vertical':
            dirs = {'up', 'down'}
        elif self.shape_type == 'horizontal':
            dirs = {'left', 'right'}
        elif self.shape_type == 'corner':
            dirs = {'up', 'right'}  # Угол «┏» в стандартной ориентации
        else:
            dirs = set()

        # Поворачиваем направления в зависимости от ориентации
        rotation_map = {
            'up': 'right',
            'right': 'down',
            'down': 'left',
            'left': 'up'
        }

        for _ in range(self.orientation):
            dirs = {rotation_map.get(d, d) for d in dirs}

        return dirs


class Board:
    """
    Класс для управления игровым полем. Генерирует поле и проверяет его состояние.
    """
    def __init__(self, size):
        self.size = size
        self.grid = [[None for _ in range(size)] for _ in range(size)]
        # Решённая конфигурация
        self.solved_grid = [[None for _ in range(size)] for _ in range(size)]

    def create_and_shuffle(self):
        """
        Создаёт решённую конфигурацию и перемешивает блоки.
        """
        while True:
            # Шаг 1: Генерируем путь
            path = template_random_walk(self.size)

            # Шаг 2: Создаём связи между клетками
            neighbors = {(r, c): [] for r in range(self.size) for c in range(self.size)}
            for i in range(len(path) - 1):
                r1, c1 = path[i]
                r2, c2 = path[i + 1]
                neighbors[(r1, c1)].append((r2, c2))
                neighbors[(r2, c2)].append((r1, c1))

            # Шаг 3: Настраиваем блоки
            for r in range(self.size):
                for c in range(self.size):
                    nb = neighbors[(r, c)]
                    dirs = set()
                    for (nr, nc) in nb:
                        if nr == r - 1:
                            dirs.add('up')
                        elif nr == r + 1:
                            dirs.add('down')
                        elif nc == c - 1:
                            dirs.add('left')
                        elif nc == c + 1:
                            dirs.add('right')

                    shape, rot = self._pick_block(dirs)
                    self.solved_grid[r][c] = Tile(shape, rot)

            # Шаг 4: Копируем в grid для проверки
            for r in range(self.size):
                for c in range(self.size):
                    self.grid[r][c] = Tile(
                        self.solved_grid[r][c].shape_type,
                        self.solved_grid[r][c].orientation
                    )

            # Шаг 5: Проверяем проходимость
            if self.is_solved():
                break

        # Шаг 6: Перемешиваем
        for r in range(self.size):
            for c in range(self.size):
                rand_rot = random.randint(0, 3)
                for _ in range(rand_rot):
                    self.grid[r][c].rotate()

    def _pick_block(self, dirs):
        """
        Выбирает тип блока и поворот на основе требуемых направлений.
        """
        shapes = [
            ('horizontal', {'left', 'right'}),
            ('vertical',   {'up', 'down'}),
            ('corner',     {'up', 'right'})
        ]
        rot_map = {
            'up': 'right',
            'right': 'down',
            'down': 'left',
            'left': 'up'
        }

        for shape, base in shapes:
            for rot in range(4):
                test = set(base)
                for _ in range(rot):
                    test = {rot_map[d] for d in test}

                if test.issuperset(dirs):
                    return shape, rot

        return 'vertical', 0

    def get_lit(self):
        """
        Возвращает список освещённых клеток.
        """
        if self.size == 0:
            return set()

        lit = set()
        queue = [(0, 0)]
        lit.add((0, 0))

        while queue:
            r, c = queue.pop(0)
            current = self.grid[r][c].get_dirs()
            for (nr, nc) in self._neighbors(r, c):
                neighbor = self.grid[nr][nc].get_dirs()
                dir_to = self._dir(r, c, nr, nc)
                dir_from = self._dir(nr, nc, r, c)
                if dir_to in current and dir_from in neighbor:
                    if (nr, nc) not in lit:
                        lit.add((nr, nc))
                        queue.append((nr, nc))
        return lit

    def is_solved(self):
        """Проверяет, все ли клетки освещены."""
        return len(self.get_lit()) == self.size * self.size

    def _neighbors(self, r, c):
        """Возвращает соседей клетки (r, c), проверяя границы поля."""
        neighbors = []
        if r > 0:
            neighbors.append((r - 1, c))  # Верхний сосед
        if r < self.size - 1:
            neighbors.append((r + 1, c))  # Нижний сосед
        if c > 0:
            neighbors.append((r, c - 1))  # Левый сосед
        if c < self.size - 1:
            neighbors.append((r, c + 1))  # Правый сосед
        return neighbors

    def _dir(self, r1, c1, r2, c2):
        """
        Возвращает направление из (r1, c1) в (r2, c2).
        """
        if r2 == r1 - 1 and c2 == c1:
            return 'up'
        if r2 == r1 + 1 and c2 == c1:
            return 'down'
        if c2 == c1 - 1 and r2 == r1:
            return 'left'
        if c2 == c1 + 1 and r2 == r1:
            return 'right'
        return None


class Game:
    """
    Управляет игровым процессом, интерфейсом и таймером.
    """
    def __init__(self, board_size=BOARD_SIZE_DEFAULT, timer_seconds=TIMER_DEFAULT, cell_size=CELL_SIZE_DEFAULT):
        """
        Инициализация игры.
        """
        self.board_size = board_size
        self.timer_seconds = timer_seconds
        self.cell_size = cell_size

        self.root = tk.Tk()
        self.root.title("Light'em Up! New Design")
        self.root.configure(bg='black')

        self.board = Board(self.board_size)
        self.board.create_and_shuffle()

        self.time_left = self.timer_seconds
        self.game_over = False

        self.canvases = [[None for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.create_canvas_grid()
        self.create_control_panel()

        self.draw_board()
        self.update_timer()

    def create_canvas_grid(self):
        """
        Создаёт сетку Canvas для игрового поля.
        Каждый элемент сетки связан с обработчиком кликов.
        """
        grid_frame = tk.Frame(self.root, bg='black')
        grid_frame.pack(pady=20)

        for r in range(self.board_size):
            for c in range(self.board_size):
                cnv = tk.Canvas(grid_frame, width=self.cell_size, height=self.cell_size, bg='gray', highlightthickness=2, highlightbackground='white')
                cnv.grid(row=r, column=c, padx=2, pady=2)
                cnv.bind("<Button-1>", lambda e, rr=r, cc=c: self.on_tile_click(rr, cc))
                self.canvases[r][c] = cnv

    def create_control_panel(self):
        """
        Создаёт панель управления с кнопкой выхода и таймером.
        """
        control_frame = tk.Frame(self.root, bg='black')
        control_frame.pack(pady=10)

        self.timer_label = tk.Label(control_frame, text=f"Time left: {self.time_left}", font=("Arial", 14), fg='white', bg='black')
        self.timer_label.pack(side=tk.LEFT, padx=20)

        quit_btn = tk.Button(control_frame, text="Quit", command=self.root.quit, font=("Arial", 12), bg='red', fg='white')
        quit_btn.pack(side=tk.RIGHT)

    def draw_board(self):
        """
        Перерисовывает игровое поле, подсвечивая освещённые клетки.
        """
        lit_cells = self.board.get_lit()

        for r in range(self.board_size):
            for c in range(self.board_size):
                cnv = self.canvases[r][c]
                cnv.delete("all")
                bg_color = 'yellow' if (r, c) in lit_cells else 'darkgray'
                cnv.configure(bg=bg_color)
                self._draw_tile(cnv, self.board.grid[r][c])

    def _draw_tile(self, canvas, tile):
        """
        Рисует линии соединения внутри клетки.
        """
        directions = tile.get_dirs()
        cx, cy = self.cell_size // 2, self.cell_size // 2
        line_color = 'orange'

        for d in directions:
            if d == 'up':
                canvas.create_line(cx, cy, cx, 0, fill=line_color, width=4)
            elif d == 'down':
                canvas.create_line(cx, cy, cx, self.cell_size, fill=line_color, width=4)
            elif d == 'left':
                canvas.create_line(cx, cy, 0, cy, fill=line_color, width=4)
            elif d == 'right':
                canvas.create_line(cx, cy, self.cell_size, cy, fill=line_color, width=4)

    def on_tile_click(self, r, c):
        """
        Обрабатывает клики по клеткам, поворачивает блок и проверяет победу.
        """
        if self.game_over:
            return

        self.board.grid[r][c].rotate()
        self.draw_board()

        if self.board.is_solved():
            self.game_over = True
            messagebox.showinfo("Победа", "Вы зажгли все блоки!")
            self.timer_label.config(text="Победа")

    def update_timer(self):
        """
        Обновляет таймер каждую секунду и проверяет проигрыш по времени.
        """
        if self.game_over:
            return

        self.time_left -= 1
        self.timer_label.config(text=f"Time left: {self.time_left}")

        if self.time_left <= 0:
            self.game_over = True
            messagebox.showwarning("Время вышло!", "Вы не успели зажечь все блоки.")
            self.timer_label.config(text="Поражение")
            self.board.grid = [[self.board.solved_grid[r][c] for c in range(self.board_size)] for r in range(self.board_size)]
            self.draw_board()
        else:
            self.root.after(1000, self.update_timer)

    def run(self):
        """
        Запуск основного цикла Tkinter.
        """
        self.root.mainloop()



if __name__ == "__main__":
    #Перед запуском игры спрашиваем у пользователя размер поля:
    root_dialog = tk.Tk()
    root_dialog.withdraw()

    board_size = simpledialog.askinteger(
        "Board size",
        f"Введите размер поля ({MIN_BOARD_SIZE}..{MAX_BOARD_SIZE}):",
        minvalue=MIN_BOARD_SIZE,
        maxvalue=MAX_BOARD_SIZE,
        parent=root_dialog
    )
    root_dialog.destroy()

    if board_size is None:
        print("Размер поля не был задан. Игра прервана.")
    else:
        game = Game(board_size=board_size,
                    timer_seconds=TIMER_DEFAULT,
                    cell_size=CELL_SIZE_DEFAULT)
        game.run()