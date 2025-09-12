import streamlit as st

st.title("Edad de tu perrito 🐶")

edad = st.radio(
    "Selecciona la edad de tu perro (años)",
    options=list(range(0, 26))
)

if edad <= 2:
    etapa = "🐾 Cachorro"
elif edad <= 10:
    etapa = "🐕 Adulto"
else:
    etapa = "🦮 Senior"

st.write(f"Tu perrito tiene {edad} años y es un: {etapa}")
