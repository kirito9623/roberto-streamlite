
import streamlit as st

st.title("Planificador semanal")

st.sidebar.header("Selecciona el día")

day = st.sidebar.selectbox("Día", ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"])

st.write("El día de hoy es:", day)

st.header("Tareas")

tasks = st.multiselect("Tareas", ["Tarea 1", "Tarea 2", "Tarea 3", "Tarea 4", "Tarea 5"])

if tasks:
    st.write("Las tareas para hoy son:", tasks)