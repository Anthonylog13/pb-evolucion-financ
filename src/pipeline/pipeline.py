import time
import pandas as pd
from typing import List, Optional, Dict
from core.interfaces import ILogger, IExtractor, ITransformer, ILoader
from core.domain import PipelineResult
from transformers.data_aggregator import DataAggregator
from pipeline.pipeline_step import PipelineStep

class Pipeline:
    """Pipeline ETL principal - Orquesta todo el flujo"""
    
    def __init__(self, logger: ILogger):
        self.logger = logger
        self.extractor: Optional[IExtractor] = None
        self.transformers: List[ITransformer] = []
        self.loader: Optional[ILoader] = None
        self.aggregator: Optional[DataAggregator] = None
    
    def set_extractor(self, extractor: IExtractor) -> 'Pipeline':
        """Configura el extractor """
        self.extractor = extractor
        return self
    
    def add_transformer(self, transformer: ITransformer) -> 'Pipeline':
        """Agrega un transformador al pipeline"""
        self.transformers.append(transformer)
        
        
        if isinstance(transformer, DataAggregator):
            self.aggregator = transformer
        
        return self
    
    def set_loader(self, loader: ILoader) -> 'Pipeline':
        """Configura el loader"""
        self.loader = loader
        return self
    
    def execute(self, input_path: str, output_path: str) -> PipelineResult:
        """Ejecuta el pipeline completo ETL"""
        start_time = time.time()
        result = PipelineResult(
            success=False,
            records_input=0,
            records_output=0,
            execution_time=0.0
        )
        
        try:
            self.logger.info("=" * 70)
            self.logger.info(" INICIANDO PIPELINE ETL - ANÁLISIS DE VENTAS")
            self.logger.info("=" * 70)
            
            
            if not self.extractor:
                raise ValueError("Extractor no configurado")
            
            df = self.extractor.extract(input_path)
            if df is None:
                raise ValueError("Extracción falló")
            
            result.records_input = len(df)
            result.steps_executed.append("Extract")
            
            
            self.logger.info("\n FASE DE TRANSFORMACIÓN")
            for transformer in self.transformers:
                step = PipelineStep(transformer, self.logger)
                df = step.execute(df)
                result.steps_executed.append(transformer.get_name())
            
            result.records_output = len(df)
            
            
            self.logger.info("\n FASE DE CARGA")
            if not self.loader:
                raise ValueError("Loader no configurado")
            
            
            if self.aggregator:
                aggregated = self.aggregator.get_aggregated_data()
                load_data = {
                    'Resumen_Ventas': aggregated['vendedor'],
                    'Ventas_Mensuales': aggregated['mensual']
                }
            else:
                load_data = {'Datos': df}
            
            if not self.loader.load(load_data, output_path):
                raise ValueError("Carga falló")
            
            result.steps_executed.append("Load")
            
            
            if self.aggregator:
                self._mostrar_estadisticas(df, aggregated)
            
           
            result.success = True
            result.execution_time = time.time() - start_time
            
            self.logger.info("\n" + "=" * 70)
            self.logger.success(" PIPELINE COMPLETADO EXITOSAMENTE")
            self.logger.info(f"  Tiempo de ejecución: {result.execution_time:.2f}s")
            self.logger.info(f" Registros procesados: {result.records_input} a {result.records_output}")
            self.logger.info("=" * 70 + "\n")
            
        except Exception as e:
            result.success = False
            result.errors.append(str(e))
            self.logger.error(f"\n ERROR EN PIPELINE: {str(e)}")
            result.execution_time = time.time() - start_time
        
        return result
    
    def _mostrar_estadisticas(self, df: pd.DataFrame, aggregated: Dict[str, pd.DataFrame]):
        """Muestra estadísticas del análisis (Post-ETL)"""
        vendedor_df = aggregated['vendedor']
        mensual_df = aggregated['mensual']
        
        total_ventas = df['Total_Venta'].sum()
        total_transacciones = len(df)
        promedio_venta = df['Total_Venta'].mean()
        
        print("\n" + "=" * 70)
        print(" ESTADÍSTICAS GENERALES - AÑO 2023")
        print("=" * 70)
        
        print(f"Total de ventas: ${total_ventas:,.2f}")
        print(f" Total de transacciones: {total_transacciones}")
        print(f" Promedio por venta: ${promedio_venta:,.2f}")
        
        print(f" TOP 3 VENDEDORES:")
        for i, row in vendedor_df.head(3).iterrows():
            print(f"   {i+1}. {row['Vendedor']}: ${row['Total_Ventas']:,.2f}")
        
        mejor_mes_row = mensual_df.loc[mensual_df['Total_Ventas'].idxmax()]
        print(f" MEJOR MES:")
        print(f"   {mejor_mes_row['Nombre_Mes']}: ${mejor_mes_row['Total_Ventas']:,.2f}")
        
        print("\n" + "=" * 70 + "\n")