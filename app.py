import pandas as pd
import plotly.express as px
import streamlit as st

# Leer el archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Título de la aplicación
st.title("Análisis de Anuncios de Coches")

# Botón para construir histograma
if st.button('Construir Histograma'):
    st.write("Histograma de Odómetro")
    fig = px.histogram(car_data, x="odometer", title="Distribución del Odómetro")
    st.plotly_chart(fig, use_container_width=True)

# Botón para construir gráfico de dispersión
if st.button('Construir Gráfico de Dispersión'):
    st.write("Gráfico de Dispersión: Precio vs Odómetro")
    fig = px.scatter(car_data, x="odometer", y="price", title="Precio vs Odómetro")
    st.plotly_chart(fig, use_container_width=True)