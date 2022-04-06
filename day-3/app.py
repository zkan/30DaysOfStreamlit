import streamlit as st


# Header text for the app
st.header("st.button")

if st.button("Say hello"):
     st.write("Why hello there")
else:
     st.write("Goodbye")
