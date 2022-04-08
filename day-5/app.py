import numpy as np
import altair as alt
import pandas as pd
import streamlit as st


st.header("st.write")

# Example 1: Markdown
st.write("Hello, *World!* :sunglasses:")

# Example 2: Number
st.write(1234)

# Example 3: DataFrame
df = pd.DataFrame({
    "first column": [1, 2, 3, 4],
    "second column": [10, 20, 30, 40],
})
st.write(df)

# Example 4: Multiple arguments
st.write("Below is a DataFrame:", df, "Above is a dataframe.")

# Example 5: Plots
df2 = pd.DataFrame(
    np.random.randn(200, 3),
    columns=["a", "b", "c"],
)
c = alt.Chart(df2).mark_circle().encode(
    x="a",
    y="b",
    size="c",
    color="c",
    tooltip=["a", "b", "c"],
)
st.write(c)

# Example 6: LaTeX
st.latex(r"""
    \sum_{i=1}^N \frac{x_i}{N}
""")
