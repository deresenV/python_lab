import sys
import csv
import statistics
from split import split_data

def read_data_from_file(filename):
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  
        data = [(float(row[0]), float(row[1])) for row in reader]
    return data

def calculate_statistics(data):
    values = [value[1] for value in data]
    return {
        'count': len(values),
        'mean': statistics.mean(values),
        'mode': statistics.mode(values),
        'median': statistics.median(values)
    }

def main():
    if len(sys.argv) != 3:
        print("Использование: python3 lab3.py <filename> <interval>")
        sys.exit(1)

    filename = sys.argv[1]
    interval = float(sys.argv[2])

    data = read_data_from_file(filename)
    intervals = split_data(data, interval)

    for start, end, segment in intervals:
        stats = calculate_statistics(segment)
        if stats:
            print(f"Отрезок: {start} - {end}")
            print(f"  Количество значений: {stats['count']}")
            print(f"  Среднее значение: {stats['mean']}")
            print(f"  Мода: {stats['mode']}")
            print(f"  Медиана: {stats['median']}")
            print()

main()
