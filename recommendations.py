import pandas as pd
df = pd.read_csv('data\\cluster_food.csv')


def recommendation(food_choice):
    """
          recommendation takes the user's input and matches it with the
          clustered data in cluster_food.csv to compare the footprint values and
          sort them in ascending order
          :param food_choice: must be an item in the dataset
          :return: dataframe with the 10 closest recommended swaps
    """
    try:
        food_choice = food_choice.lower()
        df_user_choice = df.loc[df['FullName'] == food_choice]
        user_choice_carbon_footprint = float(df_user_choice['Footprint'])
        df_same_cluster = df.loc[df['Cluster_ID'] == int(df_user_choice['Cluster_ID'])]
        df_lower_CFP = df_same_cluster.loc[df_same_cluster['Footprint'] < user_choice_carbon_footprint].sort_values(
            ["Footprint"], ascending=True)
        return df_lower_CFP[['FullName', 'Footprint', 'Cluster_ID']][0:10]

    except:
        print("Sorry! We couldn't find that item. Try another!")
