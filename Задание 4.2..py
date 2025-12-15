class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def rate_lecture(self, lecturer, course, grade):
        if not isinstance(lecturer, Lecturer):
            return 'Ошибка'
        
        if course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
            return None
        else:
            return 'Ошибка'
    
    def __str__(self):
        avg_grade = self._avg_grade()
        
        courses_in_progress_str = ', '.join(self.courses_in_progress) if self.courses_in_progress else 'Нет'
        finished_courses_str = ', '.join(self.finished_courses) if self.finished_courses else 'Нет'
        
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg_grade:.1f}\n"
                f"Курсы в процессе изучения: {courses_in_progress_str}\n"
                f"Завершенные курсы: {finished_courses_str}")
    
    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._avg_grade() < other._avg_grade()
    
    def __gt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._avg_grade() > other._avg_grade()
    
    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return abs(self._avg_grade() - other._avg_grade()) < 0.0001
    
    def _avg_grade(self):
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)
        return sum(all_grades) / len(all_grades) if all_grades else 0

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

class Lecturer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.grades = {}
    
    def __str__(self):
        avg_grade = self._avg_grade()
        
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {avg_grade:.1f}")
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._avg_grade() < other._avg_grade()
    
    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._avg_grade() > other._avg_grade()
    
    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return abs(self._avg_grade() - other._avg_grade()) < 0.0001
    
    def _avg_grade(self):
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)
        return sum(all_grades) / len(all_grades) if all_grades else 0

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if not isinstance(student, Student):
            return 'Ошибка'
        
        if course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
            return None
        else:
            return 'Ошибка'
    
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

def average_grade_for_homework(students, course_name):
    total_grades = []
    for student in students:
        if course_name in student.grades:
            total_grades.extend(student.grades[course_name])
    return sum(total_grades) / len(total_grades) if total_grades else 0

def average_grade_for_lectures(lecturers, course_name):
    total_grades = []
    for lecturer in lecturers:
        if course_name in lecturer.grades:
            total_grades.extend(lecturer.grades[course_name])
    return sum(total_grades) / len(total_grades) if total_grades else 0

student1 = Student('Николай', 'Емануилов', 'м')
student1.courses_in_progress = ['Python', 'Git', 'Django']
student1.finished_courses = ['Введение в программирование']

student2 = Student('Анна', 'Смирнова', 'ж')
student2.courses_in_progress = ['Python', 'Java', 'Базы данных']
student2.finished_courses = ['Алгоритмы и структуры данных']

print("Студенты:")
print(f"1. {student1.name} {student1.surname}")
print(f"2. {student2.name} {student2.surname}")
print()

lecturer1 = Lecturer('Иван', 'Иванов')
lecturer1.courses_attached = ['Python', 'Git']

lecturer2 = Lecturer('Петр', 'Петров')
lecturer2.courses_attached = ['Java', 'Базы данных']

print("Лекторы:")
print(f"1. {lecturer1.name} {lecturer1.surname}")
print(f"2. {lecturer2.name} {lecturer2.surname}")
print()

reviewer1 = Reviewer('Сергей', 'Сергеев')
reviewer1.courses_attached = ['Python', 'Django']

reviewer2 = Reviewer('Мария', 'Мариева')
reviewer2.courses_attached = ['Java', 'Базы данных']

print("Проверяющие:")
print(f"1. {reviewer1.name} {reviewer1.surname}")
print(f"2. {reviewer2.name} {reviewer2.surname}")
print()

print("=" * 50)
print("=" * 50)

print(f"\n{reviewer1.name} {reviewer1.surname} проверяет {student1.name} {student1.surname}:")
result1 = reviewer1.rate_hw(student1, 'Python', 9)
print(f"  Курс 'Python', оценка 9: {result1 if result1 else 'Успешно'}")

result2 = reviewer1.rate_hw(student1, 'Python', 10)
print(f"  Курс 'Python', оценка 10: {result2 if result2 else 'Успешно'}")

result3 = reviewer1.rate_hw(student1, 'Django', 8)
print(f"  Курс 'Django', оценка 8: {result3 if result3 else 'Успешно'}")

result4 = reviewer1.rate_hw(student1, 'Java', 7)
print(f"  Курс 'Java', оценка 7: {result4}")

print(f"\n{reviewer2.name} {reviewer2.surname} проверяет {student2.name} {student2.surname}:")
result5 = reviewer2.rate_hw(student2, 'Java', 8)
print(f"  Курс 'Java', оценка 8: {result5 if result5 else 'Успешно'}")

result6 = reviewer2.rate_hw(student2, 'Базы данных', 9)
print(f"  Курс 'Базы данных', оценка 9: {result6 if result6 else 'Успешно'}")

print(f"\n{student1.name} {student1.surname} оценивает лекции {lecturer1.name} {lecturer1.surname}:")
result7 = student1.rate_lecture(lecturer1, 'Python', 9)
print(f"  Курс 'Python', оценка 9: {result7 if result7 else 'Успешно'}")

result8 = student1.rate_lecture(lecturer1, 'Python', 10)
print(f"  Курс 'Python', оценка 10: {result8 if result8 else 'Успешно'}")

result9 = student1.rate_lecture(lecturer1, 'Git', 8)
print(f"  Курс 'Git', оценка 8: {result9 if result9 else 'Успешно'}")

print(f"\n{student2.name} {student2.surname} оценивает лекции {lecturer2.name} {lecturer2.surname}:")
result10 = student2.rate_lecture(lecturer2, 'Java', 8)
print(f"  Курс 'Java', оценка 8: {result10 if result10 else 'Успешно'}")

result11 = student2.rate_lecture(lecturer2, 'Базы данных', 9)
print(f"  Курс 'Базы данных', оценка 9: {result11 if result11 else 'Успешно'}")

print(f"\n{reviewer1.name} {reviewer1.surname}:")
print(reviewer1)

print(f"\n{reviewer2.name} {reviewer2.surname}:")
print(reviewer2)

print("\n--- Лекторы ---")
print(f"\n{lecturer1.name} {lecturer1.surname}:")
print(lecturer1)

print(f"\n{lecturer2.name} {lecturer2.surname}:")
print(lecturer2)

print("\n--- Студенты ---")
print(f"\n{student1.name} {student1.surname}:")
print(student1)

print(f"\n{student2.name} {student2.surname}:")
print(student2)

print("\nСравнение студентов:")
print(f"Студент1 > Студент2: {student1 > student2}")
print(f"Студент1 < Студент2: {student1 < student2}")
print(f"Студент1 == Студент2: {student1 == student2}")

print("\nСравнение лекторов:")
print(f"Лектор1 > Лектор2: {lecturer1 > lecturer2}")
print(f"Лектор1 < Лектор2: {lecturer1 < lecturer2}")
print(f"Лектор1 == Лектор2: {lecturer1 == lecturer2}")

print("\n" + "=" * 50)
print("=" * 50)

students_list = [student1, student2]
lecturers_list = [lecturer1, lecturer2]

print("\n1. Средняя оценка за домашние задания по курсу 'Python':")
avg_hw_python = average_grade_for_homework(students_list, 'Python')
print(f"   Средняя оценка: {avg_hw_python:.2f}")

print("\n2. Средняя оценка за домашние задания по курсу 'Java':")
avg_hw_java = average_grade_for_homework(students_list, 'Java')
print(f"   Средняя оценка: {avg_hw_java:.2f}")

print("\n3. Средняя оценка за домашние задания по курсу 'Git':")
avg_hw_git = average_grade_for_homework(students_list, 'Git')
print(f"   Средняя оценка: {avg_hw_git:.2f}")

print("\n4. Средняя оценка за лекции по курсу 'Python':")
avg_lect_python = average_grade_for_lectures(lecturers_list, 'Python')
print(f"   Средняя оценка: {avg_lect_python:.2f}")

print("\n5. Средняя оценка за лекции по курсу 'Java':")
avg_lect_java = average_grade_for_lectures(lecturers_list, 'Java')
print(f"   Средняя оценка: {avg_lect_java:.2f}")