import os
import filecmp

# Функция для сканирования каталога и поиска файлов
def scan_directory(directory):
    file_paths = []
    for root, _, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            try:
                file_paths.append(filepath)
            except:
                print(f"Ошибка при обработке файла")
    return file_paths

# Функция для поиска дубликатов с использованием filecmp
def find_duplicates(file_paths):
    duplicates = []
    checked = set()
    for i in range(len(file_paths)):
        if file_paths[i] in checked:
            continue
        duplicate_group = [file_paths[i]]
        for j in range(i + 1, len(file_paths)):
            try:
                if filecmp.cmp(file_paths[i], file_paths[j], shallow=False):
                    duplicate_group.append(file_paths[j])
                    checked.add(file_paths[j])
            except:
                print(f"Ошибка при сравнении файлов")
        if len(duplicate_group) > 1:
            duplicates.append(duplicate_group)
    return duplicates

# Функция для удаления дубликатов
def process_duplicates(duplicates):
    for file_list in duplicates:
        print(f"Найдены дубликаты:")
        for idx, file in enumerate(file_list):
            print(f"[{idx}] {file}")
        while True:
            choice = input("Введите номер файла, который нужно сохранить (или 's' для пропуска): ")
            if choice == 's':
                print("Пропущено.")
                break
            try:
                choice = int(choice)
                if 0 <= choice < len(file_list):
                    for idx, file in enumerate(file_list):
                        if idx != choice:
                            os.remove(file)
                            print(f"Удалён: {file}")
                    break
                else:
                    print("Некорректный номер. Попробуйте снова.")
            except:
                print("Некорректный ввод. Попробуйте снова.")

if __name__ == "__main__":
    directory = input("Введите путь к каталогу: ")
    if os.path.isdir(directory):
        file_paths = scan_directory(directory)
        duplicates = find_duplicates(file_paths)
        process_duplicates(duplicates)
        print("Готово.")
    else:
        print("Некорректный путь к каталогу.")
