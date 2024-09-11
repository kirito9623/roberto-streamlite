
import streamlit as st

st.title("Analis de datos: Comida India en Excel")
st.subheader("Instrucciones: Seleccionar las pestañas del excel")

def embed_miro_map(url):
    st.components.v1.iframe(url, height=1500, width=2000 )

miro_map_url = "https://docs.google.com/spreadsheets/d/1rR5UAMp2rnff1wti6L8p_ojyFqFzkaHEOax34uoHTl8/edit?usp=sharing"
embed_miro_map(miro_map_url)
