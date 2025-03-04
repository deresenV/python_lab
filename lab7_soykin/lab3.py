import statistics
import csv
import sys

from split_funs import split_data

def read_data_from_file(path):
    try:
        with open(path, newline='') as f: # time value
            reader = csv.DictReader(f, delimiter=',')
            return list(reader)
    except FileNotFoundError:
        return None
    except PermissionError:
        return None


def calculate_statistics(info_interval):
    results = []
    for i in range(len(info_interval)):
        info_values, time = info_interval[i][0], info_interval[i][1]
        results.append(f"Начало отрезка:{time['start_time']} Конец отрезка:{time['end_time']}\n"
                       f"Длина:{len(info_values)} Ср.знач:{statistics.mean(info_values)} "
                       f"Мода:{statistics.mode(info_values)} Медиана:{statistics.median(info_values)}\n\n")
    return "".join(results)



def main():
    if len(sys.argv) < 3:
        return "python3 lab3.py file_path interval"

    path = sys.argv[1]
    if ".csv" not in path:
        return "Файл не .csv!"

    interval = int(sys.argv[2])
    data_csv = read_data_from_file(path)
    if data_csv is None:
        return "Неверный файл"

    info_interval = split_data(data_csv, interval)
    if info_interval is None:
        return "Ошибка обработки файла проверьте правильность значений"

    return calculate_statistics(info_interval)


if __name__ == "__main__":
    result = main()
    if result is not None:
        print(result)
