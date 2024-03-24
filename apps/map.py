import folium
import pandas as pd

# Предполагается, что df - это ваш DataFrame
# df = pd.read_csv('your_data.csv')

# Создание карты
m = folium.Map(
    location=[55.751244, 37.618423], zoom_start=10, tiles="CartoDB Positron"
)

# Функция для определения цвета маркера в зависимости от цены
def get_color(price):
    if price < 10000000:
        return "green"
    elif price < 20000000:
        return "orange"
    else:
        return "red"


# Фиксированный радиус для всех маркеров
fixed_radius = 3

# Функция для определения размера маркера в зависимости от общей площади
def get_radius(area):
    return area / 25  # Примерно, чтобы размеры были разумными


# Добавление маркеров на карту
for index, row in df.iterrows():
    folium.CircleMarker(
        location=[row["latitude"], row["longitude"]],
        radius=fixed_radius,
        color=get_color(row["price"]),
        fill=True,
        fill_color=get_color(row["price"]),
        popup=f"Цена: {row['price']} руб., Площадь: {row['total_area']} кв.м.",
    ).add_to(m)

# geojson_file = 'ao.geojson' # загрузка границ районов города

# Добавление слоя GeoJSON
# folium.GeoJson(
#     geojson_file,
#     name='geojson'
# ).add_to(m)

# Добавление маркера, который создается при клике на карту
# Всплывающее окно маркера будет отображать координаты места клика
m.add_child(
    folium.ClickForMarker("<b>Lat:</b> ${lat}<br /><b>Lon:</b> ${lng}")
)

# Отображение карты
m
