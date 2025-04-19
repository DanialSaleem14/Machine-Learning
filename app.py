import streamlit as st
import pandas as pd
import numpy as np


st.title("My first app")

st.write("This is a simple app")

##create a simple dataframe

df = pd.DataFrame({
    'a': [1, 2, 3, 4],
    'b': [5, 6, 7, 8],
    'c': [9, 10, 11, 12]
})

st.write("This is a simple dataframe")
st.write(df)

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)

