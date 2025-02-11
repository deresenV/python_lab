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
def save(path, log):
    file = open(path, 'w+')

def show(path):
    with open(path, 'r') as f:
        print(f.read())
def exit_redactor(path, log):
    if len(log)!=0:
        print("Вы не сохранили все изменения! Желаете ли вы их сохранить?(y/n)")
        ans = input()
        if ans=='y':
            pass
        elif ans=='n':
            sys.exit(1)
    else:
        sys.exit(1)

def main():
    log=[]
    if len(sys.argv)!=2:
        print("Укажите путь до файла!")
        sys.exit(1)
    else:
        path=sys.argv[1]
        while True:
            command = input().split()
            len_command=len(command)
            if command[0]=="insert":
                log.append(('insert',path,
                            command[1], #text
                            int(command[2]) if len_command>=3 else None, #num_row
                            int(command[3]) if len(command)>=4 else None)) #num_col
            elif command[0]=="del":
                log.append(('del', path))
            elif command[0]=="delrow":
                log.append(('delrow',path, int(command[1])))
            elif command[0]=='swap':
                log.append(('swap', path, int(command[1]), int(command[2])))
            elif command[0]=="undo":
                log.append(('undo', path,
                            int(command[1]) if len_command>=2 else None))#num_operations
            elif command[0]=="copy":
                log.append(('copy', path, int(command[1]),
                            int(command[2]) if len_command >= 3 else None,  # start
                            int(command[3]) if len_command >= 4 else None))  # end
            elif command[0]=="paste":
                log.append(('paste', path, int(command[1])))
            elif command[0]=="save":
                save(path, log)
            elif command[0]=="show":
                show(path)
            elif command[0]=="exit":
                exit_redactor(path, log)
            elif command[0]=="seelog":
                for i in log:
                    print(i)
main()