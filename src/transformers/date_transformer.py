import pandas as pd
from core.interfaces import ITransformer

class DateTransformer(ITransformer):
    """ Procesa fechas y filtra por año"""
    
    def __init__(self, target_year: int = 2023):
        self.target_year = target_year
    
    def get_name(self) -> str:
        return f"DateTransformer(year={self.target_year})"
    
    def transform(self, data: pd.DataFrame) -> pd.DataFrame:
        """Convierte fechas y filtra por año"""
        df = data.copy()
        
        
        df['Fecha'] = pd.to_datetime(df['Fecha'])
        
        
        df = df[df['Fecha'].dt.year == self.target_year].copy()
        
        return df