a=10
b=20
if a>b:
    print("a is greater than b")
elif a<b:
    print("a is less than b")
else:
    print("a is equal to b")


mahaDish=["daal","chapati","bhaji","bhat"]
northDish=["dosa","idli","meduVada"]

dish=input("Enter the dish you want: ")
if dish in mahaDish:
    print("Dish is Maharashtrian")
elif dish in northDish:
    print("Dish is North Indian")
else:
    print("Dish is not in Maharashtrian nor North Indian")
