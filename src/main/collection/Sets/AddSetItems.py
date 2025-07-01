fruitSet = {"apple", "banana", "cherry", "apple"}

fruitSet.add("orange")
print("add method - ",fruitSet)

print("add two sets together")

seasonSet={"winter", "spring", "summer"}
fruitSet.update(seasonSet)
print("update method - ",fruitSet)

print("add any iterable like list, set, tuple, dictionary")
lst = [1,2,3,4,5]
fruitSet1 = {"tata", "birla", "reliance", "bata"}
fruitSet1.update(lst)
print(" update method for list - ",fruitSet1)
tupleT=("a","b","c")
fruitSet1 = {"mountain", "river", "trees", "stones"}
fruitSet1.update(tupleT)
print(" update method for tuple - ",fruitSet1)
fruitSet1 = {"fr1", "fr2", "fr3", "fr4"}
dictionaryT={"age":25,"class":9,"schoolRno":28}
fruitSet1.update(dictionaryT)
print(" update method for dictionary - ",fruitSet1)

