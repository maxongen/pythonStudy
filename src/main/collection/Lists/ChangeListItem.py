print("to change the value of a specific item, refer to the index number")
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

print("Change a Range of Item Values")
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

print("If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:")
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)