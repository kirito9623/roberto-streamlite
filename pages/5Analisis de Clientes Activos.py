# Importa las bibliotecas necesarias
import streamlit as st
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Título de la aplicación
st.title('Analisis de Clientes Activo e Inactivos - Roberto')

st.write("Esta aplicación permite analizar y visualizar datos de clientes activos e inactivos contenidos en un archivo Excel.")
st.write("Carga el Archivo: Haz clic en BROWSW FILE y selecciona el archivo de datos que deseas analizar. La aplicación admite archivos en formato xlsx o xls.")


# Subida del archivo Excel
uploaded_file = st.file_uploader("Cargar archivo Excel", type=["xlsx", "xls"])

if uploaded_file is not None:
    # Lee el archivo Excel
    df = pd.read_excel(uploaded_file)

    # Calcula los años de activación e inactivación
    df['Año_Activacion'] = df['Fecha de Activación'].dt.year
    df['Año_Inactivacion'] = df['Fecha de Inactivación'].dt.year

    # Agrupa y cuenta clientes activos por año
    clientes_activos_por_año = df.groupby('Año_Activacion').size()

    # Agrupa y cuenta clientes inactivos por año
    clientes_inactivos_por_año = df.groupby('Año_Inactivacion').size()

    # Visualización de datos con Streamlit Charts
    st.subheader("Distribución de Clientes Activos e Inactivos por Año")
    st.bar_chart({'Activos': clientes_activos_por_año, 'Inactivos': clientes_inactivos_por_año})

    # Ajuste a una distribución normal (solo para fines demostrativos, puedes personalizar esto)
    st.subheader("Ajuste a Distribución Normal")
    st.write(f"Media de Activos: {clientes_activos_por_año.mean():.2f}")
    st.write(f"Desviación Estándar de Activos: {clientes_activos_por_año.std():.2f}")

    # Calcular ajuste a la distribución normal
    mu, std = stats.norm.fit(clientes_activos_por_año)
    xmin, xmax = min(clientes_activos_por_año), max(clientes_activos_por_año)
    x = np.linspace(xmin, xmax, 100)
    p = stats.norm.pdf(x, mu, std)

    # Visualizar la gráfica de densidad de probabilidad de la distribución normal
    st.subheader("Gráfica de Densidad de Probabilidad de la Distribución Normal")
    st.write("La gráfica compara los datos reales con la distribución normal ajustada.")
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(clientes_activos_por_año, density=True, alpha=0.6, color='b', bins=15, label='Datos de Activos')
    ax.plot(x, p, 'k', linewidth=2, label='Ajuste a Distribución Normal')
    ax.set_xlabel('Número de Clientes')
    ax.set_ylabel('Densidad de Probabilidad')
    ax.set_title('Distribución de Clientes Activos - Ajuste a Distribución Normal')
    ax.legend()
    st.pyplot(fig)
