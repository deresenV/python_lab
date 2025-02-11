import sys
import os


def insert(path, text, num_row=None, num_col=None):
    with open(path, "r") as f:
        lines = f.readlines()  # Читаем строки
    text=text.replace('"',"")
    if num_row!=None and num_row>len(lines):
        for i in range(num_row-len(lines)):
            lines.append("\n")
        lines[num_row-1]=text
    elif num_row is None:
        # Добавляем в конец файла
        lines.append(text + "\n")

    elif num_col is None:
        # Вставляем в конкретную строку (начало от 1, а индексы с 0)
        if num_row - 1 < len(lines):
            lines[num_row - 1] = lines[num_row - 1].rstrip("\n") + text + "\n"
        else:
            lines.append("\n" * (num_row - len(lines) - 1) + text + "\n")  # Заполняем пустые строки

    else:
        # Вставляем в конкретное место внутри строки
        if num_row - 1 < len(lines):
            line = lines[num_row - 1].rstrip("\n")  # Убираем \n
            lines[num_row - 1] = line[:num_col] + text + line[num_col:] + "\n"
        else:
            lines.append("\n" * (num_row - len(lines) - 1) + text + "\n")  # Заполняем пустые строки

    with open(path, "w") as f:
        f.writelines(lines)  # Записываем обратно


def del_all(path, pusto=None):
    os.remove(path)
    open(path, 'w').close()
    print("Все содержимое файла удалено!")
def delrow(path,num_row):
    with open(path, "r") as f:
        lines = f.readlines()
    if len(lines)>=num_row:
        lines[num_row-1]="\n"
    with open(path, "w") as f:
        f.writelines(lines)

def delcol(path,num_col):
    with open(path, "r") as f:
        lines = f.readlines()
    # print(lines)
    for i in range(len(lines)):
        if len(lines[i])>=num_col:
            lines[i]=lines[i][0:num_col-1]+lines[i][num_col:]

    with open(path, "w") as f:
        f.writelines(lines)
def swap(path, num_row_1, num_row_2):
    with open(path, "r") as f:
        lines = f.readlines()
    if len(lines)<num_row_1 or len(lines)<num_row_2:
        for i in range(max(num_row_1, num_row_2)-len(lines)):
            lines.append("\n")
        print(lines[num_row_1-1], lines[num_row_2-1])
        lines[num_row_1 - 1], lines[num_row_2 - 1] = lines[num_row_2 - 1], lines[num_row_1 - 1]
    else:
        print(lines[num_row_1], lines[num_row_2])
        lines[num_row_1-1], lines[num_row_2-1] = lines[num_row_2-1], lines[num_row_1-1]
    with open(path, "w") as f:
        f.writelines(lines)
def undo(log, num):
    if len(log)<num:
        print("Введенное число больше размера изменений")
        return log
    for i in range(num):
        del(log[-1])
    return log
def copy(path, num_row, start, end):
    if num_row==None:
        print("Ошибка строки")
        return ""
    with open(path, "r") as f:
        lines = f.readlines()
    if len(lines)<num_row:
        return ""
    if start==None:
        start=1
    if end==None:
        end=len(lines[num_row-1])
    copy_text=lines[num_row-1][start-1:end]
    return copy_text
def paste(path, num_row, copy_text):
    insert(path, copy_text, num_row)
def save(path, log):
    i=0
    log=log[::-1]
    while log:
        command=log.pop()
        i+=1
        globals()[command[0]](command[1],**command[2])
    return []


def show(path):
    with open(path, 'r') as f:
        print(f.read())
def exit_redactor(path, log):
    if len(log)!=0:
        print("Вы не сохранили все изменения! Желаете ли вы их сохранить?(y/n)")
        ans = input()
        if ans=='y':
            log=save(path, log)
            return log
        elif ans=='n':
            sys.exit(1)
    else:
        sys.exit(1)

def main():
    log=[]
    copy_text=""
    if len(sys.argv)!=2:
        print("Укажите путь до файла!")
        sys.exit(1)
    else:
        path=sys.argv[1]
        while True:
            command = input().split()
            len_command=len(command)
            # print(command, len_command)
            if command[0] == "insert":
                log.append(('insert', path, {"text": command[1],
                                             "num_row": abs(int(command[2])) if len(command) >= 3 else None,
                                             "num_col": abs(int(command[3])) if len(command) >= 4 else None}))

            elif command[0] == "del":
                log.append(('del_all', path, {'pusto': None}))

            elif command[0] == "delrow" and len_command==2:
                log.append(('delrow', path, {"num_row": abs(int(command[1]))}))
            elif command[0] == "delcol" and len_command==2:
                log.append(('delcol', path, {"num_col": abs(int(command[1]))}))
            elif command[0] == "swap" and len_command==3 and command[1].isnumeric() and command[2].isnumeric():
                log.append(('swap', path, {"num_row_1": abs(int(command[1])), "num_row_2": abs(int(command[2]))}))

            elif command[0] == "undo":
                log=undo(log, int(command[1]) if len_command==2 else 1)

            elif command[0] == "copy" and 2 <= len_command <= 4:
                copy_text=copy(path,
                               int(command[1]) if len_command >= 2 and command[1].isnumeric() else None,
                               int(command[2]) if len_command >= 3 and command[2].isnumeric() else 1,
                               int(command[3]) if len_command == 4 and command[3].isnumeric() else None)
            elif command[0] == "paste" and len_command==2 and command[1].isnumeric():
                log.append(('paste', path, {"num_row": abs(int(command[1])),'copy_text': copy_text}))

            elif command[0] == "save":
                log=save(path, log)

            elif command[0] == "show":
                show(path)

            elif command[0] == "exit":
                log = exit_redactor(path, log)

            elif command[0]=="seelog":
                for i in log[::-1]:
                    print(i)
            else:
                print("Команда введена неверно")
main()