studentDict={"name":"hemant","age":18,"address":"Katraj","class":"pantBodh","rollNo":28,"year":2025}

print("copy dictionary using copy() method")
studentDictNew=studentDict.copy()
print(studentDictNew)

print("using constructor we can copy the dictionary")
studentDictNew=dict(studentDict)
print(studentDictNew)