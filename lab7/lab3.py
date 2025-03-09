# lab3.py
import sys
import csv
import statistics
import os
from split import split_data

def read_data_from_file(filename):
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            headers = next(reader, None)
            if headers is None or len(headers) < 2:
                raise ValueError("Некорректный заголовок CSV")
            
            data = []
            for row_num, row in enumerate(reader, start=2):
                if len(row) != 2:
                    raise ValueError(f"Ошибка в строке {row_num}: неверное количество колонок")
                try:
                    time = float(row[0])
                    value = float(row[1])
                    data.append((time, value))
                except ValueError:
                    raise ValueError(f"Ошибка в строке {row_num}: нечисловые данные")
            return data
    except PermissionError:
        raise PermissionError("Нет прав на чтение файла")

def calculate_statistics(data):
    values = [value for _, value in data]
    try:
        mode = statistics.mode(values)
    except statistics.StatisticsError:
        mode = "Нет моды"
    return {
        'count': len(values),
        'mean': round(statistics.mean(values), 1),
        'mode': int(mode) if isinstance(mode, float) and mode.is_integer() else mode,
        'median': round(statistics.median(values), 1)
    }

def main():
    if len(sys.argv) != 3:
        print("Использование: python lab3.py <файл.csv> <интервал>")
        return "Ошибка аргументов"

    filename = sys.argv[1]
    interval = sys.argv[2]
    if float(interval) <= 0:
        return "Интервал должен быть строго больше нуля"
    # Проверка расширения файла
    if not filename.lower().endswith('.csv'):
        return "Файл не .csv!"

    try:
        interval = float(interval)
    except ValueError:
        return "Ошибка интервала"

    try:
        data = read_data_from_file(filename)
    except FileNotFoundError:
        return "Неверный файл"
    except PermissionError:
        return "Файл не имеет прав на чтение"
    except csv.Error:
        return "Файл не .csv!"
    except ValueError as e:
        return "Ошибка обработки файла проверьте правильность значений"
    except Exception as e:
        return "Неизвестная ошибка"

    intervals = split_data(data, interval)
    output = []

    for start, end, segment in intervals:
        if not segment:
            continue
        stats = calculate_statistics(segment)
        output.append(
            f"Начало отрезка:{start:.1f} Конец отрезка:{end:.1f}\n"
            f"Длина:{stats['count']} Ср.знач:{stats['mean']} "
            f"Мода:{stats['mode']} Медиана:{stats['median']}"
        )

    result = '\n'.join(output)
    print(result)
    return result

if __name__ == "__main__":
    main()