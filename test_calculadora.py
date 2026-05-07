from unittest import TestCase
import unittest
from calculadora import Calculadora


class TestCalculadora(TestCase):
    def test_sumar_dos_mas_dos(self):
        calc = Calculadora()
        resultado = calc.sumar(2, 2)
        self.assertEqual(resultado, 4)

    def test_ingresa_caracter(self):
        calc = Calculadora()
        resultado = calc.sumar('X', 2)
        self.assertEqual('solo se permiten números', resultado)


if __name__ == '__main__':
    unittest.main()
