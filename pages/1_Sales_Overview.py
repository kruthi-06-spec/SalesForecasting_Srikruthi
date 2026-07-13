import streamlit as st
import matplotlib.pyplot as plt
from utils import *

st.title("📈 Sales Overview Dashboard")

df = load_data()
yearly = load_yearly()
monthly = load_monthly()

region = st.sidebar.selectbox(
    "Region",
    ["All"] + list(df["Region"].unique())
)

category = st.sidebar.selectbox(
    "Category",
    ["All"] + list(df["Category"].unique())
)

filtered = df.copy()

if region != "All":
    filtered = filtered[filtered["Region"] == region]

if category != "All":
    filtered = filtered[filtered["Category"] == category]

st.subheader("Total Sales by Year")

fig, ax = plt.subplots()

ax.bar(yearly["Year"], yearly["Sales"])

st.pyplot(fig)

st.subheader("Monthly Sales Trend")

fig, ax = plt.subplots(figsize=(10,4))

ax.plot(monthly["Order Date"], monthly["Sales"])

plt.xticks(rotation=45)

st.pyplot(fig)

st.subheader("Filtered Data")

st.dataframe(filtered)