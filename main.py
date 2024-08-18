class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.courses_attached = []

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

    @property
    def average_grade(self):
        total_grades = 0
        for grade in self.grades:
            total_grades += grade
        result = total_grades / len(self.grades)
        return result

    def __gt__(self, other):
        return self.average_grade > other.average_grade

    def __str__(self):
        return f"Имя:{self.name}\n Фамилия:{self.surname}\n Средняя оценка за лекцию:"


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

best_lecturer = Lecturer('Some', 'Buddy')
best_lecturer.courses_attached += ['Python']

best_reviewer = Reviewer('Some', 'Buddy')
best_reviewer.courses_attached += ['Python']
Reviewer.rate_hw(best_reviewer, best_student, 'Python', 10)
Reviewer.rate_hw(best_reviewer, best_student, 'Python', 10)
Reviewer.rate_hw(best_reviewer, best_student, 'Python', 10)

best_student.courses_attached += ['Python']
best_student.rate_lecturer(best_lecturer, 'Python', 10)
best_student.rate_lecturer(best_lecturer, 'Python', 10)
best_student.rate_lecturer(best_lecturer, 'Python', 10)

print(best_student.grades)
print(best_lecturer.grades)

some_reviewer = Reviewer('Some', 'Buddy')
some_lecturer = Lecturer('Some', 'Buddy')
some_student = Student('Ruoy', 'Eman', 'your_gender')

some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Git']
some_student.finished_courses += ['Введение в программирование']

some_lecturer.courses_attached += ['Python']
some_lecturer.courses_attached += ['Git']
some_student.rate_lecturer(some_lecturer, 'Python', 10)
some_student.rate_lecturer(some_lecturer, 'Python', 10)
some_student.rate_lecturer(some_lecturer, 'Python', 10)
some_student.rate_lecturer(some_lecturer, 'Git', 10)
some_student.rate_lecturer(some_lecturer, 'Git', 10)
some_student.rate_lecturer(some_lecturer, 'Git', 10)
some_student.rate_lecturer(some_lecturer, 'Git', 9)

some_reviewer.courses_attached += ['Python']
some_reviewer.courses_attached += ['Git']
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Git', 10)
some_reviewer.rate_hw(some_student, 'Git', 10)
some_reviewer.rate_hw(some_student, 'Git', 10)
some_reviewer.rate_hw(some_student, 'Git', 9)

some_lecturer_2 = Lecturer('Eddy', 'Bobby')
some_lecturer_2.courses_attached += ['Python']
some_lecturer_2.courses_attached += ['Git']

some_student.rate_lecturer(some_lecturer_2, 'Python', 10)
some_student.rate_lecturer(some_lecturer_2, 'Python', 10)
some_student.rate_lecturer(some_lecturer_2, 'Python', 5)
some_student.rate_lecturer(some_lecturer_2, 'Git', 10)
some_student.rate_lecturer(some_lecturer_2, 'Git', 10)
some_student.rate_lecturer(some_lecturer_2, 'Git', 10)

some_student_2 = Student('Ric', 'Lee', 'your_gender')
some_student_2.courses_in_progress += ['Python']
some_student_2.courses_in_progress += ['Git']
some_student_2.finished_courses += ['Введение в программирование']

some_reviewer.courses_attached += ['Python']
some_reviewer.courses_attached += ['Git']
some_reviewer.rate_hw(some_student_2, 'Python', 10)
some_reviewer.rate_hw(some_student_2, 'Python', 10)
some_reviewer.rate_hw(some_student_2, 'Python', 7)
some_reviewer.rate_hw(some_student_2, 'Git', 10)
some_reviewer.rate_hw(some_student_2, 'Git', 10)
some_reviewer.rate_hw(some_student_2, 'Git', 10)
some_reviewer.rate_hw(some_student_2, 'Git', 10)

print(some_reviewer)
print(some_lecturer)
print(some_lecturer_2)
print(some_student)
print(some_student_2)

print(best_student.grades)

lec_list = [some_lecturer, some_lecturer_2]
stud_list = [some_student, some_student_2]


def student_rating(stud_list, course_name):
    sum_all = 0
    count = 0
    for stud in stud_list:
        for course_name in stud.grades:
            if course_name != course_name:
                return stud.grades.values()

            sum_all += sum(stud.grades[course_name])
            count += len(stud.grades[course_name])
    if sum_all > 0:
        return round(sum_all / count, 1)
    else:
        return 0


def lecturer_rating(lec_list, course_name):
    sum_all = 0
    count = 0
    for lec in lec_list:
        for course_name in lec.grades:
            if course_name != course_name:
                return lec.grades.values()

            sum_all += sum(lec.grades[course_name])
            count += len(lec.grades[course_name])
    if count > 0:
        return round(sum_all / count, 1)
    else:
        return 0


print(f"Средняя оценка для всех студентов по курсу {'Python'}: {student_rating(stud_list, 'Python')}")
print(f"Средняя оценка для всех лекторов по курсу {'Python'}: {lecturer_rating(lec_list, 'Python')}")
