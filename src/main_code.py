import json
import datetime
from src.funcs import get_all_data
from src.load_data import load_data


AMOUNT_OF_OPERATIONS = 5


def get_presentation(tuple_with_data):
    """
    Приминает кортеж с данными вида
    tuple = (transaction_date, description, sender_info, recipient_info, amount).
    Возвращает данные в формате для вывода на экран
    """
    return f'{tuple_with_data[0]} {tuple_with_data[1]}\n'\
           f'{tuple_with_data[2]} -> {tuple_with_data[3]}\n'\
           f'{tuple_with_data[4]}\n'


data_file_name = "operations.json"  # Имя файла с данными о платежах
data_list = json.loads(load_data(data_file_name))  # Массив с данными о платежах

cleaned_data = [i for i in data_list if i]  # В json файле есть "пробелы" в данных. Данное ействие убирает "пробелы"

# Сортировка массива по дате операции (от большего к меньшему)
sorted_list = sorted(cleaned_data,
                     key=lambda x: datetime.datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"),
                     reverse=True)
counter = 0
for pay1 in sorted_list:
    if counter == AMOUNT_OF_OPERATIONS:
        break
    if pay1["state"] == "EXECUTED":
        counter += 1
        print(get_presentation(get_all_data(pay1)))
