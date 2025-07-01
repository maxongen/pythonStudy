# sets are defined using { }

# Set items are unchangeable, but you can remove items and add new items.
# Sets are unordered, so you cannot be sure in which order the items will appear.

bikesSet={"hero", "honda", "bullet"}
print(type(bikesSet))
print(bikesSet)


fruitSet = {"apple", "banana", "cherry", "apple"}

print("duplicates are not allowed in sets - ",fruitSet)

print("Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:")
tSet={"apple", "banana", "cherry", True, 1, 2}
print(tSet)
print("Note: The values False and 0 are considered the same value in sets, and are treated as duplicates:")
tSet={"apple", "banana", "cherry", False, 0, 2}
print(tSet)
print("length of set - ",len(tSet))
print("set constructor")
data="this is set constructor"
cnSet=set(data)
print(cnSet)