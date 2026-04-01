import streamlit as st
import pandas as pd

st.set_page_config(page_title="Banking Analysis", layout="wide")

# 1. Functional File Handling
@st.cache_data
def load_data(uploaded_file):
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
    else:
        # Fallback to your local file
        try:
            df = pd.read_csv("banking_transactions.csv")
        except FileNotFoundError:
            st.error("Please upload a CSV file to begin.")
            return None
            
    df["Date"] = pd.to_datetime(df["Date"])
    return df

st.title("Financial Transaction Analysis")

st.write("Upload a CSV file containing your banking transactions. The headers should be Date, Amount, Memo. If no file is uploaded, the app will attempt to load a local file named 'banking_transactions.csv'.")
uploaded_file = st.file_uploader("Upload banking CSV", type="csv")
bk = load_data(uploaded_file)

if bk is not None:
    # 2. Date Range Selection (Real-time)
    col_a, col_b = st.sidebar.columns(2)
    start_date = col_a.date_input("Start", bk["Date"].min())
    end_date = col_b.date_input("End", bk["Date"].max())

    filtered_bk = bk[(bk["Date"] >= pd.to_datetime(start_date)) & 
                     (bk["Date"] <= pd.to_datetime(end_date))].copy()

    # 3. High-Level Metrics
    total_spend = filtered_bk["Amount"].sum()
    avg_txn = filtered_bk["Amount"].mean()
    
    m1, m2, m3 = st.columns(3)
    m1.metric("Total Volume", f"${total_spend:,.2f}")
    m2.metric("Avg Transaction", f"${avg_txn:,.2f}")
    m3.metric("Transaction Count", len(filtered_bk))

    # 4. Expanded Visualizations
    tab1, tab2, tab3, tab4 = st.tabs(["Scatter Plot", "Spending Trend", "Income Trend", "Data Editor"])

    with tab1:
        st.subheader("Transaction Distribution")
        st.scatter_chart(filtered_bk.set_index("Date")["Amount"])

    with tab2:
        st.subheader("Spending Totals")
        # Functionality: Grouping data by day to see trends
        daily_trend = filtered_bk[filtered_bk["Amount"] < 0].groupby("Date")["Amount"].sum()
        st.bar_chart(daily_trend)

    with tab3:
        st.subheader("Income Totals")
        # Functionality: Grouping data by day to see trends
        daily_trend = filtered_bk[filtered_bk["Amount"] > 0].groupby("Date")["Amount"].sum()
        st.bar_chart(daily_trend)

    with tab4:
        st.subheader("Edit/Inspect Transactions")
        # Allows you to edit values and see the results
        edited_df = st.data_editor(filtered_bk, use_container_width=True)

else:
    st.info("Awaiting CSV input or local file connection.")