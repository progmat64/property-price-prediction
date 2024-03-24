import folium as fl
import pandas as pd
import streamlit as st
from streamlit_folium import st_folium

geojson_file = "ao.geojson"  # загрузка границ районов города

# @st.cache_data
# def load_data():
#     return pd.read_parquet("clean_data.parquet")

# df = load_data()


def get_pos(lat, lng):
    return lat, lng


m = fl.Map(
    location=[55.751244, 37.618423], zoom_start=10, tiles="CartoDB Positron"
)

# Добавление слоя GeoJSON
fl.GeoJson(geojson_file, name="geojson").add_to(m)


# def get_color(price):
#     if price < 10000000:
#         return 'green'
#     elif price < 20000000:
#         return 'orange'
#     else:
#         return 'red'

# # Фиксированный радиус для всех маркеров
# fixed_radius = 3

# # Функция для определения размера маркера в зависимости от общей площади
# def get_radius(area):
#     return area / 25 # Примерно, чтобы размеры были разумными

# # Добавление маркеров на карту
# for index, row in df.iterrows():
#     fl.CircleMarker(
#         location=[row['latitude'], row['longitude']],
#         radius=fixed_radius,
#         color=get_color(row['price']),
#         fill=True,
#         fill_color=get_color(row['price']),
#         popup=f"Цена: {row['price']} руб., Площадь: {row['total_area']} кв.м."
#     ).add_to(m)


m.add_child(fl.LatLngPopup())

map = st_folium(m, height=350, width=700)


data = None
if map.get("last_clicked"):
    data = get_pos(map["last_clicked"]["lat"], map["last_clicked"]["lng"])

if data is not None:
    st.write(data)  # Writes to the app
    print(data)  # Writes to terminal
