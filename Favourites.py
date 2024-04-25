import streamlit as st
import sys
import subprocess
import pandas as pd
import login2 as main

username=""
if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    username = None

st.title(f"{username}'s Favourites")

cursor = main.recipes_collection.find()
data_list = list(cursor)
recipes_data = pd.DataFrame(data_list)

user = main.users_collection.find_one({"username": username})

for i in user['favorites']:
    st.success(recipes_data['name'][i])
    st.image(recipes_data['image_url'][i],width=500,caption=recipes_data['name'][i])
    st.write("Description : ",recipes_data['description'][i])
    st.write("Ingredients : ",recipes_data['ingredients_quantity'][i])
    st.write("Directions : ",recipes_data['instructions'][i])
    st.write("Rating : ",recipes_data['rating'][i])
