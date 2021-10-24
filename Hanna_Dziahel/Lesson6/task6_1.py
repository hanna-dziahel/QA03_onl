from functools import reduce


def luhn(code: str):
    """
    This function validates if card valid or not
    """

    # Предварительно рассчитанные результаты умножения на 2 с вычетом 9 для больших цифр
    # Номер индекса равен числу, над которым проводится операция
    LOOKUP = (0, 2, 4, 6, 8, 1, 3, 5, 7, 9)
    code = reduce(str.__add__, filter(str.isdigit, code))
    evens = sum(int(i) for i in code[-1::-2])
    odds = sum(LOOKUP[int(i)] for i in code[-2::-2])
    return ((evens + odds) % 10 == 0)


import re


def validate_input(input_value: str):
    """
    This function validates if input_value consists of only 16 digits
    """

    # Использование регулярного выражения для проверки на валидность введенного значения
    match = re.match(r"\d{16}", input_value)
    if match is None:
        return False
    return True


card_number = input("Введите номер карты ")

# Присваиваем переменной значение проверенное функцией на валидацию
is_valid_input = validate_input(str(card_number))

# Проверяем валидность введенных данных
if is_valid_input is True:
    is_valid_card_number = luhn(str(card_number))
    if is_valid_card_number is True:
        print("Прошел проверку: ", card_number)
    else:
        print("Невалидный номер карты. Не прошел проверку: ", card_number)
else:
    print("Не прошел проверку. Ваш ввод должен состоять из 16 чисел: ",
          card_number)
