import statistics
import csv
import sys

from split_funs import split_data

def read_data_from_file(path):
    with open(path, newline='') as f: # time value
        reader = csv.DictReader(f, delimiter=',')
        return list(reader)


def calculate_statistics():
    pass
def main():
    if len(sys.argv) < 3:
        print("python3 lab3.py file_path interval")
        sys.exit(1)
    path = sys.argv[1]
    interval = int(sys.argv[2])
    print(path, interval)
    data_csv=read_data_from_file(path)
    sorted_interval= split_data(data_csv,interval)
    print(*sorted_interval, sep='\n')
main()