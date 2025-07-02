studentDict={"name":"hemant","age":18,"address":"Katraj","class":"pantBodh","rollNo":28,"year":2025}
print("remove item using pop(item) method")
studentDict.pop("year")
print(studentDict)
print("remove last added item using popitem()")
studentDict.popitem()
print(studentDict)
print("we can clear the dictionary using clear()")
studentDict.clear()
print(studentDict)
print("we can delete the dictionary using del ")
del studentDict
# print(studentDict) -- this will give error as dictionary is deleted