# Заголовок приложения
st.title("House Price Prediction App")


if st.button("Главная страница"):
    st.switch_page("app.py")


def get_pos(lat, lng):
    return lat, lng


m = fl.Map(
    location=[55.751244, 37.618423], zoom_start=10, tiles="CartoDB Positron"
)

m.add_child(fl.LatLngPopup())

map = st_folium(m, height=350, width=700)

data = None
if map.get("last_clicked"):
    data = get_pos(map["last_clicked"]["lat"], map["last_clicked"]["lng"])

if data is not None:
    st.write(data)  # Writes to the app
    print(data)  # Writes to terminal
    latit, longit = data


# Ввод данных пользователем
total_area = st.number_input("Total Area", min_value=0.0, step=0.01)
rooms_count = st.number_input("Number of Rooms", min_value=0.0, step=1.0)
floor = st.number_input("Floor", min_value=0.0, step=1.0)
floors_number = st.number_input(
    "Total Number of Floors", min_value=0.0, step=1.0
)
isСomplete = st.selectbox("Is the House Complete?", [0, 1])
latitude, longitude = 55, 37
latitude, longitude = get_pos(
    map["last_clicked"]["lat"], map["last_clicked"]["lng"]
)
is_auction = 0
# Создание списка регионов
regions = [
    "Ekaterinburg",
    "Kazan",
    "Moscow",
    "Nizhny Novgorod",
    "Novosibirsk",
    "Saint Petersburg",
]

# Использование st.multiselect для выбора регионов

selected_regions = st.multiselect("Выберите регион", regions, max_selections=1)

st.write(
    "Выбранный регион:",
    selected_regions[0] if selected_regions else "Ничего не выбрано",
)
region_ekb = 0
region_kzn = 0
region_msk = 0
region_nng = 0
region_nsk = 0
region_spb = 0
if selected_regions == "Ekaterinburg":
    region_ekb = 1
if selected_regions == "Kazan":
    region_kzn = 1
if selected_regions == "Moscow":
    region_msk = 1
if selected_regions == "Nizhny Novgorod":
    region_nng = 1
if selected_regions == "Novosibirsk":
    region_nsk = 1
if selected_regions == "Saint Petersburg":
    region_spb = 1

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

# Доп параметры для продажи
is_auction = st.selectbox("Is it an Auction?", [0, 1])


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
