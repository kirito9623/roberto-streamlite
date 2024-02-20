import streamlit as st
import folium
from streamlit_folium import folium_static

# Datos de empleo en tecnología en Perú (ejemplo)
empleo_tecnologia = {
    "Lima": 500,
    "Arequipa": 200,
    "Cusco": 100,
    # ... otros departamentos ...
}

# Crear un mapa Folium
m = folium.Map(location=[-9.19, -75.0152], zoom_start=5)

# Agregar marcadores al mapa
for departamento, empleo in empleo_tecnologia.items():
    popup_text = f"{departamento}: Empleo en Tecnología = {empleo}"
    folium.Marker(
        location=[-9.19, -75.0152],
        popup=popup_text,
        icon=folium.Icon(color="blue")
    ).add_to(m)

# Mostrar el mapa en Streamlit usando folium_static
st.title("Mapa del Empleo en Tecnología en Perú")
st.markdown("Este mapa muestra el empleo en tecnología en diferentes departamentos de Perú.")
folium_static(m)
