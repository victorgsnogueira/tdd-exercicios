import unittest

from src.triangulo import Triangulo


class TestTriangulo(unittest.TestCase):

    def test_escaleno_valido(self):
        self.assertEqual(Triangulo(3, 4, 5).classificar(), "escaleno")

    def test_isosceles_valido(self):
        self.assertEqual(Triangulo(3, 3, 5).classificar(), "isosceles")

    def test_equilatero_valido(self):
        self.assertEqual(Triangulo(3, 3, 3).classificar(), "equilatero")

    def test_isosceles_permutacao_1(self):
        self.assertEqual(Triangulo(3, 3, 5).classificar(), "isosceles")

    def test_isosceles_permutacao_2(self):
        self.assertEqual(Triangulo(3, 5, 3).classificar(), "isosceles")

    def test_isosceles_permutacao_3(self):
        self.assertEqual(Triangulo(5, 3, 3).classificar(), "isosceles")

    def test_um_lado_zero(self):
        with self.assertRaises(ValueError):
            Triangulo(0, 4, 5).classificar()

    def test_um_lado_negativo(self):
        with self.assertRaises(ValueError):
            Triangulo(-3, 4, 5).classificar()

    def test_soma_igual_permutacao_1(self):
        with self.assertRaises(ValueError):
            Triangulo(1, 2, 3).classificar()

    def test_soma_igual_permutacao_2(self):
        with self.assertRaises(ValueError):
            Triangulo(1, 3, 2).classificar()

    def test_soma_igual_permutacao_3(self):
        with self.assertRaises(ValueError):
            Triangulo(3, 1, 2).classificar()

    def test_soma_menor_permutacao_1(self):
        with self.assertRaises(ValueError):
            Triangulo(1, 2, 5).classificar()

    def test_soma_menor_permutacao_2(self):
        with self.assertRaises(ValueError):
            Triangulo(1, 5, 2).classificar()

    def test_soma_menor_permutacao_3(self):
        with self.assertRaises(ValueError):
            Triangulo(5, 1, 2).classificar()

    def test_tres_lados_zero(self):
        with self.assertRaises(ValueError):
            Triangulo(0, 0, 0).classificar()


if __name__ == "__main__":
    unittest.main()
