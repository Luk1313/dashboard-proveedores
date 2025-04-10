import plotly.express as px
import pandas as pd

def crear_barras_proveedores_top(df):
    """
    Crea un gráfico de barras con los 10 proveedores principales por número de facturas.
    
    Args:
        df: DataFrame con los datos de proveedores.
    
    Returns:
        fig: Figura de plotly con el gráfico de barras.
    """
    # Análisis de los 10 proveedores principales por número de facturas
    top_providers = df['Proveedor Facturador'].value_counts().head(10)
    
    # Convertimos el índice (proveedores) en una columna del DataFrame para evitar el conflicto
    top_providers_df = top_providers.reset_index()
    top_providers_df.columns = ['Proveedor', 'Número de Facturas']
    
    # Crear gráfico interactivo de barras
    fig = px.bar(
        top_providers_df,
        x='Proveedor',
        y='Número de Facturas',
        labels={'x': 'Proveedor', 'y': 'Número de Facturas'},
        title='Top 10 Proveedores por Número de Facturas',
        text='Número de Facturas',
        hover_data={'Proveedor': True},
        color='Número de Facturas',
        color_continuous_scale='Blues'
    )

    # Mejorar la visualización del gráfico de proveedores
    fig.update_layout(
        xaxis_title='Proveedor',
        yaxis_title='Número de Facturas',
        xaxis_tickangle=45,
        xaxis={'showticklabels': False},
        yaxis_tickformat=',',
        template='plotly_dark',
        title_x=0.5,
        margin={'l': 50, 'r': 50, 't': 50, 'b': 50},
        hovermode="closest",
        showlegend=False
    )
    
    # Formatear las etiquetas de las barras para mostrar el monto en pesos
    fig.update_traces(
        texttemplate='%{text:,.0f}',  # Formato con símbolo de peso y sin decimales
        textposition='outside',
        textfont=dict(color='white')
    )
    
    return fig


def crear_barras_monto_total(df):
    """
    Crea un gráfico de barras con el monto total por proveedor.
    
    Args:
        df: DataFrame con los datos de proveedores.
    
    Returns:
        fig: Figura de plotly con el gráfico de barras.
    """
    provider_amounts = df.groupby('Proveedor Facturador')['Monto Total'].sum().sort_values(ascending=False)
    
    provider_amounts_df = provider_amounts.head(10).reset_index()
    provider_amounts_df.columns = ['Proveedor', 'Monto Total']
    
    # Crear gráfico interactivo de barras para el monto total por proveedor
    fig = px.bar(
        provider_amounts_df,
        x='Proveedor',
        y='Monto Total',
        labels={'x': 'Proveedor', 'y': 'Monto Total'},
        title='Monto Total por Proveedor (Top 10)',
        text='Monto Total',
        hover_data={'Proveedor': True},
        color='Monto Total',
        color_continuous_scale='Viridis'
    )
    
    # Mejorar la visualización del gráfico de montos por proveedor
    fig.update_layout(
        xaxis_title='Proveedor',
        yaxis_title='Monto Total',
        xaxis_tickangle=45,
        xaxis={'showticklabels': False},
        yaxis_tickformat=',',
        template='plotly_dark',
        title_x=0.5,
        margin={'l': 50, 'r': 50, 't': 50, 'b': 50},
        hovermode="closest",
        showlegend=False
    )
    
    # Formatear las etiquetas de monto total para mostrar el símbolo de peso
    fig.update_traces(
        texttemplate='$%{text:,.0f}',  # Formato con símbolo de peso y sin decimales
        textposition='outside',
        textfont=dict(color='white')
    )
    
    return fig


def crear_barras_monto_promedio(df):
    """
    Crea un gráfico de barras con el monto promedio por proveedor.
    
    Args:
        df: DataFrame con los datos de proveedores.
    
    Returns:
        fig: Figura de plotly con el gráfico de barras.
    """
    average_invoice_amount = df.groupby('Proveedor Facturador')['Monto Total'].mean().sort_values(ascending=False)
    
    average_invoice_amount_df = average_invoice_amount.head(10).reset_index()
    average_invoice_amount_df.columns = ['Proveedor', 'Monto Promedio']
    
    # Crear gráfico interactivo de barras para el monto promedio por proveedor
    fig = px.bar(
        average_invoice_amount_df,
        x='Proveedor',
        y='Monto Promedio',
        labels={'x': 'Proveedor', 'y': 'Monto Promedio'},
        title='Monto Promedio por Proveedor (Top 10)',
        text='Monto Promedio',
        hover_data={'Proveedor': True},
        color='Monto Promedio',
        color_continuous_scale='Cividis'
    )
    
    # Mejorar la visualización del gráfico de monto promedio por proveedor
    fig.update_layout(
        xaxis_title='Proveedor',
        yaxis_title='Monto Promedio',
        xaxis_tickangle=45,
        xaxis={'showticklabels': False},
        yaxis_tickformat=',',
        template='plotly_dark',
        title_x=0.5,
        margin={'l': 50, 'r': 50, 't': 50, 'b': 50},
        hovermode="closest",
        showlegend=False
    )
    
    # Formatear los números en las etiquetas del gráfico para que no tengan decimales y mostrar el signo de peso
    fig.update_traces(
        texttemplate='$%{text:,.0f}',  # Eliminar decimales y mostrar el símbolo de peso
        textposition='outside',
        textfont=dict(color='white')
    )
    
    return fig
