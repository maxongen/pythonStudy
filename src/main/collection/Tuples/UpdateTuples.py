print("------------Update Tuple Items--------------")
tuple1=("test","test1","test2")
# Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.
# But there are some workarounds.
print("--------Change Tuple Values--------")
print("tuple before update - ",tuple1)
lstTuple=list(tuple1)
lstTuple[0]="Banana"
lstTuple[1]="Apple"
lstTuple[2]="Orange"
tuple1=tuple(lstTuple)
print("tuple updated using list - ",tuple1)

print("--------Add Items --------")
print("tuple before Insert - ",tuple1)
lstTupleAdd=list(tuple1)
lstTupleAdd.insert(4,"Pineapple")
tuple1=tuple(lstTupleAdd)
print("tuple after insert using list - ",tuple1)
lstTupleAdd=list(tuple1)
lstTupleAdd.append("Jackfruit")
tuple1=tuple(lstTupleAdd)
print("tuple after append using list - ",tuple1)
print("--------Add tuple to a tuple --------")
y = ("Litchi","Pomegranate")
tuple1+=y
print("tuple after adding another tuple",tuple1)

print("--------Remove Items--------")
lstTupleRemove=list(tuple1)
lstTupleRemove.remove("Litchi")
tuple1=tuple(lstTupleRemove)
print("tuple after remove using list - ",tuple1)
print("--------delete the tuple completely--------")
del tuple1
# this will give error print(tuple1)




