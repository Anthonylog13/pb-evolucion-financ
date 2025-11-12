import pandas as pd
from typing import Optional
from core.interfaces import IExtractor, ILogger

class ExcelExtractor(IExtractor):
    """Extractor: Lee datos desde Excel"""
    
    def __init__(self, logger: ILogger):
        self.logger = logger
    
    def extract(self, source: str) -> Optional[pd.DataFrame]:
        """Extrae datos desde archivo Excel"""
        try:
            self.logger.info(f" Extrayendo datos desde: {source}")
            df = pd.read_excel(source)
            self.logger.success(f" Extraídos {len(df)} registros")
            return df
        except FileNotFoundError:
            self.logger.error(f" Archivo no encontrado: {source}")
            return None
        except Exception as e:
            self.logger.error(f" Error en extracción: {str(e)}")
            return None