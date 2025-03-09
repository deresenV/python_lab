import sys
import pytest
from lab3 import main

def test_file_not_found(monkeypatch):  # Нет указанного файла
    monkeypatch.setattr(sys, "argv", ["lab3.py", "nonexistent.csv", "5"])
    assert main() == "Неверный файл"

def test_file_permission_denied(monkeypatch, tmp_path):
    file = tmp_path / "test_norights.csv"
    file.write_text("time,value\n1.0,100")
    def mock_open(*args, **kwargs):
        raise PermissionError("Доступ запрещен")
    
    monkeypatch.setattr("builtins.open", mock_open)
    monkeypatch.setattr(sys, "argv", ["lab3.py", str(file), "5"])
    assert main() == "Файл не имеет прав на чтение"

def test_file_not_csv(monkeypatch, tmp_path):  # Файл не формата CSV
    file = tmp_path / "test.txt"
    file.write_text("Это не CSV файл")
    monkeypatch.setattr(sys, "argv", ["lab3.py", str(file), "5"])
    assert main() == "Файл не .csv!"

def test_file_with_missing_column_and_invalid_data_type(monkeypatch, tmp_path):  #(подсмотрел у Сени)
    file = tmp_path / "test_two_task.csv"
    file.write_text("time,value\n1.0\n2.0,abc")
    monkeypatch.setattr(sys, "argv", ["lab3.py", str(file), "5"])
    assert main() == "Ошибка обработки файла проверьте правильность значений"

def test_output(monkeypatch, tmp_path):  # Файл делится на нужные интервалы по времени
    file = tmp_path / "test.csv"
    file.write_text("time,value\n1.0,100\n2.0,200\n3.0,300\n4.0,400")
    monkeypatch.setattr(sys, "argv", ["lab3.py", str(file), "2"])
    expected_output = (
        "Начало отрезка:1.0 Конец отрезка:3.0\n"
        "Длина:2 Ср.знач:150.0 Мода:100 Медиана:150.0\n"
        "Начало отрезка:3.0 Конец отрезка:5.0\n"
        "Длина:2 Ср.знач:350.0 Мода:300 Медиана:350.0"
    )
    assert main() == expected_output

def test_split_data(monkeypatch, tmp_path):  # Количество интервалов правильное
    file = tmp_path / "test_intervals.csv"
    file.write_text("time,value\n1.0,100\n2.0,200\n3.0,300\n4.0,400")
    monkeypatch.setattr(sys, "argv", ["lab3.py", str(file), "2"])
    result = main()
    # Ожидаем два интервала
    assert result.count("Начало отрезка:") == 2

def test_statistics_calculation(monkeypatch, tmp_path):  # Статистики подсчитываются верно
    file = tmp_path / "test_stats.csv"
    file.write_text("time,value\n1.0,100\n2.0,200\n3.0,300\n4.0,400")
    monkeypatch.setattr(sys, "argv", ["lab3.py", str(file), "2"])
    result = main()
    # Проверяем статистики для первого интервала
    assert "Ср.знач:150.0" in result
    assert "Мода:100" in result
    assert "Медиана:150.0" in result
    
def test_empty_csv(monkeypatch, tmp_path):  # Файл пустой
    file = tmp_path / "empty_test.csv"
    file.write_text("")  # Пустой файл
    monkeypatch.setattr(sys, "argv", ["lab3.py", str(file), "5"])
    assert main() == "Ошибка обработки файла проверьте правильность значений"

def test_negative_interval(monkeypatch,tmp_path ):#отрицательный интервал
    file = tmp_path / "n_test.csv"
    file.write_text("time,value\n1.0,100\n2.0,200\n3.0,300\n4.0,400")  
    monkeypatch.setattr(sys, "argv", ["lab3.py", str(file), "-2"])
    assert main() == "Интервал должен быть строго больше нуля"

if __name__ == "__main__":
    pytest.main()