import streamlit as st
import joblib

# Загрузка обученной модели
model = joblib.load("model_rf.joblib")

# Заголовок приложения
st.title("House Price Prediction App")

# Ввод данных пользователем
total_area = st.number_input("Total Area", min_value=0.0, step=0.01)
rooms_count = st.number_input("Number of Rooms", min_value=0.0, step=1.0)
floor = st.number_input("Floor", min_value=0.0, step=1.0)
floors_number = st.number_input("Total Number of Floors", min_value=0.0, step=1.0)
isСomplete = st.selectbox("Is the House Complete?", [0, 1])
longitude = st.number_input("Longitude")
latitude = st.number_input("Latitude")
is_auction = st.selectbox("Is it an Auction?", [0, 1])
region_ekb = st.selectbox("Region Ekaterinburg", [0, 1])
region_kzn = st.selectbox("Region Kazan", [0, 1])
region_msk = st.selectbox("Region Moscow", [0, 1])
region_nng = st.selectbox("Region Nizhny Novgorod", [0, 1])
region_nsk = st.selectbox("Region Novosibirsk", [0, 1])
region_spb = st.selectbox("Region Saint Petersburg", [0, 1])

# Прогнозирование цены
input_data = [
    [
        total_area,
        rooms_count,
        floor,
        floors_number,
        isСomplete,
        longitude,
        latitude,
        is_auction,
        region_ekb,
        region_kzn,
        region_msk,
        region_nng,
        region_nsk,
        region_spb,
    ]
]
predicted_price = model.predict(input_data)

# Вывод предсказанной цены
st.subheader("Predicted Price:")
st.write(predicted_price)
