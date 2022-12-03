from observador import Observador


class ContadorPalavras(Observador):
    
    def __init__(self, frase : str):
        self.frase = frase

    def update(self):
        res = len(self.frase.split())
        print ("The number of words in string are : " +  str(res)) 
        return res


class ContadorPalavrasCaracteresPares(Observador):
    
    def __init__(self, frase : str):
        self.frase = frase

    def update(self):
        res = len(self.frase.split())
        print ("The number of words in string are : " +  str(res)) 
        return res