import datetime

x=datetime.datetime.now()
print(x)
print(x.strftime("%A"))
print(x.strftime("%d/%m/%Y"))
print(x.strftime("%d/%m/%Y %H:%M:%S"))

y=datetime.datetime(2020,5,17,12,20,10)
print(y)
