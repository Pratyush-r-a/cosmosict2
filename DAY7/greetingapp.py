import streamlit as st
st. title("Greeting App")
style = st.radlo("Style", ["Format", "Casuat", "'Excited"])
name = st.text_input ("What's your name?")
if name:
  st.write(f"Hello, (name)! Welcome to Streamlit.") if style • "Formal": msg • f"Greetings, (name)."
elif style == "Casual": msg = f"Hey (name)! What's up?"
else: esg • f"WELCOME (name) !!!
st.write(f" (msg) |")