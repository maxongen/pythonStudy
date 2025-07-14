class myClass:
    x=5

m=myClass()
print(m.x)


class mInit:
    def __init__(self,x,y):
        self.x=x
        self.y=y

p=mInit("john",39)
print(p.x)
print(p.y)
print(p)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)

class funTest:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def myfunc(self):
        return self.x+self.y

f1=funTest(1,2)
print("using function method :",f1.myfunc())

print("The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class")
print("It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class:")
class Person1:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person1("John", 36)
p1.myfunc()