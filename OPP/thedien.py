class Person:
    def display(self):
        print("Lop Cha")
class Student(Person):
    def display(self):
        print("Lop Con")
print(issubclass(Student,Person)) #True
print(issubclass(Person,Student)) #False

p = Person()
s = Student()
print(isinstance(s,Person)) #True
print(isinstance(p,Student)) #False