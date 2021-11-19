import pandas as pd
import numpy as np

df = pd.read_csv('data/dataframe_100x100.csv')
print(df.head())
print(df.tail())

x = df.drop('gender', axis = 1)
y = df['gender']

x_norm = x / 255.0 #normalization
y_encod = np.where(y=='female', 1, 0) #encoding
print(np.unique(y_encod))

print(x_norm.head())

np.savez('data/data_normalized_100x100.npz', x_norm, y_encod)