# Создайте класс Students, содержащий поля: фамилия и инициалы, номер группы,
# успеваемость (массив из пяти элементов).
# Создать класс School:
# ●	Добавить возможность для добавления студентов в школу
# ●	Добавить возможность вывода фамилий и номеров групп студентов, имеющих
# оценки, равные только 5 или 6.
# ●	Добавить возможность вывода учеников заданной группы
# ●	Добавить возможность вывода учеников претендующих на автомат(ср. балл >= 7)


class Student:
    """Student's properties"""
    def __init__(self, name: str, group_number: int, marks: list):
        self.name = name
        self.group_number = group_number
        self.marks = marks

    def count_average_progress(self):
        progress = sum(self.marks) / len(self.marks)
        return progress


class School:
    """School's properties"""
    # Создаем с помощью конструктора объект класса School
    def __init__(self, school_number, students=[]):
        self.students = students
        self.school_number = school_number

    # Добавить возможность для добавления студентов в школу
    def add_students(self, students=[]):
        """
        This function adds new students to list of students or empty list
        :param students: list
        :return:
        """
        self.students += students

    # Добавить возможность вывода фамилий и номеров групп студентов, имеющих
    # оценки, равные только 5 или 6.
    def show_students_5_6(self):
        """
        This function shows name and number of group of students which have
        marks 5 or 6
        :return:
        """
        # Объявляем пустой список, куда будем записывать данные студентов,
        # соответствующих критерию поиска
        students_with_5_and_6 = []

        # Через for проходим по каждому студенту их списка студентов данного класса
        for student in self.students:
            set_marks = set(student.marks)
            if set_marks == {5} or set_marks == {6} or set_marks == {5, 6} or set_marks == {6, 5}:
                # С помощью append добавляем к пустому списку найденные значения
                students_with_5_and_6.append({
                    "name": student.name,
                    "group_number": student.group_number
                })
        # Если в список ничего не записали, выводим сообщение о том, что таких студентов нет
        if not students_with_5_and_6:
            print("There are no students which have marks 5 or 6")
        # Если студенты были найдены, выводим сообщение об этом и этот список
        else:
            print("There are students which have marks 5 and 6",
                  students_with_5_and_6)

    # Добавить возможность вывода учеников заданной группы
    def show_students_from_group(self, group_number: int):
        """
        This function shows name of students which have input group_number
        :param group_number: int
        :return:
        """
        # Объявляем пустой список, куда будем записывать данные студентов,
        # соответствующих критерию поиска
        students_from_group = []
        # Через for проходим по каждому студенту их списка студентов данного класса
        for student in self.students:
            if student.group_number == group_number:
                # С помощью append добавляем к пустому списку найденные значения
                students_from_group.append(student.name)
        # Если в список ничего не записали, выводим сообщение о том, что таких студентов нет
        if not students_from_group:
            print("There are no students from the group")
        # Если студенты были найдены, выводим сообщение об этом и этот список
        else:
            print(f"Students from the group {group_number}: ",
                  students_from_group)

    # Добавить возможность вывода учеников претендующих на автомат(ср. балл >= 7)
    def show_best_students(self):
        """
        This function shows students with marks 7 or more
        :return:
        """
        # Объявляем пустой список, куда будем записывать данные студентов,
        # соответствующих критерию поиска
        best_students = []
        # Через for проходим по каждому студенту их списка студентов данного класса
        for student in self.students:
            if student.count_average_progress() >= 7:
                # С помощью append добавляем к пустому списку найденные значенияv
                best_students.append(student.name)
        # Если в список ничего не записали, выводим сообщение о том, что таких студентов нет
        if not best_students:
            print("There are no students with marks 7 and more")
        # Если студенты были найдены, выводим сообщение об этом и этот список
        else:
            print("There are students with marks 7 and more", best_students)


students_in_school_1 = [
    Student("Abramov V.", 1, [7, 5, 8, 10, 10]),
    Student("Belyi R.", 2, [10, 6, 4, 10, 4]),
    Student("Ahmedova Y.", 1, [6, 6, 6, 5, 5]),
    Student("Usovich I.", 2, [5, 5, 5, 5, 5]),
    Student("Saburov N.", 2, [5, 6, 6, 6, 6])
]

school1 = School("1", students_in_school_1)
school1.show_students_from_group(2)
school1.add_students([Student("Sherbakov A.", 2, [4, 7, 8, 6, 5])])
print(school1.students)
school1.show_best_students()
school1.show_students_5_6()
