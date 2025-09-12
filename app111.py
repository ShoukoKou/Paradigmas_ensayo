import streamlit as st
import pandas as pd
import numpy as np

st.title("Gatitos")
num=st.slider("num", 0, 100, step = 1)
st.write("El número ingresado es {}".format(num))
