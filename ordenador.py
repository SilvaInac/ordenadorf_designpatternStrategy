from abc import ABC, abstractclassmethod

#Strategy interface
class Strategy(ABC):

    @abstractclassmethod

    def selection(self) -> None:
        pass
    
class crescente(Strategy):
    
    def __init__(self,listaData) -> None:
        self.listaData = []
        self.listaData = listaData
        
    def selection(self) -> str:
        return self.listaData.sort()

class Ordenar:
    """
    The Context defines the interface of interest to clients.
    """
    def __init__(self,strategy: Strategy) -> None:
        self._strategy = strategy