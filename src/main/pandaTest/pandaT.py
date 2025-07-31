from operator import index

import pandas as pd


a=pd.DataFrame({'Yes':[50,21],'No':[10,20]})
print(a)

b=pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})
print(b)

c=pd.DataFrame({'YES':[10,20],'NO':[23,9]},index=['row1','row2'])
print(c)
print()
d=pd.Series([10,20,30,40,50,60])
print(d)