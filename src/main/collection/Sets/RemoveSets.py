fruitSet = {"apple", "banana", "cherry", "orange"}

print("remove method will remove item from set but if its not present it will throw error")
fruitSet.remove("banana")
print(fruitSet)

print("discard method will remove item from set but if its not present it will not throw error")
fruitSet.discard("orange")
print(fruitSet)
fruitSet.discard("banana")
print("trying to remove banana which is already removed ",fruitSet)

# Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.
print("remove random item from set")
fruitSet.pop()
print(fruitSet)

print("empty the set using clear method")
fruitSet.clear()
print(fruitSet)

print("delete set using del method")
del fruitSet
# print(fruitSet) - this line will throw error
