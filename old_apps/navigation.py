import joblib
import streamlit as st

st.header("Навигация по многостраничному приложению")

if st.button("Главная страница"):
    st.switch_page("app.py")
if st.button("Покупка"):
    st.switch_page("pages/Покупка.py")
if st.button("Продажа"):
    st.switch_page("pages/Продажа.py")
