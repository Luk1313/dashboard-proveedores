import pandas as pd
import plotly.express as px

def crear_tendencia_mensual_costos(df):
    """
    Crea un gráfico de línea para la tendencia evolutiva mensual de los costos en el tiempo.
    
    Args:
        df: DataFrame con los datos de proveedores.
    
    Returns:
        fig: Figura de plotly con el gráfico de la tendencia evolutiva de los costos.
    """
    # Asegurar que la columna 'Fecha de Emisión' esté en formato datetime
    df['Fecha de Emisión'] = pd.to_datetime(df['Fecha de Emisión'], format='%d-%m-%Y')

    # Agrupar los datos por mes y año, sumando el monto total
    cost_trend_monthly = df.groupby(pd.Grouper(key='Fecha de Emisión', freq='ME'))['Monto Total'].sum().reset_index()

    # Crear el gráfico de línea de tendencia usando Plotly
    fig = px.line(
        cost_trend_monthly,
        x='Fecha de Emisión',
        y='Monto Total',
        title='Tendencia Evolutiva Mensual de los Costos',
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
        showticklabels=True  # Mostrar las etiquetas de las fechas en el eje X (meses y años)
    )

    # Cambiar la visualización del tooltip para mostrar la fecha completa al pasar el cursor
    fig.update_traces(
        hovertemplate="<b>%{x}</b><br>Monto Total: $%{y:,.0f}<extra></extra>",  # Fecha completa en el hover
    )

    return fig
