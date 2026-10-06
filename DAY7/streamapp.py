import streamlit as st
st.title("my first streamlit app")
name = st.text_input("Enter name")
if name : st.write(f"Hello, {name}!")
num = st.slider("pick number",0,100)

clicked = st.button("calculate")
agree = st.checkbox("I agree to the terms")
fruit = st.selectbox("Favourite fruit", ["apple","banana","Mango"])


col1 , col2 = st.columns(2)
with col1:
    st.write("Left side")
with col2:
    st.write("Right side")