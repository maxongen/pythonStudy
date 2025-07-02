studentDict={"name":"hemant","age":18,"address":"Katraj","class":"pantBodh","rollNo":28,"year":2025}
print("loop using for loop \n---------")
for std in studentDict:
    print(std)

print("---------\n using values() method we can get values")
for std in studentDict.values():
    print(std)

print("---------\n using keys() method we can get keys")
for std in studentDict.keys():
    print(std)

print("---------\n using items() method we can get items")
for std in studentDict.items():
     print(std)