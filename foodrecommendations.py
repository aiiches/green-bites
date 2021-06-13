"""Importing Libraries"""

#for data frame processing
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

#for user's consolemenu
from consolemenu import *
from consolemenu.items import *

#for plotting
#import matplotlib.pyplot as plt
#import plotly.express as px
#import seaborn as sns

# for 3D projection
from sklearn.preprocessing import StandardScaler
from mpl_toolkits.mplot3d import Axes3D

#for clustering
from sklearn.cluster import KMeans
from k_means_constrained import KMeansConstrained
from scipy.spatial import distance
from scipy.spatial.distance import cdist
from sklearn.neighbors import NearestNeighbors


#reading data from csv file using pandas
df=pd.read_csv('co2_data.csv')

"""Examining and Learning about the features of the dataframe"""

#getting general idea about data frame (df)
df.describe()
df.head()

#to know data types in df
df.info()

#convert all data types to float
cols = ['Energy_kcal', 'VitA_mcg', 'Folate_mcg', 'Calcium_mg','Magnesium_mg', 'Phosphorus_mg']
for col in cols:
   df[col] = df[col].apply(lambda x: float (x) if x == x else "")

#checking data type conversion
df.info()

"""Data Normalization"""

"""
* preparing data for normalization to keep values between 0 and 1
* using MinMaxScaler class available in the Scikit-learn library
* min-max approach rescales the feature to a fixed range of [0,1]
* Xnorm = X - Xmin / Xmax - Xmin
"""
#selecting numerical values in df only
df_num = df.select_dtypes(include=[np.number])

#to keep Footprint value out of normalization
df_num_1 = df_num.drop(['Footprint'], axis = 1)

#verifying changes
df_num_1.head()

"""
* Data normalization using MinMaxScaler
* To keep values between 0 and 1
* This is a better approach for clustering
"""
# create a scaler object
scaler = MinMaxScaler()

# fit and transform the data
df_num_1 = pd.DataFrame(scaler.fit_transform(df_num_1), columns=df_num_1.columns)

#assign normalized values back to the original df
df[df_num_1.columns] = df_num_1

#verifying changes
df.head()

"""#Data visualization"""
"""
#displaying data frame in Axes
fig, ax = plt.subplots(figsize = (15, 10))
sns.heatmap(df.corr(), annot = True, 
            fmt = ".2f", 
            cmap = 'coolwarm',
            cbar_kws = {"shrink": .8})

#displaying distribution of all nutritions in items
plt.rcParams["figure.figsize"] = (20, 18)
df.hist()

#closer look at footprint  distribution in items
sns.displot(df, x='Footprint')
plt.title("Carbon footprint distribution of food items")

#displaying nutrition to footprint relation for all items
data = df.drop(['Item', 'Footprint'], axis = 1)
for dato in data:
    fig = px.scatter(df, x = 'Footprint', y = dato,
                    size = dato, color = 'Item')
    fig.show()
"""

"""K-Mean Clustering"""

#droping features we do not want to cluster based on
# X1 has the clustering features (Energy_kcal, Protein_g, Fat_g, Carb_g, Sugar_g, Fiber_g, Calcium_mg, Iron_mg, Magnesium_mg, VitC_mg)

X1 = df.drop(['Item', 'Footprint', 'VitA_mcg', 'VitB6_mg', 'VitB12_mcg','VitE_mg', 'Folate_mcg', 'Niacin_mg', 'Riboflavin_mg', 'Thiamin_mg', 'Copper_mcg', 'Manganese_mg', 'Phosphorus_mg'], axis = 1)


#for i in range(1,40):
kmeans = KMeansConstrained(n_clusters=40, size_min=4, size_max=8, init='k-means++', n_init=10, max_iter=50, verbose=False, tol=1e-4, random_state=42)
kmeans.fit_predict(X1)

#compiling data frame with new values
X1['Cluster_ID'] = pd.DataFrame(kmeans.labels_)
#assign values back to the original df
df[X1.columns] = X1
#saving df to csv
df.to_csv('cluster_food.csv')

#to show number of items in each cluster
df['Cluster_ID'].value_counts()

"""K-means Clustering - 1. Elbow method to find optimal K number of clsters"""

"""
KMeans clustering arguments

* WCSS: ( Within-Cluster Sum of Square distance between each point and the centroid in a cluster)
* n_clusters: is number of clusters decided by elbow method
* init: is the method for initializing the centroid
* k-means++: for smarter initialization of centroids
* max_iter: maximum number of iterations of the k-means algorithm for a single run
* n_init: Number of time the k-means algorithm will be run with different centroid seeds (defult is 10)
* random_state: determines random number generation for centroid initialization
"""

#droping features we do not want to cluster based on
# X1 has the clustering features (Energy_kcal, Protein_g, Fat_g, Carb_g, Sugar_g, Fiber_g, Calcium_mg, Iron_mg, Magnesium_mg, VitC_mg)

X1 = df.drop(['Item', 'Footprint', 'VitA_mcg', 'VitB6_mg', 'VitB12_mcg','VitE_mg', 'Folate_mcg', 'Niacin_mg', 'Riboflavin_mg', 'Thiamin_mg', 'Copper_mcg', 'Manganese_mg', 'Phosphorus_mg'], axis = 1)

#using the Elbow method to find the optimal K value (number of clsters).
wcss = []
for i in range(1,20):
    kmeans = KMeans(n_clusters=i,init='k-means++',max_iter=10,n_init=10,random_state=42)
    kmeans.fit(X1)
    wcss.append(kmeans.inertia_)

#plot the WCSS with K value
#the plot looks like an Elbow. 
#As the number of clusters increases, the WCSS value will start to decrease
#The point at which the elbow shape is created is 4, that is, our K value or an optimal number of clusters is 4.
"""
plt.plot(range(1,20),wcss, linewidth = 2, markersize = 12, marker='o')
plt.title('The Elbow Curve')
plt.xlabel('Number of Clusters')
plt.ylabel('Sum of Squares Within Cluster ')
plt.savefig('elbow.png')
plt.show()
"""

"""K-means Clustering - 2. KMeansConstrained with min max cluster size"""
kmeans = KMeansConstrained(n_clusters=36, size_min=5, size_max=8, init='k-means++', n_init=10, max_iter=50, verbose=False, tol=1e-4, random_state=42)
kmeans.fit_predict(X1)


#Printing centroids
centroids = kmeans.cluster_centers_
print(centroids)

"""
#Visualizing Clusters
labels = kmeans.predict(X1)
C = kmeans.cluster_centers_
colors = ['red', 'cornsilk', 'green', 'yellow', 'orange', 'black', 'gray', 'pink', 'purple', 'teal', 'cyan', 'olive', 'brown', 'white', 'tomato', 'teal', 'firebrick', 'violet', 'sienna', 'peru', 'tan', 'beige', 'lavender', 'bisque', 'silver', 'gold', 'chocolate', 'lightpink', 'crimson', 'hotpink', 'plum', 'ivory', 'salmon', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
assign = []

for row in labels:
    assign.append(colors[row])

#figure 1
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(X1.iloc[:, 0], X1.iloc[:, 1], X1.iloc[:, 2], c=assign, s=60)
ax.scatter(C[:, 0], C[:, 1], C[:, 2], marker='*', s=1000)

#figure 2
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(X1.iloc[:, 3], X1.iloc[:, 4], X1.iloc[:, 5], c = assign, s = 60)
ax.scatter(C[:, 0], C[:, 1], C[:, 2], marker = '*', s = 1000)

#figure 3
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(X1.iloc[:, 6], X1.iloc[:, 7], X1.iloc[:, 8], c = assign, s = 60)
ax.scatter(C[:, 0], C[:, 1], C[:, 2], marker = '*', s = 1000)

#showing how many items per colour
copy = pd.DataFrame()
copy['Item'] = df['Item'].values
copy['Footprint'] = df['Footprint'].values
copy['label'] = labels
amount = pd.DataFrame()
amount['color'] = colors
amount['amount'] = copy.groupby('label').size()
amount
"""

"""compiling data frame with new values"""

#adding cluster_ID column to X1
X1['Cluster_ID'] = pd.DataFrame(kmeans.labels_)

#assign values back to the original df
df[X1.columns] = X1

#saving df to csv
df.to_csv('cluster_food.csv')

#to show number of items in each cluster
df['Cluster_ID'].value_counts()

"""User's console view"""

#getting users input
food_choice = input("Enter a Food Item: ")

def recomandation(food_choice):
  food_choice = food_choice.lower()
  df_user_choice = df.loc[df['Item'] == food_choice]
  user_choice_carbon_footprint = float(df_user_choice['Footprint'])
  df_same_cluster = df.loc[df['Cluster_ID'] == int(df_user_choice['Cluster_ID'])]
  df_lower_CFP = df_same_cluster.loc[df_same_cluster['Footprint'] < user_choice_carbon_footprint]
  if len(df_lower_CFP) == 0:
    print('Great choice!')
  else:
    print('\n')
    print(food_choice + ': has a carbon footprint of {} GHG'.format('%.2f'%user_choice_carbon_footprint))
    print('\n')
    print('Here is a list of items with lower carbon footprint:')
    print('\n')
    print(df_lower_CFP.sort_values(["Footprint"], ascending=True))

recomandation(food_choice)

"""
https://pypi.org/project/console-menu/
# Import the necessary packages
from consolemenu import *
from consolemenu.items import *

# Create the menu
menu = ConsoleMenu("Title", "Subtitle")

# Create some items

# MenuItem is the base class for all items, it doesn't do anything when selected
menu_item = MenuItem("Menu Item")

# A FunctionItem runs a Python function when selected
function_item = FunctionItem("Call a Python function", input, ["Enter an input"])

# A CommandItem runs a console command
command_item = CommandItem("Run a console command",  "touch hello.txt")

# A SelectionMenu constructs a menu from a list of strings
selection_menu = SelectionMenu(["item1", "item2", "item3"])

# A SubmenuItem lets you add a menu (the selection_menu above, for example)
# as a submenu of another menu
submenu_item = SubmenuItem("Submenu item", selection_menu, menu)

# Once we're done creating them, we just add the items to the menu
menu.append_item(menu_item)
menu.append_item(function_item)
menu.append_item(command_item)
menu.append_item(submenu_item)

# Finally, we call show to show the menu and allow the user to interact
menu.show()
"""