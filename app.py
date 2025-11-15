import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Leer los datos del archivo CSV en un DataFrame

car_data = pd.read_csv('vehicles_us.csv')

st.header('Tipos de vehiculos con más de 1000 anuncios')

type_counts = car_data['type'].value_counts()
popular_types = type_counts[type_counts > 1000]
popular_types_list = popular_types.index.tolist()
print(popular_types_list)

car_data[car_data['type'].isin(popular_types_list)]
car_data.sample(30)

# GRAFICO 1
st.header('Precios de venta en vehiculos')

# Crear un botón en la aplicación Streamlit
histogram_button = st.button('Graficar histograma')

# Inicializar session_state para recordar qué gráficos mostrar
if 'show_histogram' not in st.session_state:
    st.session_state.show_histogram = False

if histogram_button:
    # Recordar que se presionó el botón.
    st.session_state.show_histogram = True

# Mostrar el histograma si el estado dice que debe mostrarse
if st.session_state.show_histogram:
    st.write('Creación de Histogramas sobre precios de ventas de vehiculos')
    fig = go.Figure(
        data=[go.Histogram(x=car_data['price'])])

    # Añadir un título al gráfico
    fig.update_layout(title_text='Distribución Precios')

    # Personalizar escalas de los ejes
    fig.update_layout(
        xaxis=dict(
            title="Precio (miles)",
            range=[0, 200000],  # Rango específico
            tickmode='linear',  # Modo de marcas
            tick0=0,  # Primer tick
            dtick=50000  # Intervalo entre ticks
        ),
        yaxis=dict(
            title="Frecuencia",
            range=[0, 3000]  # Rango del eje Y
        )
    )

# Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
# 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)


# GRAFICO 2
st.header('Relación Precio - Kilometraje')

# Crear un Checkbox en la aplicación Streamlit
scatter_checkbox = st.checkbox('Mostrar Diagrama de Dispersión')

if scatter_checkbox:
    st.write('Grafica Dispersión Precio Venta vs Millas recorridas')
    fig = go.Figure(data=[go.Scatter(x=car_data['price'],
                                     y=car_data['odometer'], mode='markers')])

# Añadir un título al gráfico y nombres a los ejes
    fig.update_layout(
        title_text='Relación entre Precio y Millas',
        xaxis=dict(title="Precio ($)"),
        yaxis=dict(title="Millas")
    )

    # Configurar escalas
    fig.update_layout(
        xaxis=dict(
            range=[0, 250000],  # rango del eje x
            type="linear"       # tipo de escala
        ),
        yaxis=dict(
            range=[0, 1500000],   # rango del eje y
            type="linear"       # tipo de escala
        )
    )

# Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
# 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)
