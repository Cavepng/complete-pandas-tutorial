import streamlit as st
import pandas as pd
import numpy as np

st.write("This script outputs a list of 100 random ")

def get_data():
    df = pd.DataFrame({
        #
        "lat": np.random.randn(100) / 100 + 42.31479,
        "lon": np.random.randn(100) / 100 + -71.79364
    })
    return df

if st.button('Generate new points'):
    st.session_state.df = get_data()
if 'df' not in st.session_state:
    st.session_state.df = get_data()
df = st.session_state.df


st.map(df)