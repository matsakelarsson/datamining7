from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import csv

#print(os.listdir("../fpl-data")) # Prints all csv files
df = pd.read_csv("../data/2019-20/gws/gw8.csv") # Loads on csv file
#print(df.head()) # Prints the head of the loaded csv-file
df.index += 1
df['100 adj'] = df['total_points'].rolling(window=100).mean()
print(df.head())
print(df.index)
ax1 = plt.subplot2grid((6,1), (0, 0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5, 0), rowspan=1, colspan=1,)
ax1.scatter(df['selected'], df['total_points'])
ax1.scatter(df['selcted'], df[''])
ax2.bar(df['minutes'], df['GW'])

plt.show()
