import pandas as pd
from core.interfaces import ITransformer

class DataCleaner(ITransformer):
    """Transformador: Limpia y completa datos faltantes"""
    
    def get_name(self) -> str:
        return "DataCleaner"
    
    def transform(self, data: pd.DataFrame) -> pd.DataFrame:
        """Completa valores faltantes en Total_Venta"""
        df = data.copy()
        
        missing_count = df['Total_Venta'].isna().sum()
        if missing_count > 0:
            df['Total_Venta'] = df.apply(
                lambda row: row['Cantidad'] * row['Precio_Unitario']
                if pd.isna(row['Total_Venta'])
                else row['Total_Venta'],
                axis=1
            )
        
        return df