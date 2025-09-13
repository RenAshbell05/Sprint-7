import streamlit as st
import pandas as pd
import plotly.express as px

# Leer datos
car_data = pd.read_csv('vehicles_us.csv')

st.header("Dashboard de Anuncios de Vehículos")

# Botón para histograma
if st.button('Construir histograma'):
    st.write('Histograma del odómetro')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Botón para gráfico de dispersión
if st.button('Construir gráfico de dispersión'):
    st.write('Precio vs Odómetro')
    fig2 = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig2, use_container_width=True)
