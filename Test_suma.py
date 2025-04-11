import unittest
from suma import Suma  # Asegúrate de tener la clase Suma en el archivo suma.py

class TestSuma(unittest.TestCase):
    def test_suma_dosNumeros_retornaSuma(self):
        # Arrange
        operando1 = 10
        operando2 = 15
        resultadoEsperado = 25
        objSuma = Suma(operando1, operando2)

        # Act
        resultadoActual = objSuma.calcularSuma()

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual, "Falló la suma")

    def test_suma_operadorNoNumerico_lanzaException(self):
        # Arrange
        objSuma = Suma(3, "a")

        # Assert + Act
        with self.assertRaises(ValueError):
            objSuma.calcularSuma()

if __name__ == '__main__':
    unittest.main()
