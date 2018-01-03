import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import json
json_data = open("data3/target.json").read()
data = json.loads(json_data)

df = pd.DataFrame(data)
print(df)
df.convert_objects(convert_numeric=True).dtypes

for k in data.keys():
    print(data[k])
