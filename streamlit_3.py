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

    # Autre façon d'utiliser la sidebar avec un "with", pour grouper plusieurs éléments
    with st.sidebar:
        authenticator.logout("Déconnexion")
        selection = option_menu(
            menu_title=None,
            options = ["Accueil", "Photos animaux"]
        )
           
    # On affiche des boutons radio dans la sidebar pour choisir un mode de livraison
    if selection == "Accueil":
        st.title("Bienvenue sur la page d'accueil !")
        st.image("https://euradio-dev.s3.fr-par.scw.cloud/assets/images/news/dou-ca-vient-les-applaudissements-38348.jpg")  
    elif selection == "Photos animaux":
        st.title("Bienvenue dans l'album de mes animaux")
        col1, col2, col3 = st.columns(3) 
        with col1:
            st.header("A cat")
            st.image("https://static.streamlit.io/examples/cat.jpg")
        with col2:
            st.header("A dog")
            st.image("https://static.streamlit.io/examples/dog.jpg")
        with col3:
            st.header("A cow")
            st.image("https://media.4-paws.org/1/2/6/0/1260b8bbeb9d82d5a6caaa078d5061bbf626f94e/VIER%20PFOTEN_2015-04-27_010-1927x1333-1920x1328.jpg")

        



if st.session_state["authentication_status"]:
    accueil()
elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')






