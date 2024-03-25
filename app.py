import joblib
import streamlit as st

st.header("Navigation")

if st.button("House price prediction"):
    st.switch_page("pages/house_price_prediction.py")
if st.button("Mortgage calculator"):
    st.switch_page("pages/mortgage_calculator.py")
