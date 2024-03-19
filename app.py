import streamlit as st
import joblib
import pandas as pd

# Загрузка модели
model = joblib.load("model_lr.joblib")

# Заголовок
st.title("House Price Prediction")

# Ввод параметров
total_area = st.number_input("Total Area", min_value=0.0, max_value=1000.0, step=0.1)
floor = st.number_input("Floor", min_value=0, max_value=100, step=1)
floors_number = st.number_input("Floors Number", min_value=0, max_value=100, step=1)
longitude = st.number_input("Longitude", min_value=-180.0, max_value=180.0, step=0.1)
latitude = st.number_input("Latitude", min_value=-90.0, max_value=90.0, step=0.1)
is_auction = st.selectbox("Is Auction", ["Yes", "No"])
is_auction = 1 if is_auction == "Yes" else 0

# Прогнозирование цены
input_data = pd.DataFrame(
    {
        "total_area": [total_area],
        "floor": [floor],
        "floors_number": [floors_number],
        "longitude": [longitude],
        "latitude": [latitude],
        "is_auction": [is_auction],
    }
)
prediction = model.predict(input_data)

# Вывод результата
st.subheader("Predicted Price:")
st.write(prediction[0])
