import unittest

from src.funcionario import Funcionario
from src.calculadora_salario import CalculadoraSalario


class TestCalculadoraSalario(unittest.TestCase):

    def setUp(self):
        self.calculadora = CalculadoraSalario()

    def calcular(self, salario, cargo):
        funcionario = Funcionario("Joao", "joao@gmail.com", salario, cargo)
        return self.calculadora.calcular(funcionario)

    def test_desenvolvedor_salario_acima_de_3000(self):
        self.assertAlmostEqual(self.calcular(4000.00, "DESENVOLVEDOR"), 3200.00)

    def test_desenvolvedor_salario_igual_a_3000(self):
        self.assertAlmostEqual(self.calcular(3000.00, "DESENVOLVEDOR"), 2400.00)

    def test_desenvolvedor_salario_abaixo_de_3000(self):
        self.assertAlmostEqual(self.calcular(2000.00, "DESENVOLVEDOR"), 1800.00)

    def test_dba_salario_acima_de_2000(self):
        self.assertAlmostEqual(self.calcular(3000.00, "DBA"), 2250.00)

    def test_dba_salario_igual_a_2000(self):
        self.assertAlmostEqual(self.calcular(2000.00, "DBA"), 1500.00)

    def test_dba_salario_abaixo_de_2000(self):
        self.assertAlmostEqual(self.calcular(1000.00, "DBA"), 850.00)

    def test_testador_salario_acima_de_2000(self):
        self.assertAlmostEqual(self.calcular(3000.00, "TESTADOR"), 2250.00)

    def test_testador_salario_igual_a_2000(self):
        self.assertAlmostEqual(self.calcular(2000.00, "TESTADOR"), 1500.00)

    def test_testador_salario_abaixo_de_2000(self):
        self.assertAlmostEqual(self.calcular(1000.00, "TESTADOR"), 850.00)

    def test_gerente_salario_acima_de_5000(self):
        self.assertAlmostEqual(self.calcular(6000.00, "GERENTE"), 4200.00)

    def test_gerente_salario_igual_a_5000(self):
        self.assertAlmostEqual(self.calcular(5000.00, "GERENTE"), 3500.00)

    def test_gerente_salario_abaixo_de_5000(self):
        self.assertAlmostEqual(self.calcular(4000.00, "GERENTE"), 3200.00)


if __name__ == "__main__":
    unittest.main()
