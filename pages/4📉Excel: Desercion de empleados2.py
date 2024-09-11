
import streamlit as st

st.title("Analis de datos: Comida India en Excel")
st.subheader("Instrucciones: Seleccionar las pestañas del excel")

def embed_miro_map(url):
    st.components.v1.iframe(url, height=1500, width=2000 )

miro_map_url = "https://docs.google.com/spreadsheets/d/1IpwXuLDSs_jHTXheLIgqaucmcn3pAsFv/edit?usp=sharing&ouid=117542555051300908469&rtpof=true&sd=true"
embed_miro_map(miro_map_url)
