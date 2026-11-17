#OOP
#Classes
# class Student:
#     def __init__(self, students_name, students_age):
#         self.name = students_name
#         self.age = students_age

# new -> {} -> {}.constructor -> {name: 'Alex', age: 20}
# __new__.__init__
# student_1 = Student('Alex', 20)
# student_2 = Student('Alice', 21)
#
# print(student_1.age, student_1.name, student_2.name)
#Abstraction
#Inheritance
#Encapsulation
#private protected public
#Polymorphism
class Person:
    def __init__(self, name, age, is_admin):
        self.name = name
        self.age = age
        self.__is_admin = is_admin

    def introduce(self):
        print(f'My name is {self.name}, my age is {self.age}')


def logger(func):
    def wrapper(*args, **kwargs):
        print('function started')
        func(*args, **kwargs)
        print('function ended without errors')

    return wrapper

class Student(Person):
    def __init__(self, student_id, name, age, grade, is_admin):
        super().__init__(name, age, is_admin)
        self.__student_id = student_id
        self._grade = grade

    def __str__(self):
        return f'This is student. Student has {self._grade}!'

    def __add__(self, other):
        return self._grade + other._grade

    def study(self):
        print(f'{self.name} is studying!')

    @logger
    def introduce(self):
        print(f'My name is {self.name}, here is my student id: {self.__student_id}')

    def set_student_id(self, new_student_id):
        self.__student_id = new_student_id

    def get_student_id(self):
        return self.__student_id

    @property
    def grade(self):
        return f'students grade is {self._grade}'

    @grade.setter
    def grade(self, new_grade):
        if new_grade > 50:
            self._grade = new_grade


class Teacher(Person):
    def __init__(self, teacher_id, name, age, u_class, is_admin):
        super().__init__(name, age, is_admin)
        self.teacher_id = teacher_id
        self.u_class = u_class

    def introduce(self):
        print(f'My name is {self.name}, here is my teacher id: {self.teacher_id}')


#__new__.__init__(Person) -> {}.__init__(self) -> {name, age, introduce, study} -> student
#student.study -> {name, age, introduce, study}.self
#__new__.__init__(Student) -> {}__init__(Person) -> {name, age, introduce}-->self -> {name, age, introduce, study, student_id}
student = Student('786987976GHGfre', "Bob", 20, 80, False)
student_2 = Student('786987976GHGfre', "Alice", 20, 96, False)

teacher = Student('121976GHGfasdfre', "Alice", 30, 90, False)
anonim = Person('Anon', 20, True)

# student.set_grade(90)
# print(f'students id: {student.get_student_id()}, students grade: {student.get_grade()}')

student.set_student_id('asdjklfhha^AS6')
print(f'New student id: {student.get_student_id()}')

print(student.grade)
student.grade = 90
print(student.grade)

student.introduce()
teacher.introduce()
anonim.introduce()
print(student + student_2)

#Dunder methods
#Decorators
#Game
@logger
def create_user(name, surname, age):
    print(f'create user with params: {name}, {surname}, {age}')

@logger
def delete_user():
    print('delete user')

@logger
def buy_tokens():
    print('buying tokens')

create_user('Alex', 34, 45)
delete_user()
buy_tokens()

####----------######

def admin_check(func):
    def wrapper(self, *args, **kwargs):
        if self.role != 'admin':
            print("You don't have rights to do this")
            return

        return func(self, *args, **kwargs)

    return wrapper

class UniversitySystem:
    def __init__(self, role):
        self.role = role
        self.students = []

    def add_student(self, name):
        self.students.append(name)
        print(f"Student added: {name}")

    @admin_check
    def delete_student(self, name):
        self.students.remove(name)
        print(f"Student removed: {name}")

user = UniversitySystem('Dean')
user.add_student('Alex')
user.delete_student('Alex')

admin = UniversitySystem('admin')
admin.add_student('Alex')
admin.delete_student('Alex')