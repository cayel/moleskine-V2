import streamlit as st
import requests
from mock_data import mock_fetch_artists, mock_fetch_releases

API_URL = "https://moleskine-api.vercel.app/"

    
class Artist:
    def __init__(self, artist_name, artist_id):
        self.name = artist_name
        self.id = artist_id
        
class Release:
    def __init__(self, release_artist, release_title, release_date):
        self.title = release_title
        self.date = release_date
        self.artist = release_artist
        
def fetch_mock_artists():
    return [Artist(artist['name'], artist['id']) for artist in mock_fetch_artists()]
    
def fetch_mock_releases():
    return [Release(release['artist'], release['title'], release['date']) for release in mock_fetch_releases()]
        
def fetch_artists(api_url):
    response = requests.get(f"{api_url}artist")
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Erreur lors de la récupération des artistes")
        return []
    
def fetch_releases(api_url):
    response = requests.get(f"{api_url}release")
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Erreur lors de la récupération des artistes")
        return []

def main():
    st.title("Moleskine-V2")
    st.write("Bienvenue dans Moleskine !")

    artists = fetch_mock_artists()
    artist_names = [artist.name for artist in artists]

    if artist_names:
        selected_artist = st.selectbox("Sélectionnez un artiste", artist_names)
        st.write(f"Vous avez sélectionné : {selected_artist}")
        
    releases = fetch_mock_releases()

    if releases:
        release_data = [(release.title, release.date) for release in releases]
        
        # Créer un tableau HTML
        html_table = """
        <table>
            <tr>
                <th>Nom du disque</th>
                <th>Date de sortie</th>
            </tr>
        """
        for title, date in release_data:
            html_table += f"<tr><td>{title}</td><td>{date}</td></tr>"
        
        html_table += "</table>"
        
        # Afficher le tableau HTML
        st.markdown(html_table, unsafe_allow_html=True)
        

if __name__ == "__main__":
    main()