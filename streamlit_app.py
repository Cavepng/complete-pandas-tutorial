import streamlit as st

pg = st.navigation([
    st.Page("streamlit_pages/page_1.py", title="Coordinate Mapper", icon=":material/map:"), 
    st.Page("streamlit_pages/page_2.py", title="Other page", icon=":material/question_mark:")
    ])
pg.run()