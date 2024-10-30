import streamlit as st
from database import create_database, populate_database, drop_database, load_lists, load_list_releases
from album_grid import generate_css, generate_table_html

def main():
    st.title("Moleskine-V2")
    st.write("Bienvenue dans Moleskine !")

    # init database
    drop_database()
    create_database()
    populate_database()

    # load lists
    lists = load_lists()
    
    # select a list
    list_names = [l.name for l in lists]
    list_name = st.selectbox("Sélectionnez une liste", list_names)

    # load list releases for the selected list
    list_releases = load_list_releases()
    list_releases = [l for l in list_releases if l.name == list_name][0]

    num_columns = 5
    color = "#000000"

    table_html = generate_table_html(list_releases, num_columns)
    css = generate_css(color)
    st.markdown(css, unsafe_allow_html=True)
    st.markdown(table_html, unsafe_allow_html=True)

if __name__ == "__main__":
    main()