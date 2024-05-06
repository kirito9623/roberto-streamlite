
import streamlit as st

def embed_miro_map(url):
    st.components.v1.iframe(url, height=1500, width=2000 )

miro_map_url = "https://docs.google.com/spreadsheets/d/1zJ_ZbPkgvdk0_pLYXRzmOAhgviTMYO5RACoJLQpSsFE/edit#gid=1290258572"
embed_miro_map(miro_map_url)
