import folium
import joblib
import streamlit as st
from streamlit_folium import st_folium

st.set_page_config(
    page_title="UrbanRate", page_icon="🏠", initial_sidebar_state="auto"
)

model = joblib.load("model_xgb.joblib")

material_mapping = {
    "monolith": 1,
    "brick": 2,
    "monolithBrick": 3,
    "panel": 4,
    "block": 5,
    "unknown": 6,
    "old": 7,
    "stalin": 8,
    "wood": 9,
    "gasSilicateBlock": 10,
}

regions = [
    "Ekaterinburg",
    "Kazan",
    "Moscow",
    "Nizhny Novgorod",
    "Novosibirsk",
    "Saint Petersburg",
]

region_coordinates = {
    "Moscow": [55.751244, 37.618423],
    "Ekaterinburg": [56.8363, 60.5973],
    "Kazan": [55.7912, 49.1128],
    "Nizhny Novgorod": [56.3238, 43.9353],
    "Novosibirsk": [55.0301, 82.9225],
    "Saint Petersburg": [59.9390, 30.3158],
}

st.title("House price prediction")

total_area = st.number_input(
    "Total Area", min_value=10.0, max_value=5000.0, step=0.01
)
rooms_count = st.number_input(
    "Number of rooms", min_value=1.0, max_value=100.0, step=1.0
)
floor = st.number_input("Floor", min_value=1.0, max_value=2000.0, step=1.0)
floors_number = st.number_input(
    "Total number of floors", min_value=1.0, max_value=2000.0, step=1.0
)
material_options = list(material_mapping.keys())
selected_material = st.selectbox(
    "Material house", material_options, index=None
)

if selected_material is None:
    house_material = None
else:
    house_material = material_mapping[selected_material]

col1, col2, col3 = st.columns(3)
with col1:
    checkbox_isСomplete = st.radio("Is the house built?", ["Yes", "No"])
    isСomplete = 1 if checkbox_isСomplete == "Yes" else 0
with col2:
    checkbox_balcony = st.radio("Is there a balcony?", ["Yes", "No"])
    balcony = 1 if checkbox_balcony == "Yes" else 0
with col3:
    checkbox_is_auction = st.radio("At the auction?", ["Yes", "No"])
    is_auction = 1 if checkbox_is_auction == "Yes" else 0

selected_region = st.selectbox("Select Region", regions)
region_values = [1 if region == selected_region else 0 for region in regions]

m = folium.Map(
    location=region_coordinates[selected_region],
    zoom_start=10,
    tiles="CartoDB Positron",
)

m.add_child(folium.LatLngPopup())
map = st_folium(m, height=500, width=700)

if map.get("last_clicked"):
    latitude = map["last_clicked"]["lat"]
    longitude = map["last_clicked"]["lng"]
else:
    latitude = None
    longitude = None

if (
    total_area is None
    or rooms_count is None
    or floor is None
    or floors_number is None
    or house_material is None
    or balcony is None
    or is_auction is None
    or latitude is None
    or longitude is None
):
    st.warning(
        "Please fill in all fields and select a house or area on the map"
    )
else:
    input_data = [
        [
            total_area,
            rooms_count,
            floor,
            floors_number,
            isСomplete,
            house_material,
            balcony,
            longitude,
            latitude,
            is_auction,
            *region_values,
        ]
    ]
    predicted_price = model.predict(input_data)
    single_price = predicted_price.item()
    formatted_price = "{:,.2f}".format(single_price)
    st.success(f"##### Predicted price: {formatted_price} RUB")
