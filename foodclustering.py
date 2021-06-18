"""
Importing Libraries
"""

#for data frame processing
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

#for clustering
from sklearn.cluster import KMeans
from k_means_constrained import KMeansConstrained
import matplotlib.pyplot as plt

#reading data from csv file using pandas
df=pd.read_csv('data\\merged_dataset_large.csv')

def print_divider():
    """
    print_divider prints a dividing line (===).
    """
    print("==============================================================================================================")
    
#End of print_divider---------------------------------------------------------------------------------------------------------------------------

def load_and_process_data (df):
    """
       load_and_process_data reads a csv from the working directory,
       examens the data, and converts all numerical values
       :param df: the data frame (merged_dataset_large.csv)
       :return: updated df
    """
    
    #getting general idea about data frame (df)
    df.describe()
    df.head()
    print_divider()
    #to know data types in df
    df.info()
    print_divider()
    #convert all data types to float
    cols = ['Energy_kcal', 'VitA_mcg', 'Folate_mcg', 'Calcium_mg','Magnesium_mg', 'Phosphorus_mg']
    for col in cols:
       df[col] = df[col].apply(lambda x: float (x) if x == x else "")

    #checking data type conversion
    df.info()
    print_divider()

    return df

#End of load_and_process_data---------------------------------------------------------------------------------------------------------------------------

def data_normalization (df):

    """
    data_normalization preprocesses the df before normalization, and
    uses MinMaxScaler (Xnorm = X - Xmin / Xmax - Xmin) to keep values between [0,1].
    :param df: the data frame (merged_dataset_large.csv)
    :return: normalized df
    """

    #selecting numerical values in df only
    df_num = df.select_dtypes(include=[np.number])

    #to keep Footprint value out of normalization
    df_num_1 = df_num.drop(['Footprint'], axis = 1)

    #verifying changes
    df_num_1.head()

    # create a scaler object
    scaler = MinMaxScaler()

    # fit and transform the data
    df_num_1 = pd.DataFrame(scaler.fit_transform(df_num_1), columns=df_num_1.columns)

    #assign normalized values back to the original df
    df[df_num_1.columns] = df_num_1

    #verifying changes
    df.head()

    return df

#End of data_normalization---------------------------------------------------------------------------------------------------------------------------

def clustering (df):

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
        # X1 has the clustering features (Energy_kcal, Protein_g, Fat_g, Carb_g, Sugar_g, Fiber_g, Calcium_mg, Iron_mg, 'VitC_mg')

        X1 = df.drop(['FullName','Item', 'Footprint', 'VitA_mcg', 'VitB6_mg', 'VitB12_mcg','VitE_mg', 'Folate_mcg', 'Niacin_mg', 'Magnesium_mg', 'Riboflavin_mg', 'Thiamin_mg', 'Copper_mcg', 'Manganese_mg','Phosphorus_mg'], axis = 1)

        #using the Elbow method to find the optimal K value (number of clsters).
        wcss = []
        for i in range(1,30):
            kmeans = KMeans(n_clusters=i,init='k-means++',max_iter=10,n_init=10,random_state=42)
            kmeans.fit(X1)
            wcss.append(kmeans.inertia_)

        #plot the WCSS with K value
        #the plot looks like an Elbow.
        #As the number of clusters increases, the WCSS value will start to decrease

        plt.plot(range(1,30),wcss, linewidth = 2, markersize = 12, marker='o')
        plt.title('The Elbow Curve')
        plt.xlabel('Number of Clusters')
        plt.ylabel('Sum of Squares Within Cluster ')
        plt.savefig('elbow.png')
        plt.show()


        """K-means Clustering - 2. KMeansConstrained with min max cluster size"""

        #to run KMeansConstrained clustering 3 times
        for i in range(1,3):
            kmeans = KMeansConstrained(n_clusters=122, size_min=8, size_max=18, init='k-means++', n_init=10, max_iter=50, verbose=False, tol=1e-4, random_state=42)
            kmeans.fit_predict(X1)

        #compiling data frame with new values

        X1['Cluster_ID'] = pd.DataFrame(kmeans.labels_)
        #assign values back to the original df
        df[X1.columns] = X1
        #saving df to csv
        df.to_csv('cluster_food.csv')
        #to show number of items in each cluster
        df['Cluster_ID'].value_counts()

        #Printing centroids
        #centroids = kmeans.cluster_centers_
        #print(centroids)

#End of clustering----------------------------------------------------------------------------------------------------------------------------

#function calls
load_and_process_data (df)
data_normalization (df)
clustering (df)









