# Создать класс Book. Атрибуты: количество страниц, год издания, автор, цена.
# Добавить валидацию в конструкторе на ввод корректных данных.
# Создать свой класс MyException с ошибками, которые будут генерироваться
# при вводе некорректных данных для каждого из аттрибута класса.

class Book():
    def __init__(self, page_number, year, author, price):
        errors = []
        if type(page_number) == int:
            self.page_number = page_number
        else:
            errors.append("Page number should be integer")
        if type(year) == int:
            self.year = year
        else:
            errors.append("Year should be integer")
        if type(author) == str:
            self.author = author
        else:
            errors.append("Author should be string")
        if type(price) == int:
            self.price = price
        else:
            errors.append("Price should be integer")
        if len(errors) != 0:
            raise MyExceptions("There are my exceptions", errors)

class MyException(Exception):
   def __init__(self, message='It is my exception'):
       super().__init__(message)

class MyExceptions(Exception):
   def __init__(self, message='There are my exceptions', errors = []):
       super().__init__(message)
       self.errors = errors
#raise MyException

try:
    book = Book("78", "1995", "Ron", 100)
except MyException as error:
    print(error)
except MyExceptions as error:
    print('\n'.join(error.errors))
except Exception as error:
    print(error)


