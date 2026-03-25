import streamlit as st

pg = st.navigation([
    st.Page("page_1.py", title="QCC coordinates", icon=":material/add_circle:"), 
    st.Page("page_2.py", title="Other page", icon=":material/map:")
    ])
pg.run()