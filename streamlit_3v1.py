import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_authenticator import Authenticate



lesDonneesDesComptes = {
    'usernames': {
        'utilisateur': {
            'name': 'utilisateur',
            'password': 'utilisateurMDP',
            'email': 'utilisateur@gmail.com',
            'failed_login_attemps': 0,  # Sera géré automatiquement
            'logged_in': False,          # Sera géré automatiquement
            'role': 'utilisateur'
        },
        'root': {
            'name': 'root',
            'password': 'rootMDP',
            'email': 'admin@gmail.com',
            'failed_login_attemps': 0,  # Sera géré automatiquement
            'logged_in': False,          # Sera géré automatiquement
            'role': 'administrateur'
        }
    }
}

authenticator = Authenticate(
    lesDonneesDesComptes,  # Les données des comptes
    "cookie name",         # Le nom du cookie, un str quelconque
    "cookie key",          # La clé du cookie, un str quelconque
    30,                    # Le nombre de jours avant que le cookie expire
)

authenticator.login()

def accueil():
    st.title("Bienvenue sur ma page")
    st.image("https://euradio-dev.s3.fr-par.scw.cloud/assets/images/news/dou-ca-vient-les-applaudissements-38348.jpg")    
    # Autre façon d'utiliser la sidebar avec un "with", pour grouper plusieurs éléments
    with st.sidebar:
        authenticator.logout("Déconnexion") 
        selection = option_menu(
            menu_title=None,
            options = ["Accueil", "Photos"]
        )
           
    # On affiche des boutons radio dans la sidebar pour choisir un mode de livraison
    if selection == "Accueil":
        st.write("Bienvenue sur la page d'accueil !")
    elif selection == "Photos":
        st.write("Bienvenue sur mon album photo")

        



if st.session_state["authentication_status"]:
    accueil()
  # Le bouton de déconnexion
elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')








col1, col2, col3 = st.columns(3)

# Contenu de la première colonne : 
with col1:
  st.header("A cat")
  st.image("https://static.streamlit.io/examples/cat.jpg")

# Contenu de la deuxième colonne :
with col2:
  st.header("A dog")
  st.image("https://static.streamlit.io/examples/dog.jpg")

# Contenu de la troisième colonne : 
with col3:
  st.header("An owl")
  st.image("https://static.streamlit.io/examples/owl.jpg")

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