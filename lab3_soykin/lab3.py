import statistics
import csv
import sys

from split_funs import split_data

def read_data_from_file(path):
    with open(path, newline='') as f: # time value
        reader = csv.DictReader(f, delimiter=',')
        return list(reader)


def calculate_statistics(info_interval):
    for i in range(len(info_interval)):
        info_values, time = info_interval[i][0], info_interval[i][1]
        print(f"Начало отрезка:{time['start_time']} Конец отрезка:{time['end_time']}\nДлина:{len(info_values)} "
              f"Ср.знач:{statistics.mean(info_values)} Мода:{statistics.mode(info_values)} "
              f"Медиана:{statistics.median(info_values)}", sep='\n')
        print("\n")


def main():
    if len(sys.argv) < 3:
        print("python3 lab3.py file_path interval")
        sys.exit(1)
    path = sys.argv[1]
    interval = int(sys.argv[2])
    data_csv=read_data_from_file(path)
    info_interval= split_data(data_csv,interval)
    calculate_statistics(info_interval)


main()