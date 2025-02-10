import sys
import os
def insert(path, text, num_str=None, cursor_str=None):

    pass
def del_all(path):
    os.remove(path)
    open(path, 'w').close()
    print("Все содержимое файла удалено!")
def delrow(path,num_row):
    pass
def delcol(path,num_col):
    pass
def swap(path, num_row1=None, num_row2=None):
    pass
def undo(path, num_operations=1):
    pass
def copy(path, num_row, start=None, end=None):
    pass
def paste(path, num_row):
    pass
def save(path):
    pass
def show(path):
    pass
def exit_redactor(path, log):
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
                    log.append(('insert',path, command[1], int(command[2]), int(command[3])))
                elif command[0]=="del":
                    log.append(('del', path))
                elif command[0]=="delrow":
                    log.append(('delrow',path, int(command[1])))
                elif command[0]=='swap':
                    log.append(('swap', path, int(command[1]), int(command[2])))
                elif command[0]=="undo":
                    log.append(('undo', path, int(command[1])))
                elif command[0]=="copy":
                    log.append(('copy', path, int(command[1]), int(command[2]), int(command[3])))
                elif command[0]=="paste":
                    log.append(('paste', path, int(command[1])))
                elif command[0]=="save":
                    log.append(('save', path))
                elif command[0]=="show":
                    log.append(('show', path))
                elif command[0]=="exit":
                    log.append(('exit', path))
                elif command[0]=="seelog":
                    print(log)
                    for i in log:
                        print(i)
main()