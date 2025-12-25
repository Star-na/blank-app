import streamlit as st
import pandas as pd

st.set_page_config(page_title="Student Risk UI", layout="wide")

st.title("Student Performance Prediction - Interface Prototype")
st.write("✅ App is running!")

st.sidebar.header("Upload Dataset")
file = st.sidebar.file_uploader("Upload CSV", type=["csv"])

if file is None:
    st.info("Please upload a CSV file from the sidebar.")
else:
    df = pd.read_csv(file)
    st.subheader("Dataset Preview")
    st.write(f"Rows: {len(df)} | Columns: {len(df.columns)}")
    st.dataframe(df.head(20), use_container_width=True)
