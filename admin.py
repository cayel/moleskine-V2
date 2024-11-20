import streamlit as st  
from database import create_database, drop_database, get_id_artist, add_release
from seed_database import seed_database
import requests
import json
from database import get_all_artists, get_all_releases, add_artist, add_release, get_database_version
from maj_database import maj_database


FILE_EXPORT = "./data/moleskine_backup.json"
FILE_EXPORT_GZ = "./data/moleskine_backup.json.gz"

import json
import gzip
import os
import streamlit as st
from database import get_all_artists, get_all_releases

class ExportDatabaseError(Exception):
    """Exception levée pour les erreurs d'exportation de la base de données."""
    pass

def export_database():
    try:
        # Récupération des artistes et des albums
        artists = get_all_artists()
        releases = get_all_releases()

        data = {
            "artists": artists,
            "albums": releases
        }

        # Écriture des données dans un fichier JSON
        with open(FILE_EXPORT, "w") as f:
            json.dump(data, f, indent=4)

        # Compression du fichier JSON
        with open(FILE_EXPORT, "rb") as f:
            data = f.read()
        with open(FILE_EXPORT_GZ, "wb") as f:
            f.write(gzip.compress(data))

        # Suppression du fichier JSON non compressé
        os.remove(FILE_EXPORT)

        return True
    except Exception as e:
        raise ExportDatabaseError(f"Une erreur est survenue lors de l'exportation de la base de données : {e}")

st.header("Administration de la base de données", divider="blue")

# Export de la base de données
with st.expander("Export de la base de données", icon="📤"):
    if st.button("Exporter la base de données"):
        try:
            if export_database():
                st.success("La base de données a été exportée et compressée avec succès.")
        except ExportDatabaseError as e:
            st.error(e)

        # Lire le fichier pour le téléchargement
        with open(FILE_EXPORT_GZ, "rb") as f:
            export_data = f.read()

        # Ajouter un bouton de téléchargement
        st.download_button(
            label="Télécharger le fichier exporté",
            data=export_data,
            file_name="moleskine_backup.json.gz",
            mime="application/gzip"
        )

# Restaurer la base de données
with st.expander("Restaurer la base de données", icon="📥"):
    uploaded_file = st.file_uploader("Choisir un fichier gzip", type=["gz","json"])
    if uploaded_file is not None:
        if st.button("Restaurer la base de données"):
            try:
                drop_database()
                create_database()
                maj_database(0)
                if uploaded_file.type == "application/json":
                    with open(FILE_EXPORT, "wb") as f:
                        f.write(uploaded_file.read())
                    with open(FILE_EXPORT, "r") as f:
                        data = json.load(f)
                else:
                    with open(FILE_EXPORT_GZ, "wb") as f:
                        f.write(uploaded_file.read())
                    with gzip.open(FILE_EXPORT_GZ, "rb") as f:
                        data = json.load(f)                        
                for artist in data["artists"]:
                    add_artist(artist[1], artist[0], artist[2], artist[3])
                for album in data["albums"]:
                    add_release(album[1], album[2], album[3], album[4], album[5], album[0])
                st.success("La base de données a été restaurée avec succès.")
            except Exception as e:
                st.error(f"Une erreur est survenue lors de la restauration de la base de données : {e}")
    else:
        st.warning("Veuillez choisir un fichier gzip.")

# Bouton pour réinitialiser la base de données
with st.expander("Réinitialiser la base de données",icon="🔄"):
    if st.button("Réinitialiser la base de données"):
        drop_database()
        create_database()
        seed_database()

with st.expander("Mettre à jour la base de données", icon="🧪"):
    # Display database version
    version_db = get_database_version()
    st.write(f"Version de la base de données : {version_db}")
    if st.button("Mettre à jour la base de données"):
        ret = maj_database(version_db)
        if ret:
            st.success("La base de données a été mise à jour avec succès.")
        else:
            st.error("Une erreur est survenue lors de la mise à jour de la base de données.")
    

