import sys
import os
def insert(path, text, num_str=None, cursor_str=None):

    pass
def del_all(path):
    os.remove(path)
    open(path, 'w').close()
    print("Все содержимое файла удалено!")
def delrow():
    pass
def delcol():
    pass
def swap():
    pass
def undo():
    pass
def copy():
    pass
def paste():
    pass
def save():
    pass
def show():
    pass
def exit_redactor():
    pass

def main():
    log=[]
    if len(sys.argv)!=2:
        print("Укажите путь до файла!")
        sys.exit(1)
    else:
        path=sys.argv[1]
        with open(path, 'w+', encoding='utf-8') as f:
            while True:
                command = input().split()
                if command[0]=="insert":
                    log.append((path, command[1], int(command[2]), int(command[3])))
                elif command[0]=="del":
                    del_all(path)
                elif command[0]=="delrow":
                    pass
                elif command[0]=='swap':
                    pass
                elif command[0]=="undo":
                    pass
                elif command[0]=="copy":
                    pass
                elif command[0]=="paste":
                    pass
                elif command[0]=="save":
                    pass
                elif command[0]=="show":
                    pass
                elif command[0]=="exit":
                    pass
                elif command[0]=="seelog":
                    print(log)
                    for i in log:
                        print(i)
main()