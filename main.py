class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lector, course, grade):
        if (isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress
                and grade in range(0, 11)):
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        result = 0
        if self.grades:
            for grade in self.grades.values():
                result += sum(grade) / len(grade)
            return result / len(self.grades)
        else:
            return 0

    def __str__(self):
        return (f"Имя:{self.name}\n Фамилия:{self.surname}\n Средняя оценка за домашние задания:"
                f"{self.average_grade()}\n Курсы в процессе изучения:{self.courses_in_progress}\n Завершенные курсы:"
                f"{self.finished_courses}")


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def average_grade(self):
        total_grades = 0
        for grade in self.grades:
            total_grades += grade
        result = total_grades / len(self.grades)
        return result

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __str__(self):
        return (f"Имя:{self.name}\n Фамилия:{self.surname}\n Средняя оценка за лекцию:"
                f"{self.average_grade()}\n")


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\n"


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student.grades)