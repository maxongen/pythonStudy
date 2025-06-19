textVal="ice cream"
print(textVal)
print("using index print string, 0th position",textVal[0])
# Strings are immutable in python once you create it will not change
# textVal[0]="t" will not work it will throw error

# String using index range
print(textVal[0:3]) #it will print ice, first index included, second will exclude

print(textVal[4:]) #this will omit index, it will start from 4th index and print till last index - cream
print(textVal[:3]) #this will print from beginning to till 3rd index - ice

# String can be declared using single as well as double quote
textVal='This is single quoted string'
print(textVal)
textVal="let's play"
print(textVal)
textVal='double quote in single "quote"'
print(textVal)
# we can declare multiline string using triple quote
textVal='''This is multiline string
which contains 3 lines
line1
line2
line3'''
print(textVal)
# String concat
string1="string1 "
string2="string2 "
string3=string1+string2
print("string concat : "+string3)