from contador import ContadorPalavras
from frase import Orquestrador

fraseAleatoria = 'Ola tudo bem com voce'


manipulador1 = Orquestrador()
obs1 = ContadorPalavras(frase=fraseAleatoria)
manipulador1.addFunc(obs1)
manipulador1.order()