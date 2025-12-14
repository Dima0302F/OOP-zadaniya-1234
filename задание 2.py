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

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}  

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

lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')

student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']

print(student.rate_lecture(lecturer, 'Python', 7))   
print(student.rate_lecture(lecturer, 'Java', 8))     
print(student.rate_lecture(lecturer, 'С++', 8))      
print(student.rate_lecture(reviewer, 'Python', 6))   

print(lecturer.grades) 

student2 = Student('Ruoy', 'Eman', 'your_gender')
student2.courses_in_progress += ['Python']

print(reviewer.rate_hw(student2, 'Python', 10))  
print(reviewer.rate_hw(student2, 'Java', 9))     
print(student2.grades)  