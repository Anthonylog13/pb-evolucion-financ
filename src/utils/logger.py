from core.interfaces import ILogger

class ConsoleLogger(ILogger):
    """Logger concreto: Imprime a consola con formato"""
    
    def info(self, message: str) -> None:
        print(f"{message}")
    
    def success(self, message: str) -> None:
        print(f"{message}")
    
    def warning(self, message: str) -> None:
        print(f" {message}")
    
    def error(self, message: str) -> None:
        print(f" {message}")