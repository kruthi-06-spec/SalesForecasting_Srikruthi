import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    df = pd.read_csv("train.csv")
    df["Order Date"] = pd.to_datetime(
        df["Order Date"],
        format="%d/%m/%Y"
    )

    df["Ship Date"] = pd.to_datetime(
        df["Ship Date"],
        format="%d/%m/%Y"
    )
    return df

@st.cache_data
def load_yearly():
    return pd.read_csv("outputs/yearly_sales.csv")

@st.cache_data
def load_monthly():
    return pd.read_csv("outputs/monthly_sales.csv")

@st.cache_data
def load_forecast():
    return pd.read_csv("outputs/sarima_forecast.csv")

@st.cache_data
def load_anomalies():
    return pd.read_csv("outputs/anomalies.csv")

@st.cache_data
def load_clusters():
    return pd.read_csv("outputs/clusters.csv")