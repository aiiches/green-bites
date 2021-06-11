# Green Bites 
Ayesha Liaqat, Meriem Khalfoun, Lama Khalil, Kate Szabo, Victoria Wang - AI4GoodLab 2021

## Introduction
*Green Bites* is a grocery tool that will provide the user with helpful data about their carbon footprint, 
and provide suggestions for ways to reduce their environmental impact by adjusting their diet.

Our primary objectives are to:
- Provide users with insight about the environmental impacts of their groceries
- Empower individuals to make smart dietary decisions that are sustainable for them and for the planet
- Increase the accessibility of environmentally-friendly food options

In the app, the user can enter a food item by taking a picture or manually typing in a name. Our app will then...
1. (If applicable) Interpret the photograph using the Google Vision API and return a label indicating what food is in 
the image
2. Use NLP to identify where the user's input fits in our dataset.
3. Give the user an estimate of the carbon footprint of the food they entered.
4. Provide a list of recommended alternatives that have a similar nutritional value, but have a lower carbon footprint.

The end goal of the product is to allow the user to enter a full grocery list that they can use while shopping. The app
would provide insights into the carbon footprint, water use, and land use of their list, and provide smart 
recommendations for items that could be swapped to have a more eco-friendly grocery haul!

## Data
This project uses three datasets.
1. A dataset containing carbon footprint data for a selection of over 300 food items from 
[Su-EatableLife](https://www.sueatablelife.eu/en/).
2. A [USDA National Nutrient Database dataset](https://fdc.nal.usda.gov/index.html) containing nutritional information 
for a selection of over 8000 food items.
3. A [Kaggle dataset](https://www.kaggle.com/shuyangli94/food-com-recipes-and-user-interactions/version/2) containing 
text from over 200000 recipes available on Food.com.

A major task in the development of this project involved combining datasets 1 and 2 to form a single comprehensive 
dataset containing carbon footprint data and nutritional data for a set of common foods. To do this, a language model
was trained on dataset 3 to learn the semantics of common food-related words. Then, similar labels could be identified
between datasets 1 and 2 to add nutritional information to the carbon footprint dataset.

## Methods
*Green Bites* uses AI to identify any input from the user, identify the item's carbon footprint, and determine 
alternatives that have similar nutritional value to the input.
### Computer vision
The user is able to input a food item by either typing it into the app, or by taking a photograph. The Google Vision API
is used to identify food images.
### Language processing
Regardless of the input method, the program must interpret the string associated with the entry, and determine
how it relates to the data included in our environmental impact dataset. This is done using the same language model 
that was used to combine the carbon footprint and nutrition datasets. This model uses the 
[gensim word2vec](https://radimrehurek.com/gensim/models/word2vec.html) library. 

The model was trained on the recipe dataset to obtain word embeddings. Since many of the food labels were composed of
multiple words, embeddings could be obtained for each label by averaging the embeddings for each contained word,
which was found to preserve the semantic information.

In the future, we are interested in investigating more powerful language models such as BERT that have a larger corpus.
This would allow us to both improve the identification of user inputs and create a larger dataset, which would result
in more specific recommendations.
### Clustering
In order to provide helpful recommendations to the user, the food items were clustered based on their nutritional
information. This way, recommended alternatives will provide the user with similar nutritional value. All items were 
clustered using the [k-means++](https://www.geeksforgeeks.org/ml-k-means-algorithm/) algorithm, which uses a smarter
initialization of centroids than standard k-means clustering.

## Our vision
The current iteration of *Green Bites* is simply a prototype, intended to demonstrate the utility and potential of 
our idea. Some areas for future research and development are included below:
- Obtain a larger dataset. The dataset that we have created and are currently using is very limited, containing under
300 food items. If we could expand this dataset to include more food items, as well as more features (ex. is the food
a beverage?), we could provide more accurate emission predictions, as well as more helpful recommendations.
- Consider item quantities. Ideally, the app will recommend alternatives that have similar serving sizes, so 
that the alternatives can be easily incorporated into a recipe. Because we currently do not consider quantity, our app
will return very inaccurate carbon footprint data, as the data is normalized to 1kg of each type of food.
- Incorporate item prices. Due to a plethora of factors, food that is more eco-friendly is often more expensive. Since
a primary objective of our project is to increase the accessibility of environmentally conscious options, we would like
to be able to recommend alternatives that are similarly priced to the user's initial choice.
- Streamline the identification and recommendation process into a single, more powerful transformer model. Instead of 
using a set of simple ML models that operate on the same dataset, all functionality can be incorporated into a large
transformer. We have investigated the potential of fine-tuning the BERT model for our purposes and see lots of 
potential.
- Incorporate user profiles so that the algorithm can learn from individuals to provide more helpful recommendations.
This would also allow the app to consider dietary preferences or restrictions.