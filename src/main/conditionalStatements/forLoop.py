fruits=["apple","banana","orange"]

for fruit in fruits:
    print(fruit)

for fruit in "pinaple":
    print(fruit)

for fruit in fruits:
    print(fruit)
    if fruit=="banana":
        print("break statement")
        break

for fruit in fruits:
    print(fruit)
    if fruit=="banana":
        print("continue statement")
        continue

for fruit in range(6):
    print(fruit)

for i in range(len(fruits)):
    print("fruit",i,fruits[i])

#range
for i in range(2,30,3):
    print(i)
else:
  print("Finally finished!")

#if loops has no content then to avoid error use pass
for i in [1,2,3]:
    pass

for i in range(2,6):
    print(i)
