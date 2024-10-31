import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Custom CSS to change background color and reduce margins
st.markdown(
    """
    <style>
    .custom-bg {
        background-color: #64597d;  /* Change to your desired color */
        color: #f5f540;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 5px;  /* Reduce space below the custom background */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Custom styled text
st.markdown('<div class="custom-bg">Texto Qualquer</div>', unsafe_allow_html=True)

# Text input area
txt = st.text_input(label="")

# Custom CSS to change background color and reduce margins
st.markdown(
    """
    <style>
    .custom-bg2 {
        background-color: #ffffff;  /* Change to your desired color */
        color: #f5f540;
        font-weight: bold;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 5px;  /* Reduce space below the custom background */
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown('<div class="custom-bg2">Outro Texto Qualquer</div>', unsafe_allow_html=True)


st.text_area("Informações sobre o paciente")
st.text_input("Nome do paciente")
st.number_input("Idade do paciente")

x = np.linspace(-np.pi,np.pi,100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x,y)

st.pyplot(fig)
