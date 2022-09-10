class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.courses_in_progress = []
        self.grades = {}
        self.courses_end = []

    def __average_rating(self):
        wtf1 = sum(list(self.grades.values())[0])  # Не понимаю откуда тут появляется вложенный список
        wtf2 = len(list(self.grades.values())[0])
        return wtf1 / wtf2

    def __str__(self):
        res = f"Имя: {self.name}\n" \
              f"Фамилия: {self.surname}\n" \
              f"Средняя оценка за домашние задания: {self.__average_rating()}\n" \
              f"Курсы в процессе изучения: {self.courses_in_progress}\n" \
              f"Завершенные курсы: {self.courses_end}\n"
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Ошибка')
            return
        return self.__average_rating() < other.__average_rating()

    def add_courses(self, course_name):
        self.courses_in_progress.append(course_name)

    def rate_hw(self, teacher, grade):
        if isinstance(teacher, Lecturer):
            if set(self.courses_in_progress) & set(teacher.courses_attached):
                teacher.courses_grade.append(grade)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def add_courses(self, course_name):
        self.courses_attached.append(course_name)


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_grade = []

    def __average_rating(self):
        return (sum(self.courses_grade)) / len(self.courses_grade)

    def __str__(self):
        res = f"Имя: {self.name}\n" \
              f"Фамилия: {self.surname}\n" \
              f"Средняя оценка за лекции: {self.__average_rating()}\n"

        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Ошибка')
            return
        return self.__average_rating() < other.__average_rating()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print('Ошибка')

    def __str__(self):
        res = f"Имя: {self.name}\n" \
              f"Фамилия: {self.surname}\n"
        return res


Max = Student("Max", "Ivanov", "m")
Olga = Lecturer("Olga", "Ivanova")
Bupt = Reviewer("Bupt", "Ivanova")
Max.add_courses("math")
Olga.add_courses("math")
Bupt.add_courses("math")
Bupt.rate_hw(Max, "math", 8)
Bupt.rate_hw(Max, "math", 7)
Bupt.rate_hw(Max, "math", 10)
Max.rate_hw(Olga, 10)
Sergey = Student("Sergey", "Petrov", "m")
Alina = Lecturer("Alina", "Petrova")
Petra = Reviewer("Petra", "Petrova")
Sergey.add_courses("rus")
Alina.add_courses("rus")
Petra.add_courses("rus")
Petra.rate_hw(Sergey, "rus", 8)
Petra.rate_hw(Sergey, "rus", 7)
Sergey.rate_hw(Alina, 2)
Sergey.rate_hw(Alina, 6)
