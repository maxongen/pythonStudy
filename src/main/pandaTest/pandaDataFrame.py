from operator import index

import pandas as pd


a=pd.DataFrame({'Yes':[50,21],'No':[10,20]})
print(a)

b=pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})
print(b)

c=pd.DataFrame({'YES':[10,20],'NO':[23,9]},index=['row1','row2'])
print(c)
print()


dataset={'cars':["BMW","VOLVO","FORD","JAGUAR"],'passing':[20,30,40,50]}
myframe=pd.DataFrame(dataset)
print(myframe)
print(myframe.columns)
print(myframe.index)
print(myframe.shape)
print(myframe.values)

print("locate row")
print(myframe.loc[1])

print(myframe.loc[[0,1,2]])
for row in myframe.itertuples(index=False):
    print(row.cars,row.passing)

for idx,row in myframe.iterrows():
    print(idx,row.cars,row.passing)


print("index")

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df)
