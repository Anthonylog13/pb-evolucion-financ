import pandas as pd
from typing import Optional, Dict
from core.interfaces import ITransformer

class DataAggregator(ITransformer):
    """ Agrega datos por dimensiones"""
    
    def __init__(self):
        self.resumen_vendedor: Optional[pd.DataFrame] = None
        self.resumen_mensual: Optional[pd.DataFrame] = None
        self.meses_nombres = {
            1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril',
            5: 'Mayo', 6: 'Junio', 7: 'Julio', 8: 'Agosto',
            9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'
        }
    
    def get_name(self) -> str:
        return "DataAggregator"
    
    def transform(self, data: pd.DataFrame) -> pd.DataFrame:
        """Agrega por vendedor y mes (guarda en atributos)"""
      
        self.resumen_vendedor = data.groupby('Vendedor').agg({
            'Total_Venta': 'sum',
            'ID_Venta': 'count'
        }).reset_index()
        
        self.resumen_vendedor.columns = ['Vendedor', 'Total_Ventas', 'Cantidad_Transacciones']
        self.resumen_vendedor = self.resumen_vendedor.sort_values('Total_Ventas', ascending=False)
        self.resumen_vendedor['Total_Ventas'] = self.resumen_vendedor['Total_Ventas'].round(2)
        
     
        self.resumen_mensual = data.groupby('Mes').agg({
            'Total_Venta': 'sum',
            'ID_Venta': 'count'
        }).reset_index()
        
        self.resumen_mensual.columns = ['Mes', 'Total_Ventas', 'Cantidad_Transacciones']
        self.resumen_mensual = self.resumen_mensual.sort_values('Mes')
        self.resumen_mensual['Total_Ventas'] = self.resumen_mensual['Total_Ventas'].round(2)
        self.resumen_mensual['Nombre_Mes'] = self.resumen_mensual['Mes'].map(self.meses_nombres)
        
    
        return data
    
    def get_aggregated_data(self) -> Dict[str, pd.DataFrame]:
        """Retorna los datos agregados"""
        return {
            'vendedor': self.resumen_vendedor,
            'mensual': self.resumen_mensual
        }