from observador import Observador
from typing import Type

class Orquestrador:

    def __init__(self):
        self.functions = []
    
    def addFunc(self, func: Type[Observador]):
        self.functions.append(func)

    def order(self):
        for func in self.functions:
            func.update()

