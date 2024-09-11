import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Introducción y objetivo del análisis
st.title("Análisis de Producción de Petróleo y Gas en los EE.UU. (2008-2018)")

st.write("""
### Objetivo:
Este ejercicio demuestra el potencial de **Streamlit** y **Python** para realizar análisis de datos y generar gráficos interactivos en la web. Utilizando Streamlit, puedes integrar visualizaciones dinámicas y análisis exploratorio directamente en una aplicación web, sin necesidad de conocimientos avanzados en desarrollo web. 

En este proyecto, estamos analizando la producción de gas y petróleo crudo en los Estados Unidos a lo largo de una década (2008-2018), utilizando datos obtenidos a través de Google Drive. El objetivo es explorar tendencias clave y comparar la producción entre diferentes estados y tipos de energía.

### Lo que se está logrando:
Con este ejercicio, es aprender cómo:
- Crear aplicaciones web dinámicas para análisis de datos con **Streamlite**.
- Obtener reportés automáticos de análisis de datos
- Realizar análisis exploratorio utilizando **Python** y bibliotecas como **pandas** y **matplotlib**.
- Presentar visualizaciones y comparaciones significativas directamente en la web.

### Ventajas de obtener reportes de análisis de datos en la web:
- Acceso inmediato: Los informes se pueden visualizar desde cualquier lugar con acceso a Internet, sin necesidad de descargar archivos o instalar software especializado.
- Interactividad: Los gráficos y visualizaciones son interactivos, lo que permite explorar los datos de manera dinámica.
- Actualización en tiempo real: Los datos pueden actualizarse automáticamente, garantizando que siempre se trabaje con la información más reciente.
- Fácil colaboración: Compartir un enlace permite que varios usuarios accedan simultáneamente a los datos, facilitando la colaboración.
- Visualización atractiva: La web ofrece un entorno rico para gráficos interactivos y visualizaciones claras.
- Automatización y escalabilidad: Cambiar los datos y obtener nuevos reportes es simple, lo que permite generar análisis de manera automatizada y a gran escala.


#### Enlace del archivo:
[Archivo de datos](https://drive.google.com/file/d/12EVTdTm-5Is4Q7Lyrgi43wf-BB9JwImb/view?usp=sharing)

Para cambiar el archivo, simplemente se sustituye el ID en la URL por el nuevo archivo en el siguiente formato:
`https://drive.google.com/uc?id=FILE_ID`, y así podemos tener el reporte de todos los meses de forma automática,
solo debemos cambiar la URL.

### Gráficos y análisis:
1. **Gráfico de Producción de Gas en Estados Seleccionados**: Muestra la producción anual de gas en Colorado, Louisiana, Ohio, y Utah.
2. **Comparación de Producción de Gas y Petróleo**: Un gráfico de barras que compara la producción total anual de gas y petróleo crudo en los EE.UU.

### Instrucciones:
Para cambiar el archivo y sacar reportes de otros períodos o regiones, simplemente cambia el enlace del archivo CSV en el código.
""")

# URL de descarga directa del archivo en Google Drive
url = 'https://drive.google.com/uc?id=12EVTdTm-5Is4Q7Lyrgi43wf-BB9JwImb'

# Lee el archivo CSV directamente desde Google Drive
gas_df = pd.read_csv(url, decimal=",")

# Convertir la columna 'Month' a formato de fecha
gas_df['Month'] = pd.to_datetime(gas_df['Month'])

# Excluir las columnas de tipo 'datetime' antes de realizar la suma
# Solo seleccionamos columnas numéricas para evitar el error con las fechas
numeric_cols = gas_df.select_dtypes(include=[np.number]).columns

# Agrupar por año y sumar solo las columnas numéricas
yearly_gas_df = gas_df.groupby(gas_df['Month'].dt.year)[numeric_cols].sum()

# Muestra la producción anual desglosada por estado
st.write("Producción Anual Desglosada por Estado:")
st.write(yearly_gas_df)

# Agrupar solo por año y sumar la producción de gas para obtener el total anual de EE.UU.
filtered_yearly_gas_df = gas_df.groupby(gas_df['Month'].dt.year)[numeric_cols].sum().reset_index()
st.write("\nProducción Total Anual de EE.UU.:")
st.write(filtered_yearly_gas_df)

# **Gráfico de producción de gas en estados seleccionados**:
st.write("Gráfico de Producción de Gas en Estados Seleccionados (Colorado, Louisiana, Ohio, Utah):")
plot = filtered_yearly_gas_df.filter(items=['Colorado', 'Louisiana', 'Ohio', 'Utah']).plot()
plt.xlabel("Año")
plt.ylabel("Producción de Gas")
st.pyplot(plt)

# Cargar los datos de producción de petróleo crudo
oil_df = pd.read_csv('https://drive.google.com/uc?id=12EVTdTm-5Is4Q7Lyrgi43wf-BB9JwImb', decimal=",")

# Convertir la columna 'Month' a formato datetime
oil_df['Month'] = pd.to_datetime(oil_df['Month'])

# Agrupar por año y sumar la producción de petróleo crudo para obtener el total anual de EE.UU.
yearly_oil_df = oil_df.groupby(oil_df['Month'].dt.year)[numeric_cols].sum().reset_index()

# Muestra las primeras filas del DataFrame resultante
st.write("Producción Anual de Petróleo Crudo:")
st.write(yearly_oil_df.head())

# **Verificar que los DataFrames no estén vacíos antes de hacer el merge**
if not yearly_gas_df.empty and not yearly_oil_df.empty:
    # Comparación entre producción de gas y petróleo crudo
    st.write("Comparación de Producción de Gas y Petróleo Crudo en EE.UU.")
    merged_df = pd.merge(yearly_gas_df, yearly_oil_df, left_index=True, right_index=True, suffixes=('_Gas', '_Oil'))
    
    # Verificar que el DataFrame merged_df no esté vacío antes de graficar
    if not merged_df.empty:
        plot = merged_df.plot(kind="bar")
        plt.xlabel("Año")
        plt.legend(['Gas (Millones de pies cúbicos)', 'Petróleo Crudo (Miles de barriles)'])
        st.pyplot(plt)
    else:
        st.write("No hay datos para graficar después del merge.")
else:
    st.write("Los datos de producción de gas o petróleo están vacíos. No se puede realizar el análisis comparativo.")
