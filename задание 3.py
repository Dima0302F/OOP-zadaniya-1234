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
            if not hasattr(lecturer, 'grades'):
                lecturer.grades = {}
            
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

print("\n1. Проверяющий (Reviewer):")
reviewer = Reviewer('Some', 'Buddy')
print(reviewer)
print()

print("2. Лектор (Lecturer):")
lecturer = Lecturer('Иван', 'Иванов')
lecturer.grades = {'Python': [9, 10, 8]}
print(lecturer)
print()

print("3. Студент (Student):")
student = Student('Ruoy', 'Eman', 'your_gender')
student.courses_in_progress = ['Python', 'Git']
student.finished_courses = ['Введение в программирование']
student.grades = {'Python': [9, 10, 9.5], 'Git': [8, 9]}
print(student)

lecturer1 = Lecturer('Иван', 'Иванов')
lecturer1.grades = {'Python': [9, 10, 8]}  

lecturer2 = Lecturer('Петр', 'Петров')
lecturer2.grades = {'Java': [8, 7, 9]}  

print(f"\nСравнение лекторов:")
print(f"Лектор1 > Лектор2: {lecturer1 > lecturer2}")
print(f"Лектор1 < Лектор2: {lecturer1 < lecturer2}")
print(f"Лектор1 == Лектор2: {lecturer1 == lecturer2}")

student1 = Student('Анна', 'Смирнова', 'Ж')
student1.grades = {'Python': [9, 10, 9]}  

student2 = Student('Дмитрий', 'Козлов', 'М')
student2.grades = {'Python': [8, 9, 8]}  

print(f"\nСравнение студентов:")
print(f"Студент1 > Студент2: {student1 > student2}")
print(f"Студент1 < Студент2: {student1 < student2}")
print(f"Студент1 == Студент2: {student1 == student2}")

student3 = Student('Ольга', 'Иванова', 'Ж')
student3.grades = {'Python': [9, 10, 9]}  

print(f"Студент1 == Студент3: {student1 == student3}")

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Введение в программирование']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_lecturer = Lecturer('Expert', 'Lecturer')
cool_lecturer.courses_attached += ['Python']

print("\nВыставляем оценки...")
result1 = cool_reviewer.rate_hw(best_student, 'Python', 10)
result2 = cool_reviewer.rate_hw(best_student, 'Python', 9)
result3 = cool_reviewer.rate_hw(best_student, 'Python', 10)

result4 = best_student.rate_lecture(cool_lecturer, 'Python', 9)
result5 = best_student.rate_lecture(cool_lecturer, 'Python', 10)
result6 = best_student.rate_lecture(cool_lecturer, 'Python', 8)

print("\nИнформация о проверяющем:")
print(cool_reviewer)

print("\nИнформация о лекторе:")
print(cool_lecturer)

print("\nИнформация о студенте:")
print(best_student)