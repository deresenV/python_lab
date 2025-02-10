import sys

def insert():
    pass
def del_all():
    pass
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
    if len(sys.argv)!=2:
        print("Укажите путь до файла!")
        sys.exit(1)
    else:
        path=sys.argv[1]
        print(path)
        file = open(path, "w")
main()