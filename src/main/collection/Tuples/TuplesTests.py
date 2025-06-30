# tuples declared using ()

tuple1=("test","test1","test2")
print("tuple1 is",type(tuple1))
print("tuple",tuple1)
print("length of tuple1 : ",len(tuple1))
print("-----create single obj tuple having , compulsory-----")
tuple2=("test",)
print("tuple2 is with one item",type(tuple2))
noTuple = ("apple")
print(type(noTuple))
print("------tuple constructor----------")
data="data1"
tupleConst=tuple(data)
print(type(tupleConst),tupleConst)
test=[1,2,3,4]
tupleConst=tuple(test)
print("converting list into tuple",tupleConst)
tuple2=("test","test1","test2")