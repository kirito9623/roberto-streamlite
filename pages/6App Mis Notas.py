
import streamlit as st

def main():
    st.set_page_config(page_title="Proyecto Mis notas")

    # Enlace que deseas visualizar
    enlace = "https://misnotas-robertogonzalez.netlify.app/"

    # Título
    st.title("Proyecto mis Notas")

    # Visualización del enlace en un iframe
    st.components.v1.iframe(enlace, width=600, height=1000)

if __name__ == "__main__":
    main()