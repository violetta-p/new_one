import os
from pathlib import Path

FILE_PATH = Path(__file__).parent.parent


def load_data(file_name):
    """
    Функция принимает имя файла (с расширением),
    в котором хранятся данные, и считывает из него содержимое.
    На выходе возвращает объект типа str.
    """
    full_path_to_data = os.path.join(FILE_PATH, file_name)
    with open(full_path_to_data, 'r', encoding='utf-8') as file_with_json:
        return file_with_json.read()
