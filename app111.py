import streamlit as st

st.title("Edad de tu gato")

edad = st.slider("Selecciona la edad de tu gato (años)", 0, 25, step=1)

if edad <= 2:
    etapa = "🐾 Bebé gato"
elif edad <= 10:
    etapa = "🐱 Gato adulto"
else:
    etapa = "🧓 Gato viejo"

st.write(f"La edad seleccionada es {edad} años, y tu gato es un: {etapa}")
