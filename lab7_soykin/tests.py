import sys
import pytest
from lab3 import main

def test_first_question(monkeypatch): #нет указанного файла
    monkeypatch.setattr(sys, "argv", ["lab3.py", "example1.csv", "5"])
    assert main() == "Неверный файл"


def test_second_question(monkeypatch):#файл не имеет прав на чтение;
    pass
    monkeypatch.setattr(sys, "argv", ["lab3.py", "test_rights.txt", "5"])
    assert main() == "Файл не .csv!"


def test_third_question(monkeypatch): #файл не формата csv
    monkeypatch.setattr(sys, "argv", ["lab3.py", "png.png", "5"])
    assert main() == "Файл не .csv!"


def test_fourth_question(monkeypatch): #в какой-то из строк файла только одна колонка + данные не заданного типа
    monkeypatch.setattr(sys, "argv", ["lab3.py", "test_4_5.csv", "5"])
    assert main() == "Ошибка обработки файла проверьте правильность значений"


def test_sixth_question(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["lab3.py", "test_6.csv", "11"])
    assert main().strip() =="""Начало отрезка:1.04296875 Конец отрезка:11.42578125\nДлина:15 Ср.знач:177.2 Мода:182 Медиана:187""".strip()


def test_my1_question(monkeypatch): # Файл пустой
    monkeypatch.setattr(sys, "argv", ["lab3.py", "empty_test.csv", "11"])
    assert main().strip() =="\n".strip()


pytest.main()
