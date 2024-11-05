import streamlit as st

def main():
    pages = {
        "Musique": [
            #st.Page("select.py", title="Sélections"),
            st.Page("disco.py", title="Discographies", icon="🎵"),
        ],
        "Administration": [
            st.Page("admin.py", title="Base de données", icon="🔒"),
            st.Page("admin_releases.py", title="Releases", icon="🔒"),
            st.Page("admin_artists.py", title="Artistes", icon="🔒")
        ]
    }

    pg = st.navigation(pages)
    pg.run()
    
if __name__ == "__main__":
    main()