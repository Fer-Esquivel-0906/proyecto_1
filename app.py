import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Lee los datos necesarios para el proyecto.
cars = pd.read_csv('vehicles_us.csv')

cars_automatic = cars[cars['transmission']=='automatic']
cars_manual = cars[cars['transmission']=='manual']
cars_ot = cars[cars['transmission']=='other']

# Crear una figura vacía  
fig = go.Figure()

#Checkbox para seleccionar el tipo de gráfico
st.write('Selecciona el tipo de gráfico')
hist = st.checkbox('Histograma')
disp = st.checkbox('Dispersión')

# Lógica para hacer el gráfico de dispersión
if disp:
    # Agregar la posibilidad de filtrar
    st.write('Selecciona si quieres filtrar algún tipo de transmisión en especial')
    auto = st.checkbox('Mostrar transmisión automática')
    manual = st.checkbox('Mostrar transmisión manual')
    otro = st.checkbox('Mostrar otros tipos de transmisión')
    no_filter = st.checkbox('Mostrar todos los tipos de transmisión sin distinción')
    
    # Lógica para no permitir que el usuario seleccione no_filter a la vez que otra checkbox , pero que cualquier otra combinación sea posible
    if no_filter:
         fig.add_trace(go.Scatter(x=cars['odometer'],
                                 y=cars['price'],
                                 mode='markers'))
    else:
        if auto:
            fig.add_trace(go.Scatter(x=cars_automatic['odometer'],
                                     y=cars_automatic['price'],
                                     mode='markers',
                                     name='Transmisión automática',
                                     marker=dict(color='rgba(54, 162, 235, 0.6)')))
        if manual:
            fig.add_trace(go.Scatter(x=cars_manual['odometer'],
                                     y=cars_manual['price'],
                                     mode='markers',
                                     name='Transmisión manual',
                                     marker=dict(color='rgba(255, 99, 132, 0.6)')))
        if otro:
            fig.add_trace(go.Scatter(x=cars_ot['odometer'],
                                     y=cars_ot['price'],
                                     mode='markers',
                                     name='Otra',
                                     marker=dict(color='rgba(75, 192, 192, 0.6)')))
    
    # Realizar el gráfico, no permitir que el usuario gráfique sin seleccionar al menos un checkbox
    graf = st.button('Graficar')
    if graf:
        fig.update_layout(title_text='Relación entre el odómetro y el precio de un vehículo.')
        if fig.data:
            fig.update_layout(title='Relación entre odómetro y precio', xaxis_title='Odómetro', yaxis_title='Precio')
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("Selecciona al menos una opción para mostrar el gráfico.")

if hist:
    st.write('¿De que variable quieres ver la distribución?')
    odo = st.checkbox('Odómetro')
    year =st.checkbox('Año del modelo')
    price = st.checkbox('Precio de venta')
  
    if odo:
        fig.add_trace(go.Histogram(x=cars['odometer']))
        fig.update_layout(title='Dispersión del odómetro')
        st.plotly_chart(fig, use_container_width=True)
    
    elif year:
        fig.add_trace(go.Histogram(x=cars['model_year']))
        fig.update_layout(title='Dispersión del año del modelo')
        st.plotly_chart(fig, use_container_width=True)

    elif price:
        fig.add_trace(go.Histogram(x=cars['price']))
        fig.update_layout(title='Dispersión del precio de venta')
        st.plotly_chart(fig, use_container_width=True)