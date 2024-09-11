import streamlit as st
from streamlit_option_menu import option_menu
import altair as alt
import pandas as pd
import streamlit as st

st.title("Roberto Gonzalez Carranza")

col1, col2 = st.columns([2, 1])

col1.subheader("Analista de datos Trainee")
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
    """Soy un apasionado de los datos y la inteligencia artificial, siempre buscando maneras de utilizar estas herramientas para resolver problemas y generar valor.

Estoy en constante búsqueda de nuevas oportunidades para aprender y crecer, explorando cómo la tecnología puede mejorar tanto la vida personal como el mundo profesional. Además, disfruto del crecimiento personal y del levantamiento de pesas, actividades que complementan mi mentalidad de disciplina y resiliencia, esenciales para enfrentar cualquier reto.

Mi propósito es claro: ayudar a otros y colaborar en proyectos que impulsen la innovación tecnológica y promuevan un futuro más justo y equitativo. Estoy abierto a nuevas oportunidades donde pueda aplicar mis habilidades y seguir contribuyendo a proyectos innovadores y de impacto.
    """)

st.subheader("Tecnologías")

# Menú desplegable horizontal
def backend():
    df = pd.DataFrame({
        'Tecnología': ["Linux", "PostgreSQL", "Wordpress", "AWS"],
        'Academia': ["Linux Fundation", "University of Michigan", "Autodidacta", "AWS"],
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
        'Academia': ["Autodidacta", "Kodekloud.com"],
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

with st.expander('Consultor Tecnológico | Freelance'):
    st.write("""
    * Consultor Tecnológico: Mayo 2024 - Presente
    * Empresas: Covaro SAC | AC arquitectos
        * Marketing digital: Generación de 500 potenciales clientes mediante campañas de Meta Ads en Facebook.
        * Desarrollo web: HTML, CSS, Wordpress, Elementor.
        * Inteligencia artificial: Gestión y desarrollo de GPT especializado en normas técnicas y legales peruanas para revisores de Habilitaciones Urbanas y Edificaciones.
    * Enlace: https://covarosac.com
    """)

with st.expander('Reinvención Profesional'):
    st.write("""
    * Reinvención Profesional: Julio 2022 - presente
        * PROYECTO DE ANÁLISIS DE DATOS: 
        * Título: Portafolio
        * Tecnologías: Python, Streamlit, Linux
        * Enlace: https://robertogonzalez.streamlit.app/ --- EN PROGRESO
    """)

with st.expander('Emprendimiento en Ingeniería Civil'):
    st.write("""
    * GLOBAL INGENIEROS - Medio tiempo: Enero 2016 - presente
    * Gestión de todas las etapas de consultoría de seguridad en edificaciones, siendo el cliente principal la cadena transnacional CENCOSUD para Metro, Wong, tiendas Paris en diferentes ciudades de Perú.
    www.globalingenieros.com
    """)

with st.expander("Desarrollador Junior (Wordpress, CSS, HTML)"):
    st.write("""
    * AC ARQUITECTOS - Medio tiempo: Enero 2022 - Marzo 2023
        * Mejora de la página web, creación de formularios para filtrar clientes.
        * Mejora del Frontend, utilizando plugins y editando CSS.
        * Inicio de base de datos en Google Earth.
        * Implementación de seguimiento de clientes usando Monday.
        * Creación de campañas publicitarias con Google ADS.
        * Uso de LinkedIn Sales Navigator, 60% más oportunidades de negocio.
    """)

with st.expander("Co-fundador de Empresa de Blogs"):
    st.write("""
    * Pondomedia - Medio tiempo: Octubre 2014 - Diciembre 2015
        * Empresa que desarrollaba blogs para audiencias de habla hispana utilizando análisis web y SEO (Optimización en Motores de Búsqueda).
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
