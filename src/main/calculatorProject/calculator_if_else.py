from inputValues import get_inputs_operation_val,get_number_input

operationVal = get_inputs_operation_val()
number1, number2 = get_number_input()

 
if operationVal=="1":
  print("Addition of ",number1," and ",number2)
  print("Addition : ",number1+number2)
elif operationVal=="2":
  print("Substraction of ",number1," and ",number2)
  print("Substraction : ",number1-number2)
elif operationVal=="3":
  print("Multiplication of ",number1," and ",number2)
  print("Multiplication : ",number1*number2)
elif operationVal=="4":
  print("Division of ",number1," and ",number2)
  print("Division : ",number1/number2)
else:
  print("provided wrong operation type")


