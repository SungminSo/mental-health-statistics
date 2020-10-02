import pandas as pd

data = pd.read_csv('chs19_seoul_sample.csv', 'r', encoding='latin', delimiter=',', low_memory=False)
print(data.describe())

print(data.groupby('signgu_code').describe())
