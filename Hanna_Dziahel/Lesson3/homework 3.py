# Даны два числа
a = 10
b = 23

# 1 - Поменять значения 'a' и 'b' местами
print('Задание 1')
# Использование 3-ей переменной для обмена значениями одновременно
temp = a
a = b
b = temp
print('a = ' + str(a))
print('b = ' + str(b))

# 2 - 'a' увеличить в 3 раза, 'b уменьшить на 3
print('Задание 2')
a = a * 3
b = b - 3
print('a = ' + str(a))
print('b = ' + str(b))

# 3 - Преобразовать 'a' во float, 'b' в str
print('Задание 3')
a = float(a)
b = str(b)
print(type(a))
print(type(b))

# 4 - Разделить значение в 'a' на 11 и вывести результат с точностью 3 знака
# после запятой
print("Задание 4")
# Использование функции round для округления float до необходимой цифры
# после запятой
a = round(a/11, 3)
print("a = " + str(a))

# 5 - Преобразовать значение 'b' во float и записать в переменную 'c'
print("Задание 5")
c = float(b)
# Возвести полученное число в 3-ю степень
c = c ** 3
print("с = " + str(c))

# 6 - Получить случайное число, кратное 3-м
print("Задание 6")
# Использование модуля random для получения случайного числа
import random
print(random.randrange(0, 1000000, 3))

# 7 - Получить квадратный корень из 100 и возвести в 4 степень
print("Задание 7")
d = 100
import  math
d = math.sqrt(d)
d = pow(d,4)
d= int(d)
print(d)

# 8 - Строку “Hi guys” вывести 3 раза и в конце добавить “Today”
print("Задание 8")
# Результат - “Hi guysHi guysHi guysToday”

hi_string = "Hi guys"
new_string = hi_string*3 + "Today"
print(new_string)

# 9 - Длина строки из задания 8
print("Задание 9")
print(len(new_string))

# 10 - Вывести слово “Today” из строки в прямом и обратном порядке
print("Задание 10")

# Поиск индекса первой буквы Today c помощью методов find или index
#print(new_string.find("Today"))
#print(new_string.index("Today"))

# Вывод слова “Today” в прямом порядке через извлечение среза
# Вывод слова “Today” в обратном порядке через извлечение среза
word_direct=new_string[21:]
word_reverse=new_string[:20:-1]

print(word_direct)
print(word_reverse)

# 11 - Вывести каждую 2-ю букву в прямом и обратном порядке
print("Задание 11")
# Вывод каждой второй буквы в прямом порядке через извлечение среза
# Вывод каждой второй буквы в обратном порядке через извлечение среза
phrase_direct = new_string[1::2]
phrase_reverse = new_string[-2::-2]
print(phrase_direct)
print(phrase_reverse)

# 12 - Используя форматирования подставить результаты в строку
print("Задание 12")
# Метод format()
print("Метод format()")
print("Task 10: {task_10_direct}, {task_10_reverse} Task 11: {task_11_direct}, {task_11_reverse}".format(task_10_direct=word_direct, task_10_reverse=word_reverse, task_11_direct=phrase_direct, task_11_reverse=phrase_reverse))
# Метод f-strings
print("Метод f-strings")
print(f"Task 10: {word_direct}, {word_reverse} Task 11: {phrase_direct}, {phrase_reverse}")
format_string = f"Task 10: {word_direct}, {word_reverse} Task 11: {phrase_direct}, {phrase_reverse}"

# 13 - Вместо 2-ого 'name' вставьте ваше имя
print("Задание 13")
name_string = 'my name is name'
# Использование метода replace()
print(name_string.replace("is name", "is hanna"))

# 14 - Вывести строку из задания 12
print("Задание 14")

# Выведение каждого слова с большой буквы методом title()
print(format_string.title())
# Выведение всех слов в верхнем регистре методом upper()
print(format_string.upper())
# Выведение всех слов в нижнем регистре методом lower()
print(format_string.lower())

# 15 - Cколько раз слово “Task” встречается в строке из задания 12
print("Задание 15")
# Использование метода count()
print(format_string.count('Task'))