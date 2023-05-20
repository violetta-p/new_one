import datetime


def get_date(date_with_time):
    """
    Возвращает дату платежа в формате ДД.ММ.ГГГГ
    """
    data_str = date_with_time.split("T")
    data_format = datetime.date.fromisoformat(data_str[0])
    return data_format.strftime("%d.%m.%Y")


def get_sender(sender_info):
    """
    Возвращает данные отправителя в формате XXXX XX** **** XXXX,
    если они есть. Если данных нет, возвращает сообщение 'No info about sender'
    """
    if sender_info is not None:
        card_data = sender_info.split(" ")
        card_number = list(card_data[-1])
        card_number[-10:-4] = "******"
        card_number = "".join(card_number)
        new_number = ''
        for i in range(0, len(card_number), 4):
            new_number += card_number[i:i+4]
            new_number += ' '

        return f'{" ".join(card_data[:-1])} {new_number.rstrip(" ")}'
    return "No info about sender"


def get_recipient(recipient_info):
    """
    Возвращает данные получателя в формате 'Счет **XXXX'.
    """
    card_data = recipient_info.split(" ")
    card_number = list(card_data[-1])
    return f'{" ".join(card_data[:-1])} **{"".join(card_number[-4:])}'


def get_amount(amount_info):
    """
    Возвращает сумму платежа с указанием валюты
    """
    return f'{amount_info["amount"]} {amount_info["currency"]["name"]}'
