from abc import ABC, abstractmethod
from typing import Any, Dict
import pandas as pd

class IExtractor(ABC):
    """Contract: Extractor de datos"""
    
    @abstractmethod
    def extract(self, source: str) -> pd.DataFrame:
        """Extrae datos desde una fuente"""
        pass

class ITransformer(ABC):
    """Contract: Transformador de datos"""
    
    @abstractmethod
    def transform(self, data: pd.DataFrame) -> pd.DataFrame:
        """Transforma el DataFrame"""
        pass
    
    @abstractmethod
    def get_name(self) -> str:
        """Nombre del transformador para logging"""
        pass

class ILoader(ABC):
    """Contract: Cargador de datos"""
    
    @abstractmethod
    def load(self, data: Dict[str, pd.DataFrame], destination: str) -> bool:
        """Carga datos a destino"""
        pass

class ILogger(ABC):
    """Contract: Sistema de logging"""
    
    @abstractmethod
    def info(self, message: str) -> None:
        pass
    
    @abstractmethod
    def success(self, message: str) -> None:
        pass
    
    @abstractmethod
    def warning(self, message: str) -> None:
        pass
    
    @abstractmethod
    def error(self, message: str) -> None:
        pass