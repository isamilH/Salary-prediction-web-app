import streamlit as st
from MODEL_PAGE import show_predict_page


page = st.sidebar.selectbox("Predict", ("Predict"))

if page == "Predict":
    show_predict_page()
