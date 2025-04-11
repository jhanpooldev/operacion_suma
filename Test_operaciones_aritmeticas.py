import unittest
from operaciones_aritmeticas import OperacionesAritmeticas


class TestOperacionesAritmeticas(unittest.TestCase):

    def test_suma_dosNumeros_retornaSuma(self):
        operando1 = 10
        operando2 = 15
        resultadoEsperado = 25
        obj = OperacionesAritmeticas(operando1, operando2)
        resultadoActual = obj.calcularSuma()
        self.assertEqual(resultadoEsperado, resultadoActual, msg="Falló la suma")

    def test_division_dosNumeros_retornaDivision(self):
        dividendo = 10
        divisor = 15
        resultadoEsperado = 0.666
        obj = OperacionesAritmeticas(dividendo, divisor)
        resultadoActual = obj.calcularDivision()
        self.assertAlmostEqual(resultadoEsperado, resultadoActual, places=2, msg="Falló la división")

    def test_division_operadorNoNumerico_lanzaExcepcion(self):
        obj = OperacionesAritmeticas(3, "A")
        with self.assertRaises(TypeError):
            obj.calcularDivision()

    def test_suma_operadorNoNumerico_lanzaExcepcion(self):
        obj = OperacionesAritmeticas(3, "A")
        with self.assertRaises(TypeError):
            obj.calcularSuma()

    def test_division_porCero_lanzaExcepcion(self):
        obj = OperacionesAritmeticas(10, 0)
        with self.assertRaises(ZeroDivisionError):
            obj.calcularDivision()


if __name__ == '__main__':
    unittest.main()
