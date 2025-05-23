import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Manipulation de données et création de graphiques")



liste_df = ['anagrams', 'anscombe', 'attention', 'brain_networks', 'car_crashes','diamonds','dots','dowjones','exercise','flights','fmri','geyser','glue',
            'healthexp', 'iris', 'mpg', 'penguins', 'planets','seaice', 'taxis', 'tips', 'titanic']

choix = st.selectbox("Indiquez votre arrondissement de récupération", sorted(liste_df))

url = f"https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/{choix}.csv"
df = pd.read_csv(url)

st.dataframe(df)

colonnes = df.columns
X = st.selectbox("Choisissez la colonne X", colonnes)

Y = st.selectbox("Choisissez la colonne Y", colonnes)

type_graph = ['scatter_chart', 'bar_chart', 'line_chart']
graph = st.selectbox("Quel graphique veux-tu utiliser ?", type_graph)

if graph == 'scatter_chart':
    st.scatter_chart(df, x=X, y=Y) 

elif graph == 'bar_chart':
    st.bar_chart(df, x=X, y=Y)

elif graph == 'line_chart':
    st.line_chart(df, x=X, y=Y)

corr = st.checkbox(label = "Afficher la matrice de corrélation")
st.title("Ma matrice de corrélation")

if corr == True:
    df_nombre = df.copy()

    for col in df_nombre.select_dtypes(include=['object', 'category']):
        df_nombre[col] = df_nombre[col].astype('category').cat.codes

    df_corr = df_nombre[[X, Y]].corr()

    fig, ax = plt.subplots()
    sns.heatmap(df_corr, annot=True, cmap="coolwarm", ax=ax, vmin=-1, vmax=1)
    st.pyplot(fig)