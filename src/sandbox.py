from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import csv


df = pd.read_csv("../data/2019-20/gws/gw8.csv") # Loads on csv file
merged_df = pd.read_csv("../data/2019-20/gws/gw8.csv")

fig, ax1 = plt.subplots()
#ax2 = plt.subplots()
ax1.scatter(df['total_points'], df['value'], c=df['was_home'], s=df['threat'])
#ax1.scatter(df['selected'], df[''])
#ax2.bar(df['minutes'], df['GW'])

ax1.legend()
plt.show()