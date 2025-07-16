x=400
print("local variable scope")
def myFunc():
    x=300
    print("local variable : ",x)

class MyClass:
    myFunc()

def funOuter():
    x=200
    def funInner():
        print("local variable in nested function : ",x)
    funInner()

class call:
    funOuter()

def funGlobalScopeVar():
    print("global scope variable",x)

funGlobalScopeVar()

def globalKeywordFunc():
    global y
    y=900

# for global keyword variable you need to call that method compulsory
globalKeywordFunc()

print("global keyword variable",y)

def myfunc1():
    x="jane"
    def myfunc2():
        nonlocal x
        x="hello"
    myfunc2()
    return x
# this overwrites to "jane" with "hello" due to nonlocal variable
print(myfunc1())