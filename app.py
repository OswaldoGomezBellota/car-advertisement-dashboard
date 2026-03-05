import pandas as pd # Librería para manipulación de datos
import plotly.express as px # Librería para gráficos interactivos (Dispersión, Histograma, Barra, Linea, etc.)
import streamlit as st # Para construir el dashboard

# Leer dataset
car_data = pd.read_csv("vehicles_us.csv")
# Crear encabezado del dashboard
st.header("Dashboard de anuncios de venta de vehículos")
# Mostrar vista previa del dataset
st.write("Vista previa del dataset:")
st.dataframe(car_data.head())
# Botón para construir histograma del odómetro
hist_button = st.button("Construir histograma del odómetro")
# Si el botón es presionado, mostrar el histograma
if hist_button:
    st.write("Histograma del odómetro")
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)
    
# Botón para construir gráfico de dispersión Precio vs Odómetro
scatter_button = st.button("Construir gráfico de dispersión Precio vs Odómetro")
# Si el botón es presionado, mostrar el gráfico de dispersión
if scatter_button:
    st.write("Gráfico de dispersión Precio vs Odómetro")
    fig_scatter = px.scatter(
        car_data,
        x="odometer",
        y="price"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)