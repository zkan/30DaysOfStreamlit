import numpy as np
import pandas as pd
import streamlit as st


st.header("Line chart")

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"],
)

st.line_chart(chart_data)
