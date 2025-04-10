import plotly.express as px
import pandas as pd
import numpy as np

def crear_scatter_depth_magnitude(df):
    """
    Crea un scatter plot de profundidad vs magnitud de los sismos

    Args:
        df: DataFrame con los datos de sismos

    Returns:
        fig: Figura de plotly con el scatter plot
    """
    # Crear una copia del dataframe para no modificar el original
    df_scatter = df.copy()
    
    # Crear una columna para el año
    df_scatter['Year'] = pd.to_datetime(df_scatter['Date(UTC)']).dt.year
    
    # Crear el scatter plot
    fig = px.scatter(
        df_scatter,
        x='Magnitude',
        y='Depth',
        color='Year',
        size='Magnitude',
        size_max=15,
        opacity=0.7,
        color_continuous_scale='Viridis',
        title='Relación entre Profundidad y Magnitud de Sismos',
        labels={
            'Magnitude': 'Magnitud',
            'Depth': 'Profundidad (km)',
            'Year': 'Año'
        },
        hover_data={
            'Date(UTC)': True,
            'Latitude': ':.2f',
            'Longitude': ':.2f',
            'Magnitude': ':.1f',
            'Depth': True,
            'Year': False
        }
    )
    
    # Personalizar el layout
    fig.update_layout(
        xaxis_title='Magnitud',
        yaxis_title='Profundidad (km)',
        plot_bgcolor='white',
        yaxis=dict(
            autorange='reversed',  # Invertir el eje Y para que la profundidad aumente hacia abajo
            zeroline=True,
            zerolinewidth=1,
            zerolinecolor='#CCCCCC'
        ),
        xaxis=dict(
            zeroline=True,
            zerolinewidth=1,
            zerolinecolor='#CCCCCC',
            range=[2.5, 9]
        )
    )
    
    # Añadir líneas de referencia para las zonas de profundidad
    fig.add_hline(y=70, line_width=1, line_dash='dash', line_color='gray', 
                 annotation_text='Superficial (<70 km)', annotation_position='left')
    fig.add_hline(y=150, line_width=1, line_dash='dash', line_color='gray', 
                 annotation_text='Intermedio (70-150 km)', annotation_position='left')
    fig.add_hline(y=300, line_width=1, line_dash='dash', line_color='gray', 
                 annotation_text='Profundo (>150 km)', annotation_position='left')
    
    # Añadir líneas de referencia para las categorías de magnitud
    fig.add_vline(x=5.0, line_width=1, line_dash='dash', line_color='rgba(231, 76, 60, 0.5)', 
                 annotation_text='Moderado (5.0)', annotation_position='top')
    fig.add_vline(x=6.0, line_width=1, line_dash='dash', line_color='rgba(211, 84, 0, 0.5)', 
                 annotation_text='Fuerte (6.0)', annotation_position='top')
    fig.add_vline(x=7.0, line_width=1, line_dash='dash', line_color='rgba(192, 57, 43, 0.5)', 
                 annotation_text='Mayor (7.0)', annotation_position='top')
    fig.add_vline(x=8.0, line_width=1, line_dash='dash', line_color='rgba(169, 50, 38, 0.5)', 
                 annotation_text='Gran (8.0)', annotation_position='top')
    
    # Añadir una línea de tendencia
    fig.update_traces(marker=dict(line=dict(width=0.5, color='DarkSlateGrey')))
    
    return fig
