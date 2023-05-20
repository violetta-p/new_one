import json
import datetime
import os
from funcs import *


def load_data(file_name):
    """
    Функция принимает имя файла (с расширением),
    в котором хранятся данные, и считывает из него содержимое.
    На выходе возвращает объект типа str.
    """
    full_path_to_data = os.path.join(os.path.abspath('..'), file_name)
    with open(full_path_to_data, 'r', encoding='utf-8') as file_with_json:
        return file_with_json.read()


def get_all_data(payment):
    """
    Принимает элемент исходного массива с данными.
    Возвращает все данные в виде кортежа
    typle = (transaction_date, description, sender_info, recipient_info, amount)
    """
    transaction_date = get_date(payment.get("date", None))
    description = payment.get("description", None)
    sender_info = get_sender(payment.get("from", None))
    recipient_info = get_recipient(payment.get("to", None))
    amount = get_amount(payment.get("operationAmount", None))
    return transaction_date, description, sender_info, recipient_info, amount


def get_presentation(tuple_with_data):
    """
    Приминает кортеж с данными вида
    typle = (transaction_date, description, sender_info, recipient_info, amount).
    Возвращает данные в формате для вывода на экран
    """
    return f'{tuple_with_data[0]} {tuple_with_data[1]}\n'\
           f'{tuple_with_data[2]} -> {tuple_with_data[3]}\n'\
           f'{tuple_with_data[4]}\n'


data_file_name = "operations.json"  # Имя файла с данными о платежах

data_list = json.loads(load_data(data_file_name))  # Список с данными о платежах

# В json файле есть "пробелы" в данных. Данное действие убирает эти "пробелы"
cleaned_data = [i for i in data_list if i]

# Сортировка массива по дате операции (от большего к меньшему)
sorted_list = sorted(cleaned_data,
                     key=lambda x: datetime.datetime.strptime(" ".join(x["date"].split("T")), "%Y-%m-%d %H:%M:%S.%f"),
                     reverse=True)
counter = 0
for pay1 in sorted_list:
    if counter == 5:
        break
    if pay1["state"] == "EXECUTED":
        counter += 1
        print(get_presentation(get_all_data(pay1)))
    else:
        pass
