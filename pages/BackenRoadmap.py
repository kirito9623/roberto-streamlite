
import streamlit as st

def embed_miro_map(url):
    st.components.v1.iframe(url, height=2000, width=2000 )

miro_map_url = "https://miro.com/app/board/uXjVMsC1JYc=/"
embed_miro_map(miro_map_url)
