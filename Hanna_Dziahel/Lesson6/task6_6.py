# Функция проверяющая тип данных
# Написать функцию которая принимает на вход список из чисел, строк и таплов
# Функция должна вернуть сколько в списке элементов приведенных данных

def count_types(user_list: list):
    """
    This function counts how many int, str and tuple elements in list
    """
    int_types_count = 0
    str_types_count = 0
    tuple_types_count = 0
    for list_element in user_list:

        # Через isinstance() проверяем является ли элемент элементом
        # определенного типа
        if isinstance(list_element, int):
            int_types_count += 1
        if isinstance(list_element, str):
            str_types_count += 1
        if isinstance(list_element, tuple):
            tuple_types_count += 1

    # Создаем и возвращаем словарь
    return ({'int': int_types_count, 'str': str_types_count,
             'tuple': tuple_types_count})


print(count_types([1, 2, "a", (1, 2), "b"]))
