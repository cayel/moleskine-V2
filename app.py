import streamlit as st

def main():
    pages = {
        "Musique": [
            st.Page("disco.py", title="Discothèque"),
        ],
        "Administration": [
            st.Page("admin.py", title="Base de données"),
        ]
    }

    pg = st.navigation(pages)
    pg.run()
    
    # init database
    # drop_database()
    # create_database()
    # seed_database()
    
if __name__ == "__main__":
    main()