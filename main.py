import numpy as np #komputasi numerik
import matplotlib as plt #visualisasi
import pandas as pd #input file external

dataset = pd.read_csv("Social Network Ads.csv")
x = dataset.iloc[:, [2,3]].values
y = dataset.iloc[:, -1].values
print(x)

