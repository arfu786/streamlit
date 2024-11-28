import streamlit as st
import pandas as pd
st.write("## Hello World")
a=st.text_input("Name")
st.write(f'My name is {a}')
click = st.button("Touch me If you Dare")
st.write(f'{click}')

data = pd.read_csv("shopping_trends.csv")
st.write(data)