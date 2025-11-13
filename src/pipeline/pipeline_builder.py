from core.interfaces import ILogger
from pipeline.pipeline import Pipeline
from extractors.excel_extractor import ExcelExtractor
from transformers.data_cleaner import DataCleaner
from transformers.date_transformer import DateTransformer
from transformers.data_enricher import DataEnricher
from transformers.data_aggregator import DataAggregator
from loaders.excel_loader import ExcelLoader

class PipelineBuilder:
    """Builder para construir pipelines de forma fluida"""
    
    def __init__(self, logger: ILogger):
        self.logger = logger
        self.pipeline = Pipeline(logger)
    
    def with_excel_extractor(self) -> 'PipelineBuilder':
        """Configura extractor de Excel"""
        self.pipeline.set_extractor(ExcelExtractor(self.logger))
        return self
    
    def with_cleaning(self) -> 'PipelineBuilder':
        """Agrega paso de limpieza"""
        self.pipeline.add_transformer(DataCleaner())
        return self
    
    def with_date_filtering(self, year: int = 2023) -> 'PipelineBuilder':
        """Agrega transformación de fechas"""
        self.pipeline.add_transformer(DateTransformer(year))
        return self
    
    def with_enrichment(self) -> 'PipelineBuilder':
        """Agrega enriquecimiento de datos"""
        self.pipeline.add_transformer(DataEnricher())
        return self
    
    def with_aggregation(self) -> 'PipelineBuilder':
        """Agrega agregación de datos"""
        self.pipeline.add_transformer(DataAggregator())
        return self
    
    def with_excel_loader(self) -> 'PipelineBuilder':
        """Configura loader de Excel"""
        self.pipeline.set_loader(ExcelLoader(self.logger))
        return self
    
    def build(self) -> Pipeline:
        """Construye y retorna el pipeline"""
        return self.pipeline