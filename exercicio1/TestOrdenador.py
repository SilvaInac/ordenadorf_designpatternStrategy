import unittest
from ordenador import Ordenador,Crescente,Decrescente,Random

class Testing(unittest.TestCase):
    def test_crescente(self):

        listaOrdenadaA = Ordenador(Crescente)
        listaA = listaOrdenadaA.ordenar([2,3,5,1,4,7,6])

        self.assertEqual(listaA, [1,2,3,4,5,6,7])

    def test_decrescente(self):
        listaOrdenadaA = Ordenador(Decrescente)
        listaA = listaOrdenadaA.ordenar([2,3,5,1,4,7,6])

        self.assertEqual(listaA, [7,6,5,4,3,2,1])


    def test_None(self):
        listaOrdenadaA = Ordenador(Crescente)
        listaA = listaOrdenadaA.ordenar([])

        self.assertIsNotNone(listaA)


if __name__ == '__main__':
    unittest.main()