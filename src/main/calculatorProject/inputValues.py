def get_inputs():
  operationVal=input("Please select any option number(e.g. 1, 2, 3, 4) : ")
  number1=get_number("Enter First Number : ")
  number2=get_number("Enter Second Number : ")

  return operationVal,number1,number2

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