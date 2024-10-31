import streamlit as st  
from database import create_database, drop_database
from seed_database import seed_database

st.title("Administration")
st.write("Bienvenue dans l'administration de Moleskine !")

if st.button("Réinitialiser la base de données"):
    drop_database()
    create_database()
    seed_database()
