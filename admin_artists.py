import streamlit as st
from database import add_artist

# Formulaire pour ajouter un album
with st.form(key='artist_form'):
    st.write("Ajouter un artiste")
    artist_name = st.text_input("Nom de l'artiste")
    submit_button = st.form_submit_button(label='Enregistrer les modifications')
    if submit_button:
        if add_artist(artist_name):
            st.write("L'artiste a été ajouté avec succès.")
        else:
            st.write("Une erreur est survenue lors de l'ajout de l'artiste.")