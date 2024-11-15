import streamlit as st

# Título principal
st.title("Modelamiento de Bases de Datos")

# Descripción general
st.write("Aquí puedes encontrar poryectos bases de datos disponibles en GitHub. Haz clic en los enlaces para ver los proyectos.")

# Lista de proyectos
proyectos = [
    
        {
        "nombre": "Plataforma Educativa - Base de Datos",
        "descripcion": """Este proyecto explora el diseño y análisis de una plataforma educativa basada en bases de datos. 
        Incluye consultas avanzadas en SQL, modelado relacional y visualizaciones de métricas clave para entender 
        el comportamiento de los usuarios.""",
        "enlace_github": "https://github.com/kirito9623/bd_education_platform"
    },
    
 
]

# Mostrar proyectos
for proyecto in proyectos:
    st.header(proyecto["nombre"])
    st.write(proyecto["descripcion"])
    st.markdown(f"[Ver en GitHub]({proyecto['enlace_github']})")
