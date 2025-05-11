import streamlit as st
import random 
import string

def password_generator(length,use_digits,use_special):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits

    if use_special:
        characters += string.punctuation # add specials characters

    return "".join(random.choice(characters) for _ in range(length))


st.title("Password Generator")

length = st.slider("Select password length",min_value=6, max_value=32, value=12)
use_digits = st.checkbox("Include Digits")
use_special = st.checkbox("Include Special Characters")


if st.button("Generate Password"):
    password = password_generator(length,use_digits,use_special)
    st.write(f'Generated passwod : "{password}"')

st.write("-----------------------")

st.write("Build with love by Muhammad Faraz")