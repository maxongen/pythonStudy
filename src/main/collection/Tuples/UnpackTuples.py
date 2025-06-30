print("------------Unpack Tuple --------------")
tuple1=("test","test1","test2")
# in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
(aaa,bbb,ccc)=tuple1
print(aaa)
print(bbb)
print(ccc)

print("--------Using Asterisk*------------")
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green,red,*yellow)=fruits
print(green)
print(red)
print(yellow)

# If the asterisk is added to another variable name than the last,
# Python will assign values to the variable until the number of values left matches the number of variables left.
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green,*red,yellow)=fruits
print(green)
print(red)
print(yellow)