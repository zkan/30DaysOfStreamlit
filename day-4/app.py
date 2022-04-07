from datetime import datetime

import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st


@st.cache
def load_data():
    data_url = "https://raw.githubusercontent.com/zkan/me-and-coffee/main/me-and-coffee.csv"
    df = pd.read_csv(data_url)
    df["DateTime"] = pd.to_datetime(df["DateTime"])

    return df


df = load_data()
print(df.info())
print(df.head())

add_sidebar = st.sidebar.selectbox("Me and Coffee", ("Me and Coffee", "Nothing",))
if add_sidebar == "Me and Coffee":
    st.write("Me and Coffee")
    avg_price = df["Price"].mean()
    print(avg_price)
    st.metric("Avg Price", avg_price)
