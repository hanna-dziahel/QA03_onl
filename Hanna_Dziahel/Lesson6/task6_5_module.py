# Модуль, содержащий только функцию. Рабочая программа в task6_5

def add_elements(old_list: list, elem: str):
    """
    This function creates new list based on old list and adds element to new list
    """

    # Создание нового списка через (list), a не через присваивание,
    # так как изменения будут переходить и в старый список
    copy_list = list(old_list)

    # Добавление элемента в список через append()
    copy_list.append(elem)
    return copy_list
