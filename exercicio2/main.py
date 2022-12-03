from contador import ContadorPalavras, ContadorPalavrasCaracteresPares, ContadorPalavrasComecamMaiuscula
from frase import Orquestrador

fraseAleatoria = 'Ola tudo bem com voce Garoto'


manipulador1 = Orquestrador()
obs1 = ContadorPalavras(frase=fraseAleatoria)
obs2 = ContadorPalavrasCaracteresPares(fraseAleatoria)
obs3 = ContadorPalavrasComecamMaiuscula(fraseAleatoria)
manipulador1.addFunc(obs1)
manipulador1.addFunc(obs2)
manipulador1.addFunc(obs3)
manipulador1.order()