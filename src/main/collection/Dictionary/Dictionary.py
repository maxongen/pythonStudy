# Dictionaries are key and value pairs
# they are declared in { }
# Dictionary items are ordered, changeable, and do not allow duplicates.

studentDict={"name":"hemant","age":18,"address":"Katraj","rollNo":28}
print(type(studentDict))
print(studentDict)
print("dictionary items can be accessed by key name : ",studentDict["name"])

# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# duplicate keys are not allowed in dictionary
print("dictionary length : ",len(studentDict))
print("dictionary items are any type of data")
carDict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(carDict)
lst=["apple","banana","cherry"]
print("dictionary constructor ")
dictConstructor=dict(name = "John", age = 36, country = "Norway")
print(dictConstructor)