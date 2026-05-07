from unittest import TestCase
import unittest
from calculadora import Calculadora


class TestCalculadora(TestCase):
    def test_sumar_dos_mas_dos(self):
        calc = Calculadora()
        resultado = calc.sumar(2, 2)
        self.assertEqual(resultado, 4)

    def test_subtracao(self):
        self.assertEqual(5 - 2, 3)

    def test_multiplicacao(self):
        self.assertEqual(4 * 3, 12)

    def test_divisao(self):
        self.assertEqual(10 / 2, 5)


if __name__ == '__main__':
    unittest.main()
