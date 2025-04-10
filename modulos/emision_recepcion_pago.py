import pandas as pd
import plotly.express as px

def crear_grafico_fecha_proveedor(df):
    """
    Crea un gráfico de dispersión para la relación entre Fecha de Emisión, Fecha de Recepción y Fecha Estimada de Pago.
    
    Args:
        df: DataFrame con los datos de proveedores.
    
    Returns:
        fig: Figura de plotly con el gráfico de dispersión.
    """
    # Asegurarse de que las columnas de fechas estén en formato datetime
    df['Fecha de Emisión'] = pd.to_datetime(df['Fecha de Emisión'], errors='coerce')
    df['Fecha Recepción'] = pd.to_datetime(df['Fecha Recepción'], errors='coerce')
    df['Fecha Estimada Pago'] = pd.to_datetime(df['Fecha Estimada Pago'], errors='coerce')

    # Crear una columna para la diferencia de fechas (emisión vs recepción)
    df['Diferencia Fecha Recepción'] = (df['Fecha Recepción'] - df['Fecha de Emisión']).dt.days
    df['Diferencia Fecha Pago Estimado'] = (df['Fecha Estimada Pago'] - df['Fecha de Emisión']).dt.days

    # Clasificamos en dos grupos: "Emisión" y "Recepción" para ambos casos
    df['Color Recepción'] = df['Diferencia Fecha Recepción'].apply(lambda x: 'Emisión' if x <= 0 else 'Recepción')
    df['Color Pago'] = df['Diferencia Fecha Pago Estimado'].apply(lambda x: 'Emisión' if x <= 0 else 'Recepción')

    # Crear gráfico de dispersión para la relación Fecha de Emisión vs Fecha de Recepción
    fig = px.scatter(df, 
                     x='Fecha de Emisión', 
                     y='Fecha Recepción',
                     title='Fecha de Emisión vs. Fecha de Recepción y Fecha Estimada de Pago',
                     labels={'Fecha de Emisión': 'Fecha de Emisión', 'Fecha Recepción': 'Fecha de Recepción'},
                     color='Color Recepción',  # Diferenciar por el valor de la columna 'Color Recepción'
                     color_discrete_map={'Emisión': 'orange', 'Recepción': 'deepskyblue'},  # Colores para Emisión y Recepción
                     hover_data={'Nº Factura': True, 'Proveedor Facturador': True, 'Fecha de Emisión': True, 'Fecha Recepción': True})  # Mostrar fechas exactas al interactuar

    # Añadir los puntos para "Fecha Estimada Pago" sobre el mismo gráfico con etiquetas interactivas
    fig.add_scatter(x=df['Fecha de Emisión'], 
                    y=df['Fecha Estimada Pago'],
                    mode='markers', 
                    marker=dict(color='red', symbol='circle'),  # Color para los puntos de "Fecha Estimada Pago"
                    name="Fecha Estimada Pago",
                    hovertemplate=
                    'Fecha Estimada de Pago: %{y}<br>' +
                    'Fecha de Emisión: %{x}<br>' +
                    'Nº Factura: %{customdata[0]}<br>' +
                    'Proveedor Facturador: %{customdata[1]}',  # Personalización de la etiqueta
                    customdata=df[['Nº Factura', 'Proveedor Facturador']])  # Incluir datos personalizados para las etiquetas interactivas

    # Mejorar el diseño del gráfico
    fig.update_layout(
        xaxis_title='Fecha de Emisión',
        yaxis_title='Fecha de Recepción & Pago',
        xaxis_tickangle=45,
        template='plotly_dark',
        title_x=0.5,
        margin={'l': 50, 'r': 50, 't': 50, 'b': 50},
        hovermode="closest",  # Mostrar detalles al pasar el mouse
        legend_title="Estado"
    )

    return fig
