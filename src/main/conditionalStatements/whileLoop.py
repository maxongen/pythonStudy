i=1
while i<10:
    print(i)
    i+=1

print("while with break")
i=1
while i<10:
    print(i)
    if i==5:
        break
    i+=1

i=0
print("while with continue")
while i<6:
    i+=1
    if i==5:
        continue
    print(i)