class Calculadora:
    def __init__(self):
        pass

    def sumar(self, a, b):
        try:
            resultado = a + b
        except:
            resultado = 'solo se permiten números'
        return resultado
