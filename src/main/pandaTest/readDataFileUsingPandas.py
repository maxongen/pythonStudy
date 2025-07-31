import pandas as pd

json_data =pd.read_json('test.json')

print(json_data)


csv_data =pd.read_csv('data.csv')
print(csv_data.shape)