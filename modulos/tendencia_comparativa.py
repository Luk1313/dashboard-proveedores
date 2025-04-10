import pandas as pd
import plotly.graph_objects as go

def crear_tendencia_comparativa_costos(df):
    """
    Crea un gráfico comparativo de la tendencia evolutiva de los costos en los años 2023, 2024 y 2025.
    
    Args:
        df: DataFrame con los datos de facturación (Proveedor, Fecha de Emisión, Monto Total).
    
    Returns:
        fig: Figura de plotly con el gráfico de la tendencia comparativa de los costos.
    """
    # Asegurarse de que la columna 'Fecha de Emisión' esté en formato datetime
    df['Fecha de Emisión'] = pd.to_datetime(df['Fecha de Emisión'], format='%d-%m-%Y')

    # Filtrar los datos para 2023, 2024 y 2025
    cost_trend_2023 = df[df['Fecha de Emisión'].dt.year == 2023]
    cost_trend_2024 = df[df['Fecha de Emisión'].dt.year == 2024]
    cost_trend_2025 = df[df['Fecha de Emisión'].dt.year == 2025]

    # Agrupar los datos por mes y año, sumando el monto total para 2023, 2024 y 2025
    cost_trend_2023_monthly = cost_trend_2023.groupby(pd.Grouper(key='Fecha de Emisión', freq='ME'))['Monto Total'].sum().reset_index()
    cost_trend_2024_monthly = cost_trend_2024.groupby(pd.Grouper(key='Fecha de Emisión', freq='ME'))['Monto Total'].sum().reset_index()
    cost_trend_2025_monthly = cost_trend_2025.groupby(pd.Grouper(key='Fecha de Emisión', freq='ME'))['Monto Total'].sum().reset_index()

    # Filtrar solo los primeros tres meses de 2025
    cost_trend_2025_monthly = cost_trend_2025_monthly[cost_trend_2025_monthly['Fecha de Emisión'].dt.month <= 3]

    # Crear una figura para mostrar las tres líneas comparativas en el mismo gráfico
    fig = go.Figure()

    # Añadir la línea para 2023
    fig.add_trace(go.Scatter(
        x=cost_trend_2023_monthly['Fecha de Emisión'],
        y=cost_trend_2023_monthly['Monto Total'],
        mode='lines',
        name='2023',
        line=dict(color='deepskyblue', width=3),  # Color de la línea para 2023
    ))

    # Añadir la línea para 2024
    fig.add_trace(go.Scatter(
        x=cost_trend_2024_monthly['Fecha de Emisión'],
        y=cost_trend_2024_monthly['Monto Total'],
        mode='lines',
        name='2024',
        line=dict(color='orange', width=3),  # Color de la línea para 2024
    ))

    # Añadir la línea para 2025 (solo los primeros tres meses)
    fig.add_trace(go.Scatter(
        x=cost_trend_2025_monthly['Fecha de Emisión'],
        y=cost_trend_2025_monthly['Monto Total'],
        mode='lines',
        name='2025',
        line=dict(color='yellow', width=3, dash='dot'),  # Línea para 2025, en color amarillo y con línea discontinua
    ))

    # Mejorar el diseño del gráfico
    fig.update_layout(
        title='Tendencia Evolutiva Comparativa de los Costos 2023 - 2024 - 2025',
        xaxis_title='Fecha de Emisión',
        yaxis_title='Monto Total',
        xaxis_tickangle=45,
        template='plotly_dark',  # Estilo oscuro para un look profesional
        title_x=0.5,
        margin={'l': 50, 'r': 50, 't': 50, 'b': 50},  # Ajustar márgenes
        hovermode="closest",             # Mejor interacción con los puntos
        showlegend=True,                 # Mostrar leyenda para identificar las líneas de 2023, 2024 y 2025
        yaxis=dict(range=[0, max(cost_trend_2023_monthly['Monto Total'].max(),
                                 cost_trend_2024_monthly['Monto Total'].max(),
                                 cost_trend_2025_monthly['Monto Total'].max())]),  # Ajustar rango del eje Y
    )

    # Mejorar la visualización de las fechas (Ajustar el formato de fecha)
    fig.update_xaxes(
        tickformat="%b %Y",  # Mostrar las fechas en formato Mes Año (Ene 2024, Feb 2024)
        tickmode='array',    # Para asegurar que las fechas se muestren bien
        showticklabels=True  # Mostrar las etiquetas de las fechas en el eje X
    )

    # Cambiar la visualización del tooltip para mostrar la fecha completa al pasar el cursor
    fig.update_traces(
        hovertemplate="<b>%{x}</b><br>Monto Total: $%{y:,.0f}<extra></extra>",  # Fecha completa en el hover
    )

    return fig

