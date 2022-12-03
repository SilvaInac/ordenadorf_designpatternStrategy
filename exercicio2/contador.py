from observador import Observador


class ContadorPalavras(Observador):
    
    def __init__(self, frase : str):
        self.frase = frase

    def update(self):
        res = len(self.frase.split())
        print ("Numero total de palavras : " +  str(res)) 
        return int(res)

class ContadorPalavrasCaracteresPares(Observador):
    
    def __init__(self, frase : str):
        self.frase = frase

    def update(self):
        count = 0
        listaPalavras = self.frase.split()
        for palavra in listaPalavras:
            if(len(palavra)%2 ==0):
                count = count+1
        print ("Numero de palavras que começam com letra maiuscula: " + str(count)) 
        return count

class ContadorPalavrasComecamMaiuscula(Observador):
    def __init__(self, frase : str):
        self.frase = frase

    def update(self):
        count = 0
        listaPalavras = self.frase.split()
        for palavra in listaPalavras:
            if(palavra[0].isupper() ==True):
                count = count+1
        print ("Numero de palavras com quantidades pares de caracteres: " + str(count)) 
        return count