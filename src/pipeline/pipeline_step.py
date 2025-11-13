import pandas as pd
from core.interfaces import ITransformer, ILogger

class PipelineStep:
    """Representa un paso individual en el pipeline"""
    
    def __init__(self, transformer: ITransformer, logger: ILogger):
        self.transformer = transformer
        self.logger = logger
    
    def execute(self, data: pd.DataFrame) -> pd.DataFrame:
        """Ejecuta el paso de transformación"""
        step_name = self.transformer.get_name()
        self.logger.info(f"  Ejecutando: {step_name}")
        
        result = self.transformer.transform(data)
        
        self.logger.success(f" {step_name} completado - {len(result)} registros")
        return result