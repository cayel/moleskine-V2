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

    if releases:
        release_data = [(release['release_title'], release['release_date']) for release in releases]
        
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