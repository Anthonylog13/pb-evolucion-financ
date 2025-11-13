import warnings
from pipeline.pipeline_builder import PipelineBuilder
from utils.logger import ConsoleLogger


warnings.filterwarnings('ignore')

def main():
    """Punto de entrada de la aplicación"""
    
 
    logger = ConsoleLogger()
    
 
    pipeline = (PipelineBuilder(logger)
        .with_excel_extractor()         
        .with_cleaning()                
        .with_date_filtering(year=2023) 
        .with_enrichment()              
        .with_aggregation()             
        .with_excel_loader()            
        .build()
    )
    
   
    result = pipeline.execute(
        input_path='data/datos_ventas.xlsx',
        output_path='data/resumen_ventas.xlsx'
    )
    
    
    exit(0 if result.success else 1)


if __name__ == "__main__":
    main()