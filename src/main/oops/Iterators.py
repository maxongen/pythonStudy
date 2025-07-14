fruitSet=("apple","banana","orange","strawberry","pineapple")
print("-------- iterator ------")
fruitSetIterator=iter(fruitSet)
print(next(fruitSetIterator))
print(next(fruitSetIterator))
print(next(fruitSetIterator))
print(next(fruitSetIterator))

print("create custom iterator")
class MyNumbers:
    def __init__(self,num):
        self.num=num
    def __iter__(self):
        return self
    def __next__(self):
        return self.num
    def __reversed__(self):
        return reversed(self.num)
    def __eq__(self, other):
        return self.num == other
    def __add__(self, other):
        return self.num + other
    def __sub__(self, other):
        return self.num - other
    def __mul__(self, other):
        return self.num * other

x= MyNumbers(5)
print(x.__next__())

print("my custom iterator")
class MyNumbers2:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a <=20:
            x=self.a
            self.a+=1
            return x
        else:
            raise StopIteration
myClass=MyNumbers2()
myIter=iter(myClass)

for x in myIter:
    print(x)

