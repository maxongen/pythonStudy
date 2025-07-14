# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

class Person:
    def __init__(self,fname,lname):
      self.fname = fname
      self.lname = lname

    def printname(self):
        print(self.fname, self.lname)

x=Person("John","Doe")
x.printname()

class Student(Person):
    pass

x = Student("Mike", "Olsen")
print("inheritance : ")
x.printname()

class Student1(Person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)

x=Student1("Super","method")
x.printname()


