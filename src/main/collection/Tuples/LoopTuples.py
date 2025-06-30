fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
for item in fruits:
    print(item)

print("using range()")
for item in range(1,3):
    print(item)

print("using range() and len()")
for item in range(len(fruits)):
    print(item)

print("using len()")
i=0
while i < len(fruits):
    print(fruits[i])
    i+=1
