import pandas as pd
import plotly.express as px

def crear_tendencia_costos(df):
    """
    Crea un gráfico de línea para la tendencia evolutiva diaria de los costos en el tiempo.
    
    Args:
        df: DataFrame con los datos de facturación (Proveedor, Fecha de Emisión, Monto Total).
    
    Returns:
        fig: Figura de plotly con el gráfico de la tendencia evolutiva de los costos.
    """
    # Agrupar los datos por fecha de emisión y sumar el monto total
    cost_trend = df.groupby('Fecha de Emisión')['Monto Total'].sum().reset_index()

    # Asegurar que la columna 'Fecha de Emisión' esté en formato datetime
    cost_trend['Fecha de Emisión'] = pd.to_datetime(cost_trend['Fecha de Emisión'], format='%d-%m-%Y')

    # Ordenar por fecha
    cost_trend = cost_trend.sort_values('Fecha de Emisión')

    # Crear el gráfico de línea de tendencia usando Plotly
    fig = px.line(
        cost_trend,
        x='Fecha de Emisión',
        y='Monto Total',
        title='Tendencia Evolutiva Diaria de los Costos en el Tiempo',
        labels={'Fecha de Emisión': 'Fecha de Emisión', 'Monto Total': 'Monto Total'},
        line_shape='linear',  # Forma de la línea, mejor para tendencias claras
        markers=False,  # Sin marcadores, solo línea continua
        color_discrete_sequence=["deepskyblue"],  # Color de la línea (tono profesional)
    )

    # Mejorar el diseño del gráfico
    fig.update_layout(
        xaxis_title='Fecha de Emisión',  # Título del eje X
        yaxis_title='Monto Total',       # Título del eje Y
        xaxis_tickangle=45,              # Ángulo de las etiquetas del eje X
        template='plotly_dark',          # Estilo oscuro para un look ejecutivo
        title_x=0.5,                     # Centrar el título
        margin={'l': 50, 'r': 50, 't': 50, 'b': 50},  # Ajustar márgenes
        hovermode="closest",             # Mejor interacción con los puntos
        showlegend=False,                # Eliminar la leyenda, ya que solo hay una línea
    )

    # Mejorar la visualización de las fechas (Ajustar el formato de fecha)
    fig.update_xaxes(
        tickformat="%b %Y",  # Mostrar las fechas en formato Mes Año (Ene 2024, Feb 2024)
        tickmode='array',    # Para asegurar que las fechas se muestren bien
        showticklabels=True  # Mostrar las etiquetas de las fechas en el eje X
    )

    # Cambiar la visualización del tooltip para mostrar la fecha completa y sin el signo de peso en el monto
    fig.update_traces(
        hovertemplate="<b>%{x}</b><br>Monto Total: %{y:,.0f}<extra></extra>",  # Mostrar monto sin el signo de peso
    )

    return fig
