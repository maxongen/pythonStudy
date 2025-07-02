print("Using the append() method to append an item")

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

print("To insert a list item at a specified index, use the insert() method.")
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

print("To append elements from another list to the current list, use the extend() method.")
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

print("Add Any Iterable")
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)