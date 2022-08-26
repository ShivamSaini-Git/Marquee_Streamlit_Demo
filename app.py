import streamlit as st
import pandas as pd

st.title("Demo Dashboard")
st.write("Demo dashboard created during Queen's Marquee Python class")
# st.write is similar to print() in Python

categories = ['A', 'B', 'C']
st.multiselect('Pick an option', categories)

st.sidebar.button('Click me!')

url = "https://www.iposcoop.com/last-100-ipos/"
df = pd.read_html(url)[0]

# st.write(df)

st.dataframe(df)