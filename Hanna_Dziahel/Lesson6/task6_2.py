# Подсчет количества букв

def count_letters(word: str):
    """
    This function counts how many letters are in a word
    """
    letter = []
    cnt = []
    for c in word:
        if c not in letter:
            letter.append(c)
            cnt.append(1)
        else:
            cnt[-1] += 1
    return list(zip(letter, cnt))


# Записываем в переменную значение, полученное при применении функции к слову
my_letter_count = count_letters('aaabbceedd')

# Выводим значения списка из tuples через for
my_count_list = [i + "" + str(n) for [i, n] in my_letter_count]
# Соединяем значения из списка в одну строку через join()
my_count_list = (''.join(my_count_list))
# Заменяем 1 на '' через replace()
result = my_count_list.replace('1', '')
print(result)
