import streamlit as st
import pandas as pd

st.title("Streamlit Widgets")

name = st.text_input("Enter your name")

if name:
    st.write(f"Hello {name}!")
    
age = st.slider("Select your age: ", 0, 100, 25)

st.write(f"Your age is {age}")

options = ["python", "java", "c++", "javascript"]
choice = st.selectbox("Choose your favourite programming language", options)
st.write (f"You Selected {choice}")

data = {
    "name": ["John", "Jane", "Doe"],
    "age":[25, 30, 35],
    "city": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)
df.to_csv("data.csv")
st.write(df)

upload_file = st.file_uploader("Upload a CSV file", type=["csv"])
if upload_file is not None:
    df = pd.read_csv(upload_file)
    st.write(df)