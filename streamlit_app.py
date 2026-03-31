import streamlit as st

pg = st.navigation([
    st.Page("streamlit_pages/page_1.py", title="QCC coordinates", icon=":material/map:"), 
    st.Page("streamlit_pages/page_2.py", title="Other page", icon=":material/question_mark:"),
    st.Page("streamlit_pages/page_3.py", title="Example", icon=":material/help:")
    ])
pg.run()