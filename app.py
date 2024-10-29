import streamlit as st
import requests

API_URL = "https://moleskine-api.vercel.app/"

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

    artists = fetch_artists(API_URL)
    artist_names = [artist['artist_name'] for artist in artists]

    if artist_names:
        selected_artist = st.selectbox("Sélectionnez un artiste", artist_names)
        st.write(f"Vous avez sélectionné : {selected_artist}")
        
    releases = fetch_releases(API_URL)
    releases_titles = [release['release_title'] for release in releases]

    if releases_titles:
        selected_release = st.selectbox("Sélectionnez un disques", releases_titles)
        st.write(f"Vous avez sélectionné : {selected_release}")
        

if __name__ == "__main__":
    main()