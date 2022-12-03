import unittest
from contador import ContadorPalavras, ContadorPalavrasCaracteresPares, ContadorPalavrasComecamMaiuscula
from frase import *

class Testing(unittest.TestCase):
    def test_countAll(self):
        fraseAleatoria = 'Ola tudo bem'
        obs1 = ContadorPalavras(frase=fraseAleatoria).update()
        self.assertEqual(obs1, 3)

    def test_countPar(self):
        fraseAleatoria = 'Ola tudo bem'
        obs1 = ContadorPalavrasCaracteresPares(frase=fraseAleatoria).update()
        self.assertEqual(obs1, 1)
    def test_countPar(self):
        fraseAleatoria = 'Ola tudo bem'

        obs1 = ContadorPalavrasComecamMaiuscula(frase=fraseAleatoria).update()
        self.assertEqual(obs1, 1)

if __name__ == '__main__':
    unittest.main()