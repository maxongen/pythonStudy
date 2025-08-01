import pandas as pd

json_data =pd.read_json('test.json')

print(json_data)


df =pd.read_csv('data.csv')
print(df.shape)
print("head method ")
print("print first 5 rows ")
print(df.head())
print(df.head(10))
print("last 5 rows ")
print(df.tail())
print("info")
print(df.info())

print("remove empty cells")
new_df=df.dropna()
print(new_df)