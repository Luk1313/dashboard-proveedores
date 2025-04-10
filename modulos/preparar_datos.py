# modulos/preparar_datos.py
import pandas as pd

def preparar_columnas_fecha(df):
    """
    Función para preparar las columnas de fechas en el DataFrame.
    Convierte las fechas a formato datetime y hace cualquier otro procesamiento necesario.

    Args:
        df: DataFrame que contiene las columnas de fechas a procesar.

    Returns:
        df: DataFrame con las columnas de fechas preparadas.
    """
    # Asegurarse de que las columnas de fecha estén en formato datetime
    df['Fecha Estimada Pago'] = pd.to_datetime(df['Fecha Estimada Pago'], errors='coerce', dayfirst=True)
    df['Fecha Recepción'] = pd.to_datetime(df['Fecha Recepción'], errors='coerce', dayfirst=True)
    df['Fecha de Emisión'] = pd.to_datetime(df['Fecha de Emisión'], errors='coerce', dayfirst=True)


    # Otros posibles pasos de limpieza o transformación aquí

    return df

