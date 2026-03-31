import streamlit as st
import pandas as pd

#Open banking transactions
bk = pd.read_csv("banking_transactions.csv")

#Convert Date to datetime column
bk["Date"] = pd.to_datetime(bk["Date"])  # <- important!

st.title("Banking Data")

with st.form("date_range"):
    st.write("Input the date range")
    start_date = st.date_input("Start date", bk["Date"].min())
    end_date = st.date_input("End Date", bk["Date"].max())
    st.form_submit_button("Submit")

filtered_bk = bk[(bk["Date"] >= pd.to_datetime(start_date)) &
                 (bk["Date"] <= pd.to_datetime(end_date))]

st.scatter_chart(filtered_bk.set_index("Date")["Amount"])