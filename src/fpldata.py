from mpl_toolkits.plot3d import Axes3d
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import csv

print(os.listdir("../fpl-data")) # Prints all csv files
df = pd.read_csv("../fpl-data/FPL_2018_19_Wk0.csv") # Loads on csv file
print(df.head()) # Prints the head of the loaded csv-file
