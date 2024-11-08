import streamlit as st
from database import charger_releases
import pandas as pd
import matplotlib.pyplot as plt


# Display histogram of the number of albums per artist
st.title("Statistiques")

df = charger_releases()

# Add a widget to show the total number of albums
st.write("Nombre total d'albums:", len(df))
# Add a widget to show the total number of artists
st.write("Nombre total d'artistes:", len(df['name'].unique()))

st.subheader("Nombre d'albums par artiste")
# Group the data by artist
d = df['name'].value_counts()
chart_data = pd.DataFrame(d)
st.bar_chart(chart_data, horizontal=True)

st.subheader("Nombre d'albums par année")
# Convert the date column to a datetime object
df['date'] = pd.to_datetime(df['date'])
# Group the data by year
d = df['date'].dt.year.value_counts()
chart_data = pd.DataFrame(d)
st.bar_chart(chart_data, horizontal=False)

