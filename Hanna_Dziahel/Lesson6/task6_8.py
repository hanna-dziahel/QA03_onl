# Написать функцию, которая проверяет есть ли в списке объекты,
# которые можно вызвать

def is_callable(any_list: list):
    """
    This function defines if object in list is callable or not
    """
    for i in any_list:

        # Через callable() узнаем каждый объект в списке вызываемый или нет
        if callable(i):
            print('Объект в списке вызываемый: ', str(i))
        elif not callable(i):
            print('Объект в списке невызываемый: ', str(i))


list_for_method = [1, 3, 4]
user_list = [len, list_for_method.sort, 1, is_callable, 'text',
             {1: 'hi', 2: 'by'}, (1, 2, 3),
             [1, 2, 3]]
is_callable(user_list)
