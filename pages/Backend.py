import streamlit as st

from streamlit_elements import elements, nivo, mui






st.title("Backend")

st.header("Estado del arte")

st.markdown("El backend es la parte de una aplicación web que maneja la lógica empresarial y los datos. Es responsable de procesar las solicitudes del usuario, acceder a la base de datos y generar la respuesta.")

st.markdown("El estado del arte en el backend es el desarrollo de aplicaciones web escalables y altamente disponibles. Esto se puede lograr utilizando tecnologías como contenedores, microservicios y nubes.")

st.header("Tendencias")

st.markdown("""Algunas de las tendencias más recientes en el backend incluyen:

* El uso de contenedores para crear aplicaciones web escalables y altamente disponibles.
* El desarrollo de microservicios para crear aplicaciones web más modulares y fáciles de mantener.
* El uso de nubes para alojar y administrar aplicaciones web.
* Inteligencia Artificial (IA), Aprendizaje Automático (AM), Aplicación web progresiva (PWA), Realidad Aumentada (RA), Realidad Virtual (RV), Arquitectura sin servidor y Aplicación de una sola página (SPA

            
Estas tendencias están permitiendo a los desarrolladores crear aplicaciones web más rápidas, más seguras y más escalables.""")

st.header("Tecnologías")

st.markdown("""Algunas de las tecnologías más populares para el desarrollo de backend incluyen:

* Java
* Python
* Javascript            
* PHP
* Go
* Ruby
* .NET
* Perl
""")
            
#PIE CHART

with elements("nivo_charts"):


    DATA = [
            {
                "id": "Go",
                "label": "Go",
                "value": 4.3,
                "color": "hsl(339, 70%, 50%)"
            },
            {
                "id": "Java",
                "label": "Java",
                "value": 17.4,
                "color": "hsl(303, 70%, 50%)"
            },
            {
                "id": "Php",
                "label": "Php",
                "value": 5.4,
                "color": "hsl(53, 70%, 50%)"
            },
            {
                "id": "Javascript",   
                "label": "Javascript",
                "value": 26.5,
                "color": "hsl(62, 70%, 50%)"
            },
            {
                "id": "Python",
                "label": "Python",
                "value": 34,
                "color": "hsl(12, 70%, 50%)"
            }
         ]
    

    with mui.Box(sx={"height": 500}):
        nivo.Pie(
            data=DATA,
            margin={ "top": 40, "right": 80, "bottom": 80, "left": 80 },
            innerRadius={0.5},
            padAngle={0.7},
            cornerRadius={3},
            activeOuterRadiusOffset={8},
            borderWidth={1},
            borderColor={"from": "color"},
            arcLinkLabelsSkipAngle={10},
            arcLinkLabelsTextColor="white",
            arcLinkLabelsThickness={2},
            arcLinkLabelsColor={ "from": "color" },
            arcLabelsSkipAngle={10},
            arcLabelsTextColor="black",
            defs=[
                {
                    "id": 'dots',
                    "type": 'patternDots',
                    "background": 'inherit',
                    "color": 'rgba(255, 255, 255, 0.3)',
                    "size": 4,
                    "padding": 1,
                    "stagger": True
                },
                {
                    "id": 'lines',
                    "type": 'patternLines',
                    "background": 'inherit',
                    "color": 'rgba(255, 255, 255, 0.3)',
                    "rotation": -45,
                    "lineWidth": 6,
                    "spacing": 10
                }
            ],
            fill=[
                {
                    "match": {
                        "id": 'Go'
                    },
                    "id": 'lines'
                },
                {
                    "match": {
                        "id": 'Php'
                    },
                    "id": 'lines'
                },
                
                {
                    "match": {
                        "id": 'Python'
                    },
                    "id": 'lines'
                },
    
                {
                    "match": {
                        "id": 'Javascript'
                    },
                    "id": 'dots'
                }
            ],

            legends=[
                {
                    "anchor": 'bottom',
                    "direction": 'row',
                    "justify": False,
                    "translateX": 0,
                    "translateY": 56,
                    "itemsSpacing": 0,
                    "itemWidth": 100,
                    "itemHeight": 18,
                    "itemTextColor": 'white',
                    "itemDirection": 'left-to-right',
                    "itemOpacity": 1,
                    "symbolSize": 18,
                    "symbolShape": 'circle',
                    "effects": [
                        {
                            "on": 'hover',
                            "style": {
                                "itemTextColor": '#80FF40'
                            }
                        }
                    ]
                }
            ],
    )   






st.header("Skill necesarias")

st.markdown("""Las habilidades necesarias para ser un desarrollador de backend incluyen:

* Conocimiento de programación
* Conocimiento de bases de datos
* Conocimiento de sistemas operativos
* Conocimiento de redes
* Conocimiento de seguridad
* Conocimiento de herramientas de desarrollo

Estas habilidades son esenciales para poder desarrollar y mantener aplicaciones web complejas.""")

            
st.header("Fuentes")