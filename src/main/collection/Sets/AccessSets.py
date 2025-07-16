import PythonSets

fruitSet = PythonSets.fruitSet

print("access set using loop(for or while)")
for fruit in fruitSet:
    print(fruit)

print("banana" in fruitSet)
print("banana" not in fruitSet)

print("------iterator in sets---------")
myItr=iter(fruitSet)
print(next(myItr))
print(next(myItr))
print(next(myItr))
