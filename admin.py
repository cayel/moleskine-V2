import streamlit as st  
from database import create_database, drop_database, get_id_artist, add_release
from seed_database import seed_database
import requests

API_KEY = 'cac21970e3572d81c5a8aef87526959b'  

def search_album(title, artist):
    url = f"http://ws.audioscrobbler.com/2.0/?method=album.search&album={title}&artist={artist}&api_key={API_KEY}&format=json"
    response = requests.get(url)
    return response.json()

def get_album_info(mbid):
    url = f"http://ws.audioscrobbler.com/2.0/?method=album.getinfo&mbid={mbid}&api_key={API_KEY}&format=json"
    response = requests.get(url)
    return response.json()

def get_album_info_musicbrainz(mbid):
    url = f"https://musicbrainz.org/ws/2/release/{mbid}?inc=artist-credits+labels+discids+recordings&fmt=json"
    response = requests.get(url)
    return response.json()

# Initialiser l'état de la session pour les albums
if 'albums' not in st.session_state:
    st.session_state['albums'] = []
if 'selected_album' not in st.session_state:
    st.session_state['selected_album'] = None

st.title("Administration")
st.write("Bienvenue dans l'administration de Moleskine !")

# Bouton pour réinitialiser la base de données
if st.button("Réinitialiser la base de données"):
    drop_database()
    create_database()
    seed_database()

# Formulaire pour ajouter un album
st.write("Ajouter un album")
release_title = st.text_input("Titre de l'album")
release_artist = st.text_input("Artiste de l'album")

# Bouton pour rechercher l'album sur Last.fm
if st.button("Rechercher l'album"):
    if release_artist and release_title:
        # Réinitialiser le contexte de recherche
        st.session_state['albums'] = []
        st.session_state['selected_album'] = None
        limit_search = 20
        result = search_album(release_title, release_artist)
        st.session_state['albums'] = [
            album for album in result['results']['albummatches']['album']
            if album['mbid'] and album['image'][2]['#text']][:limit_search]

        if not st.session_state['albums']:
            st.write("Aucun album trouvé.")
    else:
        st.write("Veuillez entrer le titre et l'artiste de l'album.")

# Afficher les albums trouvés
if st.session_state['albums']:
    albums = st.session_state['albums']
    cols = st.columns(5)
    
    for i, album in enumerate(albums):
        album_image = album['image'][2]['#text']
        album_title = album['name']
        album_mbid = album['mbid']
        if album_image and album_mbid:
            with cols[i % 5]:
                st.image(album_image, width=100)
                if st.button("Choisir", key=f"choose_{i}"):
                    st.session_state['selected_album'] = i

# Afficher les détails de l'album sélectionné
if st.session_state['selected_album'] is not None:
    selected_album = st.session_state['selected_album']
    if selected_album < len(st.session_state['albums']):
        album = st.session_state['albums'][selected_album]
        album_image = album['image'][2]['#text'] 
        album_title = album['name']
        album_artist = album['artist']
        album_mbid = album['mbid']

        album_info = get_album_info_musicbrainz(album_mbid)
        album_date = album_info.get('date', 'Date non disponible')
        st.write(f"### Vous avez sélectionné l'album n°{selected_album + 1}")
        st.image(album_image, caption=album_title, width=200)
        
        with st.form(key='album_form'):
            new_album_title = st.text_input("Titre de l'album", value=album_title)
            id_artist = get_id_artist(album_artist)
            new_album_artist = st.text_input("Artiste", value=album_artist)
            if id_artist == -1:
                st.warning("L'artiste n'existe pas dans la base de données.")
            new_album_mbid = st.text_input("MBID", value=album_mbid)
            new_album_date = st.text_input("Date de sortie", value=album_date)
            new_album_image = st.text_input("Image", value=album_image)
            submit_button = st.form_submit_button(label='Enregistrer les modifications', disabled=(id_artist == -1))

        if submit_button:
            if add_release(new_album_title, new_album_date, id_artist, new_album_image, new_album_mbid):
                st.write("L'album a été ajouté avec succès.")
            else:
                st.write("Une erreur est survenue lors de l'ajout de l'album.")
    else:
        st.write("L'album sélectionné n'existe pas.")