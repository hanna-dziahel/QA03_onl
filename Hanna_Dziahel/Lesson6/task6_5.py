# Работа с областями видимости

# Импортируем созданный нами модуль из task6_5_module.py
import task6_5_module

my_list = [1, 2, 3]
my_elem = 'hello'

# Используем функцию из импортированного модуля.
# Пишем модуль.название_функции(аргументы)
print(task6_5_module.add_elements(my_list, my_elem))
print(my_list)
