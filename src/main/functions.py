def my_function():
    print("simple function")

my_function()


def my_parameterized_fun(test):
    print("parameterized function - ",test)

my_parameterized_fun("function1")

lst=["apple","banana","orange"]
my_parameterized_fun(lst)

def multi_parametrized_fun(param1, param2):
    print("param 1 - ",param1,"param2 - ",param2)

multi_parametrized_fun("test","test2")
# multi_parametrized_fun("ttt") - it will throw error

def multi_param_fun_ast(*test):
    print("param 1 - ",test[0],test[1])
multi_param_fun_ast("test","test2")
multi_param_fun_ast("a","b","c")

def keyword_fun(a,b,c):
    print("keyword - ",a,b,c)

keyword_fun(a=10,b=20,c=30)

def arbitary_fun(**a):
    print("arbitary - ",a["lname"])
arbitary_fun(fname="test",lname="test")