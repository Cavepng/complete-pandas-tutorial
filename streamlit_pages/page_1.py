import streamlit as st
import pandas as pd

st.title("Coordinate Mapper")

# Define the path to your default file
DEFAULT_FILE = "address_coordinates.csv"

# 1. File Uploader UI
st.write("Upload a CSV file with 'lat' and 'lon' columns to visualize on the map. If no file is uploaded, the default dataset will be used.")
uploaded_file = st.file_uploader("Optional: upload a custom CSV.", type="csv")

@st.cache_data
def load_data(file):
    # This handles both a file path (string) or an uploaded file object
    df = pd.read_csv(file)
    return df

# 2. Functional Selection: Default vs. Uploaded
if uploaded_file is not None:
    data = load_data(uploaded_file)
    st.success("Using uploaded file")
else:
    data = load_data(DEFAULT_FILE)
    st.info(f"Using default data: {DEFAULT_FILE}")

# 3. Processing and Display
if data is not None:
    # Ensure columns exist before mapping
    if "lat" in data.columns and "lon" in data.columns:
        latlon = data[["lat", "lon"]].dropna()
        st.metric("Total Points Mapped", len(latlon))
        st.map(latlon)
        with st.expander("View Data Table"):
            st.write(latlon)
    else:
        st.error("CSV must contain 'lat' and 'lon' columns.")