import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Importar funciones desde los módulos locales
from modulos.preparar_datos import preparar_columnas_fecha
from modulos.Proveedores_Principales import (
    crear_barras_proveedores_top,
    crear_barras_monto_total,
    crear_barras_monto_promedio,
)
from modulos.emision_recepcion_pago import crear_grafico_fecha_proveedor
from modulos.tendencia_comparativa import crear_tendencia_comparativa_costos
from modulos.Tendencia_diaria_evolutiva import crear_tendencia_costos
from modulos.tendencia_evolutiva_mensual import crear_tendencia_mensual_costos

# Cargar y preparar los datos
df = pd.read_excel("data_proveedores.xlsx")
df = preparar_columnas_fecha(df)

# Crear app Dash
app = dash.Dash(__name__)
app.title = "Dashboard de Proveedores"

# Layout
app.layout = html.Div([
    html.H1("Análisis de Proveedores", className="header-title"),

    html.Div([
        html.H2("Top 10 Proveedores por Número de Facturas", className="card-title"),
        dcc.Graph(id="top-proveedores", figure=crear_barras_proveedores_top(df)),
    ], className="card"),

    html.Div([
        html.H2("Proveedores por Monto Total", className="card-title"),
        dcc.Graph(id="grafico-monto-total", figure=crear_barras_monto_total(df)),
    ], className="card"),

    html.Div([
        html.H2("Proveedores por Monto Promedio", className="card-title"),
        dcc.Graph(id="grafico-monto-promedio", figure=crear_barras_monto_promedio(df)),
    ], className="card"),

    html.Div([
        html.H2("Tendencia Diaria Evolutiva de los Costos", className="card-title"),
        dcc.Graph(id="tendencia-diaria-evolutiva", figure=crear_tendencia_costos(df)),
    ], className="card"),

    html.Div([
        html.H2("Tendencia Evolutiva Mensual de los Costos", className="card-title"),
        dcc.Graph(id="tendencia-evolutiva-mensual", figure=crear_tendencia_mensual_costos(df)),
    ], className="card"),

    html.Div([
        html.H2("Tendencia Comparativa de los Costos (2023 - 2025)", className="card-title"),
        dcc.Graph(id="tendencia-comparativa", figure=crear_tendencia_comparativa_costos(df)),
    ], className="card"),

    html.Div([
        html.H2("Fechas de Emisión, Recepción y Pago", className="card-title"),
        dcc.Graph(id="grafico-fechas", figure=crear_grafico_fecha_proveedor(df)),
    ], className="card"),
])

if __name__ == '__main__':
    aplicación.ejecutar(debug=True)

servidor = aplicación.servidor

