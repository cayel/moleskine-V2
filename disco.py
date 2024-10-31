import streamlit as st  
from database import load_artists,load_releases_from_artists_and_years
from album_grid import generate_css,generate_table_html_array

st.title("Discographies")

# Load all artists
artists = load_artists()

# Select artists
selected_artists = st.multiselect("Artistes", options=artists, format_func=lambda artist: artist.name)

# Select years
years = st.slider("Années", min_value=1950, max_value=2021, value=(1950, 2024))

# Select sort order by date asc or desc
sort_order = st.radio("Tri par date", ("Ascendant", "Descendant"))

# Launch query if button is clicked
if st.button("Rechercher"):
    if selected_artists:
        # Load all releases for the selected artists
        releases = load_releases_from_artists_and_years(selected_artists, years, sort_order)

        # Generate the HTML table
        num_columns = 5
        color = "#000000"
        table_html = generate_table_html_array(releases, num_columns)
        css = generate_css(color)
        st.markdown(css, unsafe_allow_html=True)
        st.markdown(table_html, unsafe_allow_html=True)



