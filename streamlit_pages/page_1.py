import streamlit as st
import pandas as pd

st.title("Location Map")
st.write("Visualizing coordinat data from a CSV file.")

addrcords = pd.read_csv("address_coordinates.csv")
latlon = addrcords.loc[:, ["lat", "lon"]]
latlon.dropna(inplace=True)

st.map(latlon)