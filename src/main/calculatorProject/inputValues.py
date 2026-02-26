def get_inputs():
  operationVal=get_op_val()
  number1, number2 = get_number_input()
  return operationVal,number1, number2

operationList=["1","2","3","4"]

def get_op_val():
  while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    operationVal = input("Please select any option number(e.g. 1, 2, 3, 4) : ")
    if operationVal in operationList:
         return operationVal
    else:
        print("Invalid operation. Please select 1, 2, 3 or 4.")



def get_number_input():
  number1=get_number("Enter First Number : ")
  number2=get_number("Enter Second Number : ")
  return number1,number2

def get_number(message):
  while True:
    value=input(message)
    if value.strip()=="":
      print("Input cannot be empty")
      continue
    
    try:
      return float(value)
    except ValueError:
      print("Given input is not a number. Try again.")