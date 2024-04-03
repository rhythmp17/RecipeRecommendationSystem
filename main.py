import pandas as pd
import numpy as np
import scipy.sparse
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Loading the dataset
recipes_data = pd.read_csv('data.csv')

# Preprocessing the data
recipes_data['Ingredients'] = recipes_data['Ingredients'].str.lower()
recipes_data['Tags'] = recipes_data['Tags'].str.lower()
recipes_data['search_words'] = recipes_data['Tags'] + ' ' + recipes_data['Ingredients']
recipes_data = recipes_data.drop('recipe_name',axis=1)
recipes_data = recipes_data.drop('Tags',axis=1)
recipes_data = recipes_data.drop('ExtraTags',axis=1)

# Initializing TF-IDF vectorizer
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(recipes_data['search_words'])


# Function to recommend recipes based on ingredients
def recommend_recipe(ingredients, tfidf_matrix=tfidf_matrix, recipes_data=recipes_data):

  # Converting input ingredients to lowercase
    ingredients = [ingredient.lower() for ingredient in ingredients]

  # Creating search words for input ingredients
    input_search_words = ' '.join(ingredients)
    input_tfidf = tfidf.transform([input_search_words])

  # Checking Similarities of Ingridients
    similarity_scores = cosine_similarity(input_tfidf, tfidf_matrix)
    similarity_scores = list(enumerate(similarity_scores[0]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    similar_recipes_indices = [i[0] for i in similarity_scores[:5]]
    similar_recipes = recipes_data.iloc[similar_recipes_indices]

    return similar_recipes

def add_recipe(name="" , des="",by="",reqtime=np.nan,servings=np.nan,ingredients="",direc="",image="not available",nutri="",tags=""):

    recipe_id = recipes_data['id'].max() + 1

    # Creating a new DataFrame with the new recipe
    new_recipe = pd.DataFrame({'RecipeID': [recipe_id],'recipies': [name.lower()],'Description': [des.lower()],'RequiredTime' : [reqtime],
                               'Servings': [servings],'Nutritions': [nutri.lower()],'Direction': [direc],'search_words': [tags.lower()+' '+name.lower()],
                               'ingredients': [','.join(ingredients).lower()],'ImageLink':[image]})

    recipes_data = pd.concat([recipes_data, new_recipe], ignore_index=True)

    # Transform the search words of the new recipe to TF-IDF vector
    new_tfidf_vector = tfidf.transform([new_recipe['search_words'][0]])
    tfidf_matrix = scipy.sparse.vstack([tfidf_matrix, new_tfidf_vector])

# Example usage
input_ingredients = ['besan', 'ghee']
recommended_recipes = recommend_recipe(input_ingredients)
# print(pd.DataFrame(recommended_recipes['recipies'].values))
# print(recommended_recipes.iloc[2]['Ingredients'])