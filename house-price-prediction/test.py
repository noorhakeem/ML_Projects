import pandas as pd
import numpy as np

#dataset = pd.read_csv("data/Housing.csv")

#dataset = pd.read_csv("data/QDER628BIS.csv")

dataset = pd.read_csv("data/data.csv")

# configuring float numbers format
pd.options.display.float_format = '{:20.2f}'.format
print(dataset.head(n=5))    


print(dataset.describe(include=[np.number], percentiles= [.5]).transpose().drop("count", axis=1))