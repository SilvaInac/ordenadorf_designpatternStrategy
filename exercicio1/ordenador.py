from abc import ABC, abstractclassmethod
import random

#Strategy interface
class Strategy(ABC):

    @abstractclassmethod

    def selection(self) -> None:
        pass
    
class Crescente(Strategy):
    def selection(self,lista = None) -> str:
        self.newList  = []
        for i in lista:
            self.newList.append(i)

        self.newList.sort()
        return (self.newList)

class Decrescente(Strategy):
    def selection(self,lista = None) -> str:
        self.newList  = []
        for i in lista:
            self.newList.append(i)

        self.newList.sort(reverse=1)
        return (self.newList)


class Random(Strategy):
    def selection(self,lista = None) -> str:
        self.newList  = []

        options = [Crescente, Decrescente]
        algoritmo =  random.choice(options)

        for i in lista:
            self.newList.append(i)

        if(algoritmo == Crescente):
            self.newList.sort()

        elif(algoritmo == Decrescente):
            self.newList.sort(reverse=1)


        return self.newList


class Ordenador:
    strategy: Strategy
    """
    The Context defines the interface of interest to clients.
    """
    def __init__(self,strategy: Strategy = None) -> None:
        if strategy is not None:
                self.strategy = strategy
        else:
            self.strategy = Random()
    
    def ordenar(self,lista = None) -> None:
        listaOrdenada = self.strategy.selection(self,lista)
        return listaOrdenada
