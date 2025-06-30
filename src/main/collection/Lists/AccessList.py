lst1 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(lst1[1])

print("------Negative Indexing------")
# Negative indexing means start from the end
# -1 refers to the last item, -2 refers to the second last item etc.
print(lst1[-1])
print("----list range-------")
print("Range of Indexes 2 to 5 ",lst1[2:5])
print("By leaving out the start value",lst1[:4])
print("By leaving out the end value",lst1[2:])
print("Range of Negative Indexes -4 to -1",lst1[-4:-1])
print("---- Check if Item Exists -----")
if "apple" in lst1:
  print("Yes, 'apple' is in the fruits list")
