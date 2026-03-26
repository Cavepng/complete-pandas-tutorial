import streamlit as st

pg = st.navigation([
    st.Page("page_1.py", title="QCC coordinates", icon=":material/map:"), 
    st.Page("page_2.py", title="Other page", icon=":material/question_mark:")
    ])
pg.run()