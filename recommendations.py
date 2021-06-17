import pandas as pd
df =pd.read_csv('data\\cluster_food.csv')

def recomandation(food_choice):
    """
          recomandation takes the user's input and matches it with the
          clustered data in cluster_food.csv to compare the footprint values and
          sort them in ascending order
          :param user's choice
          :return: list of recommandations
    """
    try:
        food_choice = food_choice.lower()
        df_user_choice = df.loc[df['FullName'] == food_choice]
        user_choice_carbon_footprint = float(df_user_choice['Footprint'])
        df_same_cluster = df.loc[df['Cluster_ID'] == int(df_user_choice['Cluster_ID'])]
        df_lower_CFP = df_same_cluster.loc[df_same_cluster['Footprint'] < user_choice_carbon_footprint].sort_values(
            ["Footprint"], ascending=True)
        if len(df_lower_CFP) == 0:
            print('Great choice!')
        else:
            print(food_choice + ': has a carbon footprint of {} GHG'.format('%.2f' % user_choice_carbon_footprint))
            print('\n')
            print('Here is a list of items with lower carbon footprint:')
            print('\n')
            print(df_lower_CFP[['FullName', 'Footprint', 'Cluster_ID']][0:10])
    except:
        print('Sorry, we do not know this item. Try an other name')

