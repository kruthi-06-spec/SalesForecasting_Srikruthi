import streamlit as st
import matplotlib.pyplot as plt
from utils import *

weekly = load_anomalies()

st.title("⚠️ Anomaly Report")

fig, ax = plt.subplots(figsize=(12,5))

ax.plot(
    weekly["Order Date"],
    weekly["Sales"]
)

anomaly = weekly[weekly["Anomaly"] == -1]

ax.scatter(
    anomaly["Order Date"],
    anomaly["Sales"],
    color="red"
)

st.pyplot(fig)

st.subheader("Detected Anomalies")

st.dataframe(
    anomaly[
        ["Order Date","Sales"]
    ]
)