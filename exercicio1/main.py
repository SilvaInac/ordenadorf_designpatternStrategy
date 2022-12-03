from ordenador import *


listaDesordenada = [5,1,3,2,4,7,8,9,6]

listaOrdenadaA = Ordenador(Crescente)
listaOrdenadaB = Ordenador(Decrescente)
listaOrdenadaC = Ordenador()

listaA = listaOrdenadaA.ordenar(listaDesordenada)
print("Crescente:",listaA)
listaB = listaOrdenadaB.ordenar(listaDesordenada)
print("Decrescente:",listaB)
listaC = listaOrdenadaC.ordenar(listaDesordenada)
print("Ordem Randomica:",listaC)
