class Student:
    add = 'Hai Duong'
    __phone ='0339365888'
    def __init__(self,name):
        self.name = name
    def setAge(self,age):
        self.age = age
    def getAge(self):
        return self.age
    def display(self):
        return self.name + " , "+str(self.age)+" , "+self.add
    def setphone(self,phone):
        self.__phone=phone
        print(self.__phone)
    def __str__(self):
        return self.name + " , "+str(self.age)+" , "+self.add
stu = Student('khai')
stu.setAge(22)
#print(stu.display())
stu.setphone('016678589')
# print(stu._Student__phone) #cach hien thi bien bi dau
print(stu)