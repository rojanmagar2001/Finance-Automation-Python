import pandas as pd
import streamlit as st

# import plotly.express as px
# import json
# import os

def load_transactions(file):
    try:
        df = pd.read_csv(file)

        df.columns = [col.strip() for col in df.columns]
        df["Amount"] = df["Amount"].str.replace(",", "").astype(float)
        df["Date"] = pd.to_datetime(df["Date"], format="%d %b %Y")

        return df
    except Exception as e:
        st.error(f"Error processing file: {str(e)}")
        return None

def main():
    st.set_page_config(page_title="S Finance App", page_icon="💰💰💰", layout="wide")

    st.title("S Finance Dashboard")

    uploaded_file = st.file_uploader("Upload your transaction CSV file", type = ["csv"])

    if uploaded_file is not None:
        df = load_transactions(uploaded_file)

        if df is not None:
            debits_df = df[df["Debit/Credit"] == "Debit"].copy()
            credits_df = df[df["Debit/Credit"] == "Credit"].copy()

            tab1, tab2 = st.tabs(["Expenses (Debits)", "Payments (Credits)"])
            with tab1:
                st.write(debits_df)
            with tab2:
                st.write(credits_df)



if __name__ == "__main__":
    main()
