from core.interfaces import ILogger

class ConsoleLogger(ILogger):
    """ Imprime a consola con formato"""
    
    def info(self, message: str) -> None:
        print(f"[INFO]  {message}")
    
    def success(self, message: str) -> None:
        print(f"[SUCCESS] {message}")
    
    def warning(self, message: str) -> None:
        print(f" [WARNING] {message}")
    
    def error(self, message: str) -> None:
        print(f"[ERROR] {message}")