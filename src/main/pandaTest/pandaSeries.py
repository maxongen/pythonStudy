import pandas as pd

a=[1,2,3]
myvar=pd.Series(a)
print(myvar)

print("labels")
print(myvar[0])
print("--------")
print(myvar.dtypes)
print(myvar.describe())
print(myvar.shape)
print(myvar.index)
print(myvar.values)


print("with index argument you can name your own labels")
myvar=pd.Series(a,index=["a","b","c"])
print(myvar)
print(myvar["a"])

print("key value objects in series")
cal={"day1":420,"day2":430,"day3":440}
vals=pd.Series(cal)
print(vals)

myvar = pd.Series(cal, index = ["day1", "day2"])
print(myvar)