import streamlit as st
import pandas as pd

st.title("Demo Dashboard")
st.write("Demo dashboard created during Queen's Marquee Python class")

categories = ['A', 'B', 'C']
st.multiselect('Pick an option', categories)

st.sidebar.button('Click me!')