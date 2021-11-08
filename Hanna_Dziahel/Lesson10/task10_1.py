# Определить иерархию и создать несколько цветов (Розы, Тюльпаны, Фиалки, Ромашки).
# У каждого класса цветка следующие атрибуты:
# Стоимость – атрибут класса, который определяется заранее
# Свежесть (в днях), цвет, длинна стебля – атрибуты экземпляра
# При попытке вывести информацию о цветке, должен отображаться цвет и тип
# Rose = RoseClass(7, Красная, 15)
# Print(Rose) -> Красная Роза
# Собрать букет (можно использовать аксессуары – отдельные классы со своей
# стоимостью: например, упаковочная бумага) с определением ее стоимости.
# У букета должна быть возможность определить время его увядания по среднему
# времени жизни всех цветов в букете
# Позволить сортировку цветов в букете на основе различных параметров
# (свежесть/цвет/длина стебля/стоимость...)
# Реализовать поиск цветов в букете по определенным параметрам.
# Узнать, есть ли цветок в букете.
# Добавить возможность получения цветка по индексу либо возможность пройтись по
# букету и получить каждый цветок по-отдельности
from operator import attrgetter


# Создаем класс-родитель Flower
class Flower():
    # Определяем стоимость как атрибут класса
    # Статические поля
    default_price = 0

    def __init__(self, freshness, color, stem_length):
        # Определяем свежесть, цвет, длину стебля как атрибуты экземпляра
        # Динамические поля
        self.freshness = freshness
        self.color = color
        self.stem_length = stem_length
        self.price = self.default_price

    # Создаем функцию для получения имени класса
    def get_class_name(self):
        """
        This function returns class name
        :return:
        """
        return self.__class__.__name__

    # Объявляем магический метод __str__ для вывода цвета и типа цветка
    def __str__(self):
        return f"Информация о цветке по цвету и типу - {self.color} {self.get_class_name()}"

    # Создаем статический метод, котороый принтит объекты класса Flower,
    # а не ссылки на объекты
    @staticmethod
    def show_flowers(flowers):
        """
        This function prints objects of Flower class
        :param flowers:
        :return:
        """
        for flower in flowers:
            print(flower)


# Создаем класс-потомок от класса Flower
class Rose(Flower):
    # Переопределяем значение атрибута класса-родителя
    default_price = 100
    pass


# Создаем класс-потомок от класса Flower
class Tulip(Flower):
    # Переопределяем значение атрибута класса-родителя
    default_price = 50
    pass


# Создаем класс-потомок от класса Flower
class Violet(Flower):
    # Переопределяем значение атрибута класса-родителя
    default_price = 40


# Создаем класс-потомок от класса Flower
class Chamomile(Flower):
    # Переопределяем значение атрибута класса-родителя
    default_price = 30


# Создаем класс-родитель Accessory
class Accessory:
    default_price = 0

    def __init__(self):
        self.price = self.default_price


# Создаем класс-потомок от класса Accessory
class Wrapping_paper(Accessory):
    # Переопределяем значение атрибута класса-родителя
    default_price = 10
    pass


# Создаем общий класс Bouquet, который будет содержать цветы, аксессуары,
# все основные методы
class Bouquet:
    # Передаем в качестве параметров списки цветов и аксесуаров
    def __init__(self, flowers, accessories):
        self.flowers = flowers
        self.accessories = accessories

    # Собрать букет (можно использовать аксессуары – отдельные классы со своей
    # стоимостью: например, упаковочная бумага) с определением ее стоимости.

    def count_price(self):
        """
        This function counts common price of bouquet based on price of flowers
        and accessories
        :return:
        """
        # Создаем переменную с общей суммой для записи суммы цветов и аксессуаров
        bouquet_price = 0
        # С помощью for проходим по каждому элементу списка
        for flower in self.flowers:
            # Записываем цену в общую сумму
            bouquet_price += flower.price
        # С помощью for проходим по каждому элементу списка
        for accessory in self.accessories:
            # Записываем цену в общую сумму
            bouquet_price += accessory.price
        return bouquet_price

    # У букета должна быть возможность определить время его увядания по среднему
    # времени жизни всех цветов в букете
    def count_freshness_time(self):
        """
        This function counts average freshness of all flowers in bouquet
        :return:
        """
        # Создаем переменную с общим временем свежести для записи значений
        total_freshness_time = 0
        # С помощью for проходим по каждому элементу списка
        for flower in self.flowers:
            # Записываем время свежести каждого цветка в общее время
            total_freshness_time += flower.freshness
        # Находим среднее время свежести
        average_freshness_time = total_freshness_time / len(self.flowers)
        return average_freshness_time

    # Позволить сортировку цветов в букете на основе различных параметров
    # (свежесть/цвет/длина стебля/стоимость...)
    def sort_flowers(self):
        """
        This function sorts flowers in bouquet based on entered value
        :return:
        """
        sort_option = input('''Sort flowers by:
        1. Freshness
        2. Color
        3. Stem Length
        4. Price
        5. No sorting
        Enter value: ''')
        if sort_option == '1':
            print(self.sort_flowers_by_freshness())
        elif sort_option == '2':
            print(self.sort_flowers_by_color())
        elif sort_option == '3':
            print(self.sort_flowers_by_stem_length())
        elif sort_option == '4':
            print(self.sort_flowers_by_price())
        else:
            pass

    def sort_flowers_by_freshness(self):
        """
        This function sorts flowers in bouquet by freshness
        :return:
        """
        result = sorted(self.flowers, key=attrgetter('freshness'))
        return result

    def sort_flowers_by_color(self):
        """
        This function sorts flowers in bouquet by color
        :return:
        """
        result = sorted(self.flowers, key=attrgetter('color'))
        return result

    def sort_flowers_by_stem_length(self):
        """
        This function sorts flowers in bouquet by stem length
        :return:
        """
        result = sorted(self.flowers, key=attrgetter('stem_length'))
        return result

    def sort_flowers_by_price(self):
        """
        This function sorts flowers in bouquet by price
        :return:
        """
        result = sorted(self.flowers, key=attrgetter('price'))
        return result

    def search_flowers(self):
        """
        This function searches flowers based on entered value
        :return:
        """
        search_option = input('''Search flowers by:
        1. Freshness
        2. Color
        3. Stem Length
        4. Price
        5. No search
        Enter value: ''')

        if search_option in ['1', '2', '3', '4']:
            searched_value = input("Enter searched_value: ")
            if search_option == '1':
                print(self.search_flowers_by_freshness(searched_value))
            elif search_option == '2':
                print(self.search_flowers_by_freshness(searched_value))
            elif search_option == '3':
                print(self.search_flowers_by_stem_length(searched_value))
            elif search_option == '4':
                print(self.search_flowers_by_price(searched_value))
        else:
            pass

    def search_flowers_by_freshness(self, searched_value):
        """
        This function searches flowers in bouquet by freshness value
        :param searched_value:
        :return:
        """
        found_values = list(
            filter(lambda flower: searched_value == str(flower.freshness),
                   self.flowers))
        return found_values

    def search_flowers_by_color(self, searched_value):
        """
        This function searches flowers in bouquet by color value
        :param searched_value:
        :return:
        """
        found_values = list(
            filter(lambda flower: searched_value == str(flower.color),
                   self.flowers))
        return found_values

    def search_flowers_by_stem_length(self, searched_value):
        """
        This function searches flowers in bouquet by stem length value
        :param searched_value:
        :return:
        """
        found_values = list(
            filter(lambda flower: searched_value == str(flower.stem_length),
                   self.flowers))
        return found_values

    def search_flowers_by_price(self, searched_value):
        """
        This function searches flowers in bouquet by price value
        :param searched_value:
        :return:
        """
        found_values = list(
            filter(lambda flower: searched_value == str(flower.price),
                   self.flowers))
        return found_values

    # Используем магический метод, чтобы узнать, есть ли цветок в букете
    def __contains__(self, item):
        return item in self.flowers

    # Используем магический метод, чтобы получить цветок по индексу
    def __getitem__(self, item):
        if 0<=item<len(self.flowers):
            return self.flowers[item]
        else:
            raise IndexError("Index is outside of boundaries of collection")

    # Возможность пройтись по букету и получить каждый цветок по-отдельности
    def __iter__(self):
        return iter(self.flowers)

rose = Rose(100, "Pink", 5)
blue = Violet(10, "Blue", 9)
# 1 - вывести информацию о цветке
# print(Rose(100, "Pink", 5))

# 2.1 - Собрать букет
best_bouquet = Bouquet([Rose(100, "Red", 5), Tulip(30, "Blue", 10), rose],
                       [Wrapping_paper()])

# 2.2 - Определить стоимость собранного букета
# print(best_bouquet.count_price())

# 3 - Определить время увядания букета по среднему времени жизни всех цветов
# print(best_bouquet.count_freshness_time())

# 4 - Cортировка цветов в букете на основе различных параметров
# best_bouquet.sort_flowers()

# 5 - Поиск цветов в букете на основе различных параметров
# best_bouquet.search_flowers()

# 6 - Узнать, есть ли цветок в букете (__contains__)
# print(blue in best_bouquet.flowers)

# 7 - Возможность получения цветка по индексу (__getitem__)
# print(best_bouquet.flowers[0])

# 8 - Возможность пройтись по букету и получить каждый цветок по-отдельности (__iter__)
#for flower in best_bouquet.flowers:
#    print(flower)