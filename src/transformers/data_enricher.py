import pandas as pd
from core.interfaces import ITransformer

class DataEnricher(ITransformer):
    """ Enriquece datos con columnas adicionales"""
    
    def get_name(self) -> str:
        return "DataEnricher"
    
    def transform(self, data: pd.DataFrame) -> pd.DataFrame:
        """Agrega columna Mes"""
        df = data.copy()
        df['Mes'] = df['Fecha'].dt.month
        return df