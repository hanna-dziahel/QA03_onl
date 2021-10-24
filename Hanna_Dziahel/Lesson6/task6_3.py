# Простейший калькулятор v0.1
# Реализуйте программу, которая спрашивала у пользователя,
# какую операцию он хочет произвести над числами,
# а затем запрашивает два числа и выводит результат
# Проверка деления на 0

def do_operation(action: int, number_1: int, number_2: int):
    """
    This function chooses which action will be taken based on input value
    """
    if action == 1:
        return number_1 + number_2
    elif action == 2:
        return number_1 - number_2
    elif action == 3:
        return number_1 * number_2
    elif action == 4:
        if number_2 == 0:
            return "Деление на ноль невозможно"
        return number_1 / number_2
    else:
        return 'Введен невалидный номер пункта меню'


print('''Выберите операцию:
    1. Сложение
    2. Вычитание
    3. Умножение
    4. Деление''')
user_action = int(input("Введите номер пункта меню: "))
user_number_1 = int(input("Введите первое число: "))
user_number_2 = int(input("Введите второе число: "))

print(do_operation(user_action, user_number_1, user_number_2))
