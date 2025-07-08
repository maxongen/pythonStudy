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