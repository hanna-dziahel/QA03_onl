# Написать пример чтобы hash от объекта 1 и 2 были одинаковые, а id разные

print('Способ 1')
# Используем, если в листе у нас только одно значение
object_1 = [213]
object_2 = [213]

print(id(object_1))
print(id(object_2))
print(hash(i for i in object_1))
print(hash(i for i in object_2))

print('Способ 2')


# Создаем функцию, которая будет соединять все элементы списка в один объект
# и возвращать от него хэш

def find_hash(list_with_values: list):
    """
    This function makes one string from elements in list and returns its hash
    """
    values_string = ''
    for element in list_with_values:
        values_string += str(element)
    return hash(values_string)


object_3 = [234, 345346, 346377]
object_4 = [234, 345346, 346377]
object_5 = ["qwe", "ad", "asd"]
object_6 = ["qwe", "ad", "asd"]
print(id(object_3))
print(id(object_4))
print(find_hash(object_3))
print(find_hash(object_4))

print(id(object_5))
print(id(object_6))
print(find_hash(object_5))
print(find_hash(object_6))
