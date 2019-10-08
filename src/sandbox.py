from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import csv
from sklearn.cluster import KMeans

def no_clusters(data,a,b):
    '''to find the number of clusters for the k means algorithm'''
    SSE = []
    clusters = range(a,b)
    for k in clusters:
        SSE.append(KMeans(n_clusters=k).fit(data).inertia_)
    plt.plot(clusters, SSE, '-x')
    plt.xticks(clusters)
    plt.xlabel('Number of clusters')
    plt.ylabel('Sum of Squared Distances (SSD)')
    plt.title('KMeans Elbow Method')
    plt.rcParams['figure.figsize']=(8,7)


def no_instances(data,Class):
    print(str(Class)+ ' split')
    no_class = pd.value_counts(data[Class]).sort_index()
    print(no_class)
    plt.bar(no_class.index, no_class, align = 'center')
    plt.title('Instances in each class for '+str(Class))
    plt.xticks(no_class.index)
    plt.savefig(str(Class)+'.png')
    plt.show()
    print('\n')


df_gw8 = pd.read_csv("../data/2019-20/gws/gw8.csv") # Loads on csv file
#df1 = pd.read_csv("../data/2019-20/gws/gw7.csv")

df = pd.concat((pd.read_csv(f) for f in ["../data/2019-20/gws/gw1.csv", "../data/2019-20/gws/gw2.csv", "../data/2019-20/gws/gw3.csv", "../data/2019-20/gws/gw4.csv", "../data/2019-20/gws/gw5.csv", "../data/2019-20/gws/gw6.csv", "../data/2019-20/gws/gw7.csv", "../data/2019-20/gws/gw8.csv"]), ignore_index=True)
df1 = df.groupby('name', as_index=False)['total_points'].sum()
df2 = df.groupby('name', as_index=False)['minutes'].sum()
df3 = df.groupby('name', as_index=False)['goals_scored'].sum()


df1 = df1.rename(columns = {"total_points":"combined_points"}) 
df2 = df2.rename(columns = {"minutes":"combined_minutes"}) 
df3 = df3.rename(columns = {"goals_scored":"combined_scored"}) 


df_merged = pd.merge(df1, df_gw8, how='inner', on=['name'])
df_merged = pd.merge(df2, df_merged, how='inner', on=['name'])
df_merged = pd.merge(df3, df_merged, how='inner', on=['name'])
df_merged.to_csv('combined.csv')



x = df_merged[['combined_points','value']]
no_clusters(x,1,8)


kM6 = KMeans(n_clusters=6, random_state = 1)
df_merged['KMeans6'] = kM6.fit_predict(x)


fig, ax1 = plt.subplots()
#ax2 = plt.subplots()
ax1.scatter(df_merged['combined_points'], df_merged['value'], c=df_merged['combined_scored'])
#ax1.scatter(df['selected'], df[''])
#ax2.bar(df['minutes'], df['GW'])


#ax1.legend()


no_instances(df_merged,'KMeans6')


centroids2 = kM6.cluster_centers_
plt.scatter(df_merged['combined_points'], df_merged['value'], c = df_merged.KMeans6) 
plt.scatter(centroids2[:,0],centroids2[:,1], marker = 'x', s = 150, linewidths = 5, c = 'r')
plt.title('Premier League - K = 6')
plt.xlabel('combined points')
plt.ylabel('value')
plt.show()
