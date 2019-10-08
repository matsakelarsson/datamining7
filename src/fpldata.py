from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import csv


df = pd.read_csv("../data/2019-20/gws/merged_gw.csv") # Loads on csv file


df['100 adj'] = df['total_points'].rolling(window=100).mean()

ax1 = plt.subplot2grid((6,1), (0, 0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5, 0), rowspan=1, colspan=1,)
ax1.scatter(df['selected'], df['total_points'])

#ax1.scatter(df['selected'], df[''])
#ax2.bar(df['minutes'], df['GW'])

plt.show()
