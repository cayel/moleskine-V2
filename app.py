import streamlit as st

def main():
    pages = {
        "Musique": [
            #st.Page("select.py", title="Sélections"),
            st.Page("disco.py", title="Discographies"),
        ],
        "Administration": [
            st.Page("admin.py", title="Base de données"),
        ]
    }

    pg = st.navigation(pages)
    pg.run()
    
if __name__ == "__main__":
    main()