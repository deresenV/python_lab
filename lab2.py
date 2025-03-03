import sys

lines = []  
clipboard = "" 
history = []  

def local_save():
    global history, lines
    history.append(lines.copy())

def load_file(file_path):
    global lines
    try:
        with open(file_path, 'r') as file:
            lines = [line.rstrip("\n") for line in file]
    except FileNotFoundError:
        print(f"Файл {file_path} не найден")
        lines = []

def insert(text, num_row=None, num_col=None):
    global lines
    local_save()

 
    if num_row is None:
        if lines:  
            lines[-1] += text  
        else:  
            lines.append(text)  
        return

    num_row -= 1

    if num_row < 0:
        print("Ошибка: Номер строки должен быть положительным числом")
        return

    while len(lines) <= num_row:
        lines.append("")

    if num_col is None:
        lines[num_row] += text 
    else:
        num_col -= 1

        if num_col < 0:
            print("Ошибка: Номер столбца должен быть положительным числом")
            return

        if num_col > len(lines[num_row]):
            lines[num_row] += " " * (num_col - len(lines[num_row]))

        lines[num_row] = (
            lines[num_row][:num_col] + text + lines[num_row][num_col:]
        )


def dell():
    global lines
    local_save()
    lines = []

def delrow(num_row):
    global lines
    if num_row is None or num_row < 1 or num_row > len(lines):
        print("Ошибка: Некорректный номер строки")
        return
    local_save()
    del lines[num_row - 1]

def delcol(num_col):
    global lines
    if num_col is None or num_col < 1:
        print("Ошибка: Некорректный номер столбца")
        return
    local_save()
    num_col -= 1
    for i in range(len(lines)):
        if num_col < len(lines[i]):
            lines[i] = lines[i][:num_col] + lines[i][num_col + 1:]

def swap(num_row_1, num_row_2):
    global lines
    if num_row_1 is None or num_row_2 is None or num_row_1 < 1 or num_row_2 < 1 or num_row_1 > len(lines) or num_row_2 > len(lines):
        print("Ошибка: Некорректные номера строк")
        return
    local_save()
    num_row_1 -= 1
    num_row_2 -= 1
    lines[num_row_1], lines[num_row_2] = lines[num_row_2], lines[num_row_1]

def undo(num_operations=1):
    global history, lines
    if num_operations < 1 or num_operations > len(history):
        print("Ошибка: Некорректное количество операций")
        return
    for _ in range(num_operations):
        lines = history.pop()

def copy(num_row, start=None, end=None):
    global clipboard, lines
    if num_row is None or num_row < 1 or num_row > len(lines):
        print("Ошибка: Некорректный номер строки")
        return
    num_row -= 1
    line = lines[num_row]
    if start is None:
        clipboard = line
    else:
        if start < 1 or start > len(line):
            print("Ошибка: Некорректный стартовый символ")
            return
        start -= 1
        if end is None:
            clipboard = line[start:]
        else:
            if end < start or end > len(line):
                print("Ошибка: Некорректный конечный символ")
                return
            end -= 1
            clipboard = line[start:end + 1]

def paste(num_row):
    global lines, clipboard
    if num_row is None or num_row < 1:
        print("Ошибка: Некорректный номер строки")
        return


    num_row -= 1

    while len(lines) <= num_row:
        lines.append("")

    local_save()
    lines[num_row] += clipboard

def save(file_path):
    global lines
    with open(file_path, 'w') as file:
        for line in lines:
            file.write(line + "\n")
    print("Файл сохранен")

def show():
    global lines
    for i, line in enumerate(lines, start=1):
        print(f"{i}: {line}")

def exit(file_path):
    global history
    if len(history) > 0:
        answer = input("Есть несохраненные изменения. Сохранить? (y/n): ")
        if answer.lower() == 'y':
            save(file_path)
    print("Выход из редактора")
    quit()

def main():
    if len(sys.argv) != 2:
        print("Укажите файл")
        return
    file_path = sys.argv[1]
    load_file(file_path)

    while True:
        command = input("Введите команду: ").strip().split()
        if not command:
            continue
        cmd = command[0]
        args = command[1:]
        if cmd == "insert":
            if len(args) < 1:
                print("Ошибка: Недостаточно аргументов")
                continue
            text = args[0].strip('"')
            num_row = int(args[1]) if len(args) > 1 else None
            num_col = int(args[2]) if len(args) > 2 else None
            insert(text, num_row, num_col)
        elif cmd == "del":
            dell()
        elif cmd == "delrow":
            if len(args) < 1:
                print("Ошибка: Недостаточно аргументов")
                continue
            num_row = int(args[0])
            delrow(num_row)
        elif cmd == "delcol":
            if len(args) < 1:
                print("Ошибка: Недостаточно аргументов")
                continue
            num_col = int(args[0])
            delcol(num_col)
        elif cmd == "swap":
            if len(args) < 2:
                print("Ошибка: Недостаточно аргументов")
                continue
            num_row_1 = int(args[0])
            num_row_2 = int(args[1])
            swap(num_row_1, num_row_2)
        elif cmd == "undo":
            num_operations = int(args[0]) if len(args) > 0 else 1
            undo(num_operations)
        elif cmd == "copy":
            if len(args) < 1:
                print("Ошибка: Недостаточно аргументов")
                continue
            num_row = int(args[0])
            start = int(args[1]) if len(args) > 1 else None
            end = int(args[2]) if len(args) > 2 else None
            copy(num_row, start, end)
        elif cmd == "paste":
            if len(args) < 1:
                print("Ошибка: Недостаточно аргументов")
                continue
            num_row = int(args[0])
            paste(num_row)
        elif cmd == "save":
            save(file_path)
        elif cmd == "show":
            show()
        elif cmd == "exit":
            exit(file_path)
        else:
            print("Неизвестная команда")


main()