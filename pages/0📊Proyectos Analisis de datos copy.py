import streamlit as st

# Título principal
st.title("Proyectos de Análisis de Datos")

# Descripción general
st.write("Aquí puedes encontrar una lista de proyectos de análisis de datos disponibles en Google Colab y GitHub. Haz clic en los enlaces para ver los proyectos.")

# Lista de proyectos
proyectos = [
    {
        "nombre": "Análisis de Datos de Iris",
        "descripcion": """El Iris Data Set es un conjunto de datos presentado por Ronald Fisher. 
        Este consiste en la medición del ancho y largo del pétalo y sépalo de 3 especies de la planta Iris 
        (Iris setosa, Iris virginica e Iris versicolor). El conjunto de datos fue presentado por Fisher en 
        su artículo de 1936 'The use of multiple measurements in taxonomic problems'. 
        El conjunto de datos es usado como puerta de entrada para explicar conceptos vinculados con la exploración de datos.""",
        "enlace_colab": "https://colab.research.google.com/github/kirito9623/analisis-de-datos/blob/main/EDA_iris.ipynb",
        "enlace_github": "https://github.com/kirito9623/analisis-de-datos/blob/main/EDA_iris.ipynb"
    },
    {
        "nombre": "Análisis Exploratorio de Datos (EDA) para la Venta de Equipos Móviles",
        "descripcion": """El objetivo de este trabajo es realizar un Análisis Exploratorio de Datos (EDA) 
        para entender mejor el negocio de la venta de equipos móviles y responder a preguntas clave de la gerencia.""",
        "enlace_colab": "https://colab.research.google.com/github/kirito9623/analisis-de-datos/blob/main/reporte-celulares.ipynb",
        "enlace_github": "https://github.com/kirito9623/analisis-de-datos/blob/main/reporte-celulares.ipynb"
    },
    {
        "nombre": "Reporte de Acciones Apple",
        "descripcion": """Este proyecto realiza un análisis de las acciones de Apple, evaluando su rendimiento
        y comportamiento a lo largo del tiempo.""",
        "enlace_colab": "https://colab.research.google.com/github/kirito9623/analisis-de-datos/blob/main/reporte-acciones-apple.ipynb",
        "enlace_github": "https://github.com/kirito9623/analisis-de-datos/blob/main/reporte-acciones-apple.ipynb"
    }
]

# Mostrar proyectos
for proyecto in proyectos:
    st.header(proyecto["nombre"])
    st.write(proyecto["descripcion"])
    st.markdown(f"[Ver en Colab]({proyecto['enlace_colab']})")
    st.markdown(f"[Ver en GitHub]({proyecto['enlace_github']})")
