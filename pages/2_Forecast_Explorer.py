import streamlit as st
import matplotlib.pyplot as plt
from utils import *

st.title("🔮 Forecast Explorer")

forecast = load_forecast()
df = load_data()

mode = st.selectbox(
    "Forecast By",
    ["Category", "Region"]
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

# Show only selected months
forecast = forecast.head(months)

fig, ax = plt.subplots(figsize=(8,4))

ax.plot(
    range(1, len(forecast)+1),
    forecast["predicted_mean"],
    marker="o",
    linewidth=2
)

ax.set_xticks([1, 2, 3][:months])
ax.set_xlabel("Forecast Month")
ax.set_ylabel("Predicted Sales")
ax.set_title("SARIMA Sales Forecast")

st.pyplot(fig)

# Replace with your actual values
MAE = 18031.40
RMSE = 19009.18

col1, col2 = st.columns(2)
col1.metric("MAE", round(MAE,2))
col2.metric("RMSE", round(RMSE,2))
