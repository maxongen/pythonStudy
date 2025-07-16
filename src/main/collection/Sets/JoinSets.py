# There are several ways to join two or more sets in Python.
# The union() and update() methods joins all items from both sets.
# The intersection() method keeps ONLY the duplicates.
# The difference() method keeps the items from the first set that are not in the other set(s).
# The symmetric_difference() method keeps all items EXCEPT the duplicates.
import PythonSets

fruitSet = PythonSets.fruitSet

seasonSet={"winter", "spring", "summer","orange"}
set1=fruitSet.union(seasonSet)

print("----Union----")
print("return new set with all items - ",set1)
print("You can use the | operator instead of the union() method, and you will get the same result.")
set2=fruitSet | seasonSet
print("return new set with all items using | - ",set2)
print("Join Multiple Sets")
thingsSet={"Mountain", "River", "Stones"}
bikeSets={"Bullet", "I-smart", "Activa"}
set3=thingsSet | bikeSets | fruitSet | seasonSet
print("joining multiple sets - ",set3)
print("join other iterators like list, tuple, dictionaries")
tupleS=("Bullet", "I-smart", "Activa")
set4=fruitSet.union(tupleS)
print("union set with tuple - ",set4)

print("----Intersection----")
set4=fruitSet.intersection(seasonSet)
print("intersection set with fruit set - ",set4)
set4=fruitSet & seasonSet
print("intersection set using & - ",set4)
print("The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.")
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)

print("-------Difference-----------")
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3=set1.difference(set2)
print(set3)

print("You can use the - operator instead of the difference() method, and you will get the same result.")
set3=set1-set2
print(set3)
print("The difference_update() method will also keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.")
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)
print(set1)

print("------Symmetric Differences---------------")
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3=set1.symmetric_difference(set2)
print(set3)
print("You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.")
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3=set1 ^ set2
print(set3)
print("The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.")
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)