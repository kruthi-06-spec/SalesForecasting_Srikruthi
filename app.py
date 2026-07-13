import streamlit as st
st.set_page_config(
    page_title="Superstore Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Superstore Sales Dashboard")

st.write("""
Welcome!

Use the sidebar to navigate through:

- Sales Overview
- Forecast Explorer
- Anomaly Report
- Product Demand Segments
""")

st.sidebar.success("Select a page above")