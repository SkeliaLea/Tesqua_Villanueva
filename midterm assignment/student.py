from person import Person

class Student(Person):
    def __init__(self,idno,lastname,firstname,age,course,level):
        super().__init__(lastname,firstname,age)
        self.idno=idno
        self.lastname=lastname
        self.firstname=firstname
        self.age=age
        self.course=course
        self.level=level
        
        
    def displayStudent(self):
        print(self.idno,end=" ")
        print(self.lastname,end=" ")
        print(self.firstname,end=" ")
        print(self.age,end=" ")
        print(self.course,end=" ")
        print(self.level)


