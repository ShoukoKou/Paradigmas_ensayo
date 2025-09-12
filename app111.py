import streamlit as st
import numpy as np

st.title("Gatitos - Edades")

edades = st.text_input("Ingresa edades de gatos separadas por comas:", "2,4,7")

if edades:
    lista = [int(x) for x in edades.split(",") if x.strip().isdigit()]
    if lista:
        st.write("Edad mínima:", min(lista))
        st.write("Edad máxima:", max(lista))
        st.write("Edad promedio:", round(np.mean(lista),2))
