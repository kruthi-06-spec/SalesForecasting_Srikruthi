import streamlit as st
import matplotlib.pyplot as plt
from utils import *

features = load_clusters()

st.title("📦 Product Demand Segments")

fig, ax = plt.subplots()

ax.scatter(
    features["PC1"],
    features["PC2"],
    c=features["Cluster"]
)

st.pyplot(fig)

st.subheader("Cluster Details")

st.dataframe(
    features[
        ["Cluster","Cluster Name"]
    ]
)