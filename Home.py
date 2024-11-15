import streamlit as st
from streamlit_option_menu import option_menu
import altair as alt
import pandas as pd
import streamlit as st

st.title("Roberto Gonzalez Carranza")

col1, col2 = st.columns([2, 1])

col1.subheader("Analista de datos ")
col1.image("./images/aaa.png", caption="¡Este soy yo!", use_column_width=None)

col2.subheader("Contacto")
col2.write("""
    * Trujillo, Perú (GMT-5)
    * (+51) 948907318
    * https://github.com/kirito9623
    * https://www.linkedin.com/in/roberto-gonzalez-developer/
    """)

st.subheader("Acerca de mí")
st.markdown(
    """Ingeniero con 7 años de experiencia profesional, con una sólida base en gestión de proyectos y análisis de
datos. Cuento con 6 años de experiencia en gestión de proyectos, trabajando en consultoría en diferentes
ciudades del Perú, para una empresa transnacional, esta experiencia me ha permitido desarrollar
habilidades clave como toma de decisiones bajo presión y la capacidad de resolver problemas.
Durante el último año, me he especializado en análisis de datos, adquiriendo experiencia Python, SQL, SQL
Server Transact-SQL, Power BI y Excel para extraer, limpiar y analizar datos a gran escala, generando
insights estratégicos y visualizaciones de alto impacto, asimismo tengo experiencia en la creación de
dashboards para campañas de marketing.
Soy creativo, dinámico y orientado a resultados, con capacidad para trabajar en equipo. Actualmente, busco
desarrollarme como analista de datos, aplicando mis conocimie
    """)

st.subheader("Tecnologías")

# Menú desplegable horizontal
def backend():
    df = pd.DataFrame({
        'Tecnología': ["Linux", "SQL" , 'SQL Server Transact-SQL', "PostgreSQL", "Wordpress", "AWS"],
        'Academia': ["Linux Fundation", "DSRP","DSRP","University of Michigan", "Autodidacta", "AWS"],
    })
    st.write(df)

def frontend():
    df = pd.DataFrame({
        'Tecnología': ["HTML", "CSS", "Sass", "Bootstrap"],
        'Academia': ["TECSUP", "TECSUP", "TECSUP", "TECSUP"],
    })
    st.write(df)

def languages():
    df = pd.DataFrame({
        'Lenguaje': ["Python", "Go"],
        'Academia': ["DSRP", "Kodekloud.com"],
    })
    st.write(df)

def others(): 
    df = pd.DataFrame({
        'Tecnología': ["Git", "Docker", "Soporte Técnico", "Ingeniería Civil"],
        'Academia': ["Kodekloud.com", "Kodekloud.com", "Google", "UPAO(Perú))"],
    })
    st.write(df)

selected2 = option_menu(None, ["Backend", "Frontend", "Lenguajes", 'Otros'], 
    icons=['database', 'window-fullscreen', "code-square", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal")

if selected2 == "Backend":
    backend()
elif selected2 == "Frontend":
    frontend()
elif selected2 == "Lenguajes":
    languages()
elif selected2 == "Otros":
    others()

# Experiencia laboral
st.subheader("Experiencia Laboral")

with st.expander('Analista de Datos| Freelance'):
    st.write("""
    * Analista de Datos: Mayo 2024 - Presente
    * Empresas: Covaro SAC | AC arquitectos
        * Generé 3 dashboards en Looker Studio para el control de KPIs de campañas de marketing, mejorando la
        visibilidad del rendimiento y la toma de decisiones estratégicas.
        * Optimicé 10 campañas de marketing digital en Facebook Ads, logrando un incremento del 20% en la tasa
        de conversión y mejorando el retorno de inversión (ROI).
        * Implementé un proceso de integración que extrae en tiempo real los datos de campañas de Facebook
        Ads hacia Looker Studio, optimizando la actualización de reportes en un 80%.
        * Aumenté en un 40% la captación de leads mediante el desarrollo de una landing page optimizada dentro
        de un funnel de ventas, redirigiendo a grupos de WhatsApp y mejorando la interacción y el engagement.
        * Diseñe, desarrollé y desplegué la página web:  https://covarosac.com
    """)


with st.expander('Emprendimiento en Ingeniería Civil'):
    st.write("""
    * GLOBAL INGENIEROS - Medio tiempo: Enero 2016 - Abril 2024
        * Gestioné más de 50 expedientes técnicos para renovar certificados de seguridad en edificaciones de un
        promedio de 5,000 m² de área ocupada, cumpliendo con normativas ante diversas municipalidades en
        Perú.
        * Redacté 50 informes técnicos con recomendaciones específicas para mejorar la seguridad y el
        cumplimiento normativo de las edificaciones.
        * Desarrollé 50 presupuestos para implementar mejoras de seguridad, optimizando costos y recursos en
        cada proyecto.
        * Revisé y actualicé 300 planos (arquitectura, seguridad y eléctricos), alineando toda la documentación
        con requisitos regulatorios.
        * Participé en 50 inspecciones técnicas de edificaciones de alto riesgo, asegurando la correcta
        implementación de normas de seguridad.
        * Supervisé la subcontratación de 15 profesionales especializados en seguridad y construcción,
        garantizando la calidad de las soluciones.
        * Coordiné la colaboración de 60 personas, incluyendo 20 jefes de tienda, 20 jefes de seguridad, 20 jefes de
        mantenimiento, arquitectos e ingenieros, facilitando el levantamiento de observaciones y la ejecución de
        mejoras técnicas en 50 edificaciones, lo que resultó en una mejora del 70% en el cumplimiento
        normativo.
        * Gestioné 50 órdenes de compra y procesé 50 facturas en el sistema de proveedores de Cencosud,
        logrando un cobro puntual y un ahorro promedio del 15% en costos operativos.
    """)
    
col1, col2 = st.columns([2, 1])

col1.subheader("Habilidades")
col1.write("""
    * Proactivo
    * Aprendizaje rápido
    * Trabajo en equipo
    """)

col2.subheader("Idiomas Hablados")
col2.write("""
    * Español: Nativo
    * Inglés: CEFR - B2 Intermedio Superior
    """)


st.header("Portafolio de Proyectos")

st.markdown("""
## Descripción
Este portafolio presenta una serie de proyectos desarrollados con **Streamlit** y **Python**, diseñados para realizar análisis de datos de manera interactiva y accesible. La aplicación permite visualizar datos en tiempo real y explorar resultados de forma intuitiva, sin necesidad de conocimientos avanzados en desarrollo web. 

Los proyectos aquí mostrados ejemplifican cómo se pueden utilizar herramientas de análisis de datos en entornos accesibles y visuales para apoyar la toma de decisiones estratégicas, con la ayuda de bibliotecas y tecnologías modernas.

## Tecnologías Utilizadas
Para el desarrollo de estos proyectos se han empleado las siguientes tecnologías:

- **Python**: Lenguaje de programación principal para la manipulación de datos.
- **Streamlit**: Framework para crear aplicaciones web interactivas y visualizaciones en tiempo real.
- **Pandas**: Biblioteca para manipulación y análisis de datos.
- **Matplotlib**: Biblioteca para crear visualizaciones de datos.
- **Excel**: Fuente de datos para algunos proyectos.
- **Google Drive**: Almacenamiento y fuente de datos externos.

## Objetivo y Logros
Este portafolio permite explorar cómo:

- **Crear aplicaciones web dinámicas** para análisis de datos utilizando Streamlit.
- **Generar reportes automáticos** de análisis de datos de manera continua, facilitando la actualización y revisión de la información.
- **Realizar análisis exploratorio** de datos utilizando Python y bibliotecas como pandas y matplotlib para extraer tendencias y patrones significativos.
- **Presentar visualizaciones y comparaciones** de datos directamente en la web, lo que permite a los usuarios interactuar y entender los datos de manera visual y fácil.

""")


