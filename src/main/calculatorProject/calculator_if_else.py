operationVal=input("Please select any option number(e.g. 1, 2, 3, 4) : ")
number1=float(input("Enter First Number : "))
number2=float(input("Enter Second Number : "))


if operationVal=="1":
  print("Addition of ",number1," and ",number2)
  number3=number1+number2
  print("Addition : ",number3)
elif operationVal=="2":
  print("Substraction of ",number1," and ",number2)
  number3=number1-number2
  print("Substraction : ",number3)
elif operationVal=="3":
  print("Multiplication of ",number1," and ",number2)
  number3=number1*number2
  print("Multiplication : ",number3)
elif operationVal=="4":
  print("Division of ",number1," and ",number2)
  number3=number1/number2
  print("Division : ",number3)
else:
  print("provided wrong operation type")

