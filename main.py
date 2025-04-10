import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Importar funciones desde los módulos locales
from módulos.preparar_datos import preparar_columnas_fecha
from módulos.Proveedores_Principales import (
    crear_barras_proveedores_top,
    crear_barras_monto_total,
    crear_barras_monto_promedio
)
from módulos.emisión_recepción_pago import crear_grafico_fecha_proveedor
from módulos.tendencia_comparativa import crear_tendencia_comparativa_costos
from módulos.Tendencia_diaria_evolutiva import crear_tendencia_costos
from módulos.tendencia_evolutiva_mensual import crear_tendencia_mensual_costos

# Cargar y preparar los datos
df = pd.read_excel("datos_proveedores.xlsx")
df = preparar_columnas_fecha(df)

# Crear aplicación Dash
aplicación = dash.Dash(__name__)
aplicación.title = "Panel de Proveedores"

# Disposición de la app
aplicación.layout = html.Div([
    html.H1("Análisis de Proveedores", className="título-del-encabezado"),

    html.Div([
        html.H2("Top 10 Proveedores por Número de Facturas"),
        dcc.Graph(id='top-proveedores', figure=crear_barras_proveedores_top(df)),
    ], className="card"),

    html.Div([
        html.H2("Proveedores por Monto Total"),
        dcc.Graph(id='grafico-monto-total', figure=crear_barras_monto_total(df)),
    ], className="card"),

    html.Div([
        html.H2("Proveedores por Monto Promedio"),
        dcc.Graph(id='grafico-monto-promedio', figure=crear_barras_monto_promedio(df)),
    ], className="card"),

    html.Div([
        html.H2("Tendencia Diaria Evolutiva de los Costos"),
        dcc.Graph(id='tendencia-diaria-evolutiva', figure=crear_tendencia_costos(df)),
    ], className="card"),

    html.Div([
        html.H2("Tendencia Evolutiva Mensual de los Costos"),
        dcc.Graph(id='tendencia-evolutiva-mensual', figure=crear_tendencia_mensual_costos(df)),
    ], className="card"),

    html.Div([
        html.H2("Tendencia Comparativa de los Costos (2023 - 2025)"),
        dcc.Graph(id='tendencia-comparativa', figure=crear_tendencia_comparativa_costos(df)),
    ], className="card"),

    html.Div([
        html.H2("Fechas de Emisión, Recepción y Pago"),
        dcc.Graph(id='grafico-fechas', figure=crear_grafico_fecha_proveedor(df)),
    ], className="card"),
])

# Para que Render pueda ejecutarla
server = aplicación.server

# Ejecutar localmente
if __name__ == '__main__':
    aplicación.run_server(debug=True)


