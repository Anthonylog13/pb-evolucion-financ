from dataclasses import dataclass, field
from typing import List

@dataclass
class ResumenVendedor:
    """Value Object: Resumen por vendedor"""
    vendedor: str
    total_ventas: float
    cantidad_transacciones: int

@dataclass
class ResumenMensual:
    """Value Object: Resumen mensual"""
    mes: int
    nombre_mes: str
    total_ventas: float
    cantidad_transacciones: int

@dataclass
class PipelineResult:
    """Value Object: Resultado del pipeline"""
    success: bool
    records_input: int
    records_output: int
    execution_time: float
    steps_executed: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)