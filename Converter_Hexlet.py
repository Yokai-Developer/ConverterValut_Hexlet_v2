import time
from onlinerequests import currencies


# 1 Приветствие
# 2.1 Мануал
# 2.2 Перечень валют
# 2.3 Обновление курса валют
# 3 Выбора валюты которая имеется на руках
# 4 Объём имеющийся валюты
# 5 Во что конвертируем
# 6 Результат

def quiting(variable):
    if variable == 'quit':
        quit()


def is_number(amount):
    try:
        float(amount)
        return True
    except ValueError:
        return False


def greetings():
    # 1
    print('Приветствуем вас в конвертер валют !')
    # 2.1
    print("""Для работы с программой, вам необходимо:
    - Выбрать валюту из которой вы хотите конвертировать
    - Выбрать сумму имеющийся валюты
    - Выбрать валюту для которой будете конвертировать
    - Если хотите выйти из программы введите quit
    """)


def get_user_info(currency):
    # 2.2
    print("Список валют: ")
    for key in currency.keys():  # 'EUR' -> 'USD' -> 'GBD' -> 'RUB'
        print(f'- {key}')

    # 3
    first_currency = input("Введите имеющийся валюту: ")
    quiting(first_currency)
    while first_currency not in currency.keys():
        first_currency = input("Введите корректную имеющийся валюту: ")
        quiting(first_currency)

    # 4
    amount = input("Введите количество имеющийся валюты: ")
    quiting(amount)
    while not is_number(amount):
        amount = input("Введите корректное количество имеющийся валюты: ")
        quiting(amount)
    amount = float(amount)

    # 5
    second_currency = input("Введите валюту конвертации: ")
    quiting(second_currency)
    while second_currency not in currency.keys():
        second_currency = input("Введите корректную валюту конвертации: ")
        quiting(second_currency)

    return first_currency, amount, second_currency


def get_conversion(amount, first_currency, second_currency, currency):
    # 6
    result = amount / currency[first_currency] * currency[second_currency]
    return round(result, 2)


def main():
    flag = ''
    while flag != 'quit':
        greetings()
        currency = currencies()
        user_info = get_user_info(currency)
        print(get_conversion(
            first_currency=user_info[0],
            amount=user_info[1],
            second_currency=user_info[2],
            currency=currency))
        flag = input("Для продолжения введите любой символ или нажмите Enter: ")


main()
