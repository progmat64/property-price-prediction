import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="UrbanRate", page_icon="🏠", initial_sidebar_state="auto"
)

st.title("Mortgage calculator")

predicted_price = st.number_input(
    "Predicted price", min_value=100000.0, step=1.0
)
first_pay = st.number_input("Initial payment", min_value=10000.0, step=1.0)
year = st.number_input("Loan term", min_value=1.0, step=1.0)
rate = st.number_input("Loan rate", min_value=1.0, step=0.1)

month_pay = (
    (predicted_price - first_pay)
    * (rate / 12)
    * ((1 + rate / 12) ** (year * 12))
    / (((1 + rate / 12) ** (year * 12)) - 1)
)
total_money = 12 * year * month_pay
percentage = total_money - predicted_price


if month_pay >= 0 and total_money >= 0 and percentage >= 0:
    data = {
        "Month pay": ["{:.2f}".format(month_pay)],
        "Total payment": ["{:.2f}".format(total_money)],
        "Percentage": ["{:.2f}".format(percentage)],
    }
    df = pd.DataFrame(data)
    st.table(df)
