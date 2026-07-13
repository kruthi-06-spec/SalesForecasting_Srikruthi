import streamlit as st
import matplotlib.pyplot as plt
from utils import *

forecast = load_forecast()
df = load_data()

st.title("🔮 Forecast Explorer")

mode = st.selectbox(
    "Forecast By",
    ["Category","Region"]
)

if mode == "Category":
    st.selectbox(
        "Category",
        df["Category"].unique()
    )
else:
    st.selectbox(
        "Region",
        df["Region"].unique()
    )

months = st.slider(
    "Forecast Horizon",
    1,
    3,
    3
)

fig, ax = plt.subplots()

ax.plot(
    forecast["ds"],
    forecast["yhat"]
)

st.pyplot(fig)

# Replace these with your actual values from Task 3
MAE = 18031.4
RMSE = 19009.18

st.metric("MAE", round(MAE,2))
st.metric("RMSE", round(RMSE,2))