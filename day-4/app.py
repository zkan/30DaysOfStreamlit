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
