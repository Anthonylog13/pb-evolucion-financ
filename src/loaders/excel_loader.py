import pandas as pd
from typing import Dict
from core.interfaces import ILoader, ILogger

class ExcelLoader(ILoader):
    """Exporta a Excel con múltiples hojas"""
    
    def __init__(self, logger: ILogger):
        self.logger = logger
    
    def load(self, data: Dict[str, pd.DataFrame], destination: str) -> bool:
        """Carga datos a archivo Excel con múltiples hojas"""
        try:
            self.logger.info(f" Cargando datos a: {destination}")
            
            with pd.ExcelWriter(destination, engine='openpyxl') as writer:
                for sheet_name, df in data.items():
                    df.to_excel(writer, sheet_name=sheet_name, index=False)
            
            self.logger.success(f" Datos cargados exitosamente")
            return True
            
        except Exception as e:
            self.logger.error(f"✗ Error en carga: {str(e)}")
            return False