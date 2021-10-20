class Person:
    def __init__(self,name,age,add):
        self.name = name
        self.age = age
        self.add = add
    def salary(self):
        return '1000$'
    def isPerson(self):
        return True
    def __str__(self):
        return self.name + " , " + str(self.age) + " , " + self.add

class Student(Person):
    def __init__(self,name,age,add,school,gpa):
        Person.__init__(self,name,age,add)
        self.school = school
        self.gpa = gpa
    def setSkill(self,skill):
        self.skill = skill
    def __str__(self):
        return self.name + " , " + str(self.age) + " , " + self.add+" , "+self.school+" , "+str(self.gpa)
    def isStudent(self):
        return True
person = Person("Xoa",40,"Hai Duong")
student = Student("Vu Van Khai",22,"Hai Duong",'Ptit',2.8)
print(student.isPerson())
print(student)
print(student.salary())
student.setSkill("Toiec 555")
print(student.skill)