import streamlit as st
import pandas as pd

st.title("Bienvenue sur le site web d'Olivier")

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/taxis.csv"
df = pd.read_csv(url)

arrondissements = pd.concat([df['pickup_borough'],df['dropoff_borough']]).dropna().unique()

choix = st.selectbox("Indiquez votre arrondissement de récupération", sorted(arrondissements))

st.write("Tu as choisis :", choix)

image_dict = {
    "Manhattan": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/View_of_Empire_State_Building_from_Rockefeller_Center_New_York_City_dllu.jpg/330px-View_of_Empire_State_Building_from_Rockefeller_Center_New_York_City_dllu.jpg",
    "Bronx": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Yankee_Stadium_001.JPG/330px-Yankee_Stadium_001.JPG",
    "Brooklyn": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Brooklyn_Bridge%2C_New_York%2C_United_States_%28Unsplash_DiBu1qTQQ8s%29.jpg/330px-Brooklyn_Bridge%2C_New_York%2C_United_States_%28Unsplash_DiBu1qTQQ8s%29.jpg",
    "Queens": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Unisphere-2_%2827835155267%29.jpg/330px-Unisphere-2_%2827835155267%29.jpg",
    "Staten Island": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Verrazano_-_Narrows_Bridge4.jpg/330px-Verrazano_-_Narrows_Bridge4.jpg"
}

st.image(image_dict[choix])
