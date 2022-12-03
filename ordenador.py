from abc import ABC, abstractclassmethod
import random

#Strategy interface
class Strategy(ABC):

    @abstractclassmethod

    def selection(self) -> None:
        pass
    
class Crescente(Strategy):
    def selection(self,lista) -> str:
        self.newList  = []
        for i in lista:
            self.newList.append(i)

        self.newList.sort()
        return (self.newList)

class Decrescente(Strategy):
    def selection(self,lista) -> str:
        self.newList  = []
        for i in lista:
            self.newList.append(i)

        self.newList.sort(reverse=1)
        return (self.newList)


class Random(Strategy):
    def __init__(self,lista: list) -> None:
        if lista is not None:
                self.listData = lista

    def selection(self) -> str:
        options = [Crescente, Decrescente]
        algoritmo =  random.choice(options)

        if(algoritmo == Crescente):
            return self.listData.sort()


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
    
    def ordenar(self,lista) -> None:
        listaOrdenada = self.strategy.selection(self,lista)
        return listaOrdenada


listaDesordenada = [5,1,3,2,4,7,8,9,6]

listaOrdenadaA = Ordenador(Crescente)
listaOrdenadaB = Ordenador(Decrescente)
listaOrdenadaC = Ordenador(Random)

listaA = listaOrdenadaA.ordenar(listaDesordenada)
print("Crescente:",listaA)
listaB = listaOrdenadaB.ordenar(listaDesordenada)
print("Decrescente:",listaB)
listaC = listaOrdenadaB.ordenar(listaDesordenada)
print("Ordem Randomica:",listaC)
