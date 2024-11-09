import streamlit as st
from database import add_artist
from database import load_artists, update_artist, delete_artist, get_releases_count


# Formulaire pour ajouter un artiste

with st.expander("Ajouter un artiste", expanded=False, icon="🎨"):
    with st.form(key='artist_form'):
        artist_name = st.text_input("Nom de l'artiste")
        artist_country = st.text_input("Pays de l'artiste")
        submit_button = st.form_submit_button(label='Enregistrer les modifications')
        if submit_button:
            if add_artist(artist_name, None, artist_country):
                st.write("L'artiste a été ajouté avec succès.")
            else:
                st.write("Une erreur est survenue lors de l'ajout de l'artiste.")

# Sélection d'un artiste pour le modifier
with st.expander("Modifier un artiste", expanded=False, icon="🖌️"):
    # Réinitialiser le formulaire
    st.session_state.form_submitted = False
    artist_to_update = st.selectbox("Sélectionnez un artiste à modifier", options=load_artists(), format_func=lambda artist: artist.name)
    if artist_to_update:
        with st.form(key='update_artist_form'):
            st.write("Modifier un artiste")
            if artist_to_update.country is None:
                artist_to_update.country = ""
            new_artist_name = st.text_input("Nom de l'artiste", value=artist_to_update.name)
            new_artist_country = st.text_input("Pays de l'artiste", value=artist_to_update.country)
            submit_button = st.form_submit_button(label='Enregistrer les modifications')
            if submit_button:
                if update_artist(artist_to_update.id, new_artist_name, new_artist_country):
                    st.write("L'artiste a été modifié avec succès.")
                    # Réinitialiser le formulaire
                    st.session_state.form_submitted = True
                    # Réinitialiser artist_to_update
                    artist_to_update = None
                else:
                    st.write("Une erreur est survenue lors de la modification de l'artiste.")

with st.expander("Supprimer un artiste", expanded=False, icon="🗑️"):
    artist_to_delete = st.selectbox("Sélectionnez un artiste à supprimer", options=load_artists(), format_func=lambda artist: artist.name)
    if artist_to_delete:
        if get_releases_count(artist_to_delete.id) > 0:
            st.warning("Cet artiste a des albums associés. Vous devez d'abord supprimer les albums avant de supprimer l'artiste.")
        else:
            if st.button("Supprimer l'artiste"):
                if delete_artist(artist_to_delete.id):
                    st.write("L'artiste a été supprimé avec succès.")
                else:
                    st.write("Une erreur est survenue lors de la suppression de l'artiste.")