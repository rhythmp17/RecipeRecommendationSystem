import streamlit as st
import sys
import subprocess

username=""
if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    username = None

st.title(f"Add Your Recipe")
name = st.text_input("Recipe Name : ")
name = st.text_input("Cuisine : ")
name = st.text_input("Course : ")
name = st.text_input("Diet : ")
name = st.text_input("Instructions : ")
name = st.text_input("Cook Time : ")
name = st.text_input("Image_url : ")
button=st.button("Add")
