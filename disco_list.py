import streamlit as st
import sqlite3
from database import create_list, load_lists, load_all_releases, add_list_release, delete_lists_release, update_list, load_releases_list
from release_list import ReleaseList
from album_grid import generate_table_html_array, generate_css

st.session_state.selected_list = None
st.session_state.albums = [None] * 3 

st.title("Listes")
st.write("Cette page permet de gérer les listes.")

# Créer un formulaire pour ajouter une liste en demandant:
# - le nom de la liste
# - la description de la liste
# - Le choix du critère : Date de sortie, Pays, Artiste

with st.expander("Ajouter une liste", expanded=False, icon="📜"):
    with st.form(key='list_form'):
        list_name = st.text_input("Nom de la liste")
        list_description = st.text_area("Description de la liste")
        list_criteria = st.selectbox("Critère de la liste", ["Date de sortie", "Pays", "Artiste"])
        list_private = st.checkbox("Liste privée")
        submit_button = st.form_submit_button(label='Enregistrer la liste')
        if submit_button:
            create_list(list_name, list_description, list_private, list_criteria)
            st.success("La liste a été ajoutée avec succès")

with st.expander("Compléter une liste", expanded=False, icon="📝"):
        all_releases = load_all_releases()
        # Ajouter 10 albums à une liste
        list_to_update = st.selectbox("Sélectionnez une liste à compléter", options=load_lists(), index=0, format_func=lambda list: list.name)
        if 'selected_list' not in st.session_state:
            st.session_state.selected_list = None
        
        if list_to_update != st.session_state.selected_list:
            load_releases_list(list_to_update)
            st.session_state.selected_list = list_to_update
            st.session_state.albums = [None] * 3  # Réinitialiser les albums sélectionnés
        with st.form(key='update_list_form'):    
            if list_to_update:
                albums = []
                for i in range(3):
                    if len(list_to_update.releases) > i and list_to_update.releases[i] is not None:
                        selected_album_id = all_releases[list_to_update.releases[i].id-1].id-1
                    else:
                        selected_album_id = 0
                    album = st.selectbox(f"Album {i+1}", options=all_releases, index=selected_album_id, key=f"album_{i+1}",)
                    albums.append(album)
                    st.session_state.albums[i] = album
                update_button = st.form_submit_button(label='Mettre à jour la liste')
                if update_button:
                    list_to_update.clear_releases()
                    for album in albums:
                        ret = list_to_update.add_release(album)
                        if not ret:
                            break
                    if ret:
                        update_list(list_to_update)
                        st.success("La liste a été mise à jour avec succès")
                    else:
                        st.error("Erreur lors de la mise à jour de la liste")
                        
with st.expander("Afficher les albums de la liste", expanded=False, icon="📖"):
    list_to_display = st.selectbox("Sélectionnez une liste à afficher", options=load_lists(), format_func=lambda list: list.name)
    if list_to_display:
        load_releases_list(list_to_display)
            # Generate the HTML table
        num_columns = 5
        color = "#000000"
        table_html = generate_table_html_array(list_to_display.releases, num_columns)
        css = generate_css(color)
        st.markdown(css, unsafe_allow_html=True)
        st.markdown(table_html, unsafe_allow_html=True)

        
