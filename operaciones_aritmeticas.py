class OperacionesAritmeticas:
    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2

    def validar_operandos(self):
        if not isinstance(self.operando1, (int, float)) or not isinstance(self.operando2, (int, float)):
            raise TypeError("Los operandos deben ser int o float.")

    def calcularSuma(self):
        self.validar_operandos()
        return self.operando1 + self.operando2

    def calcularDivision(self):
        self.validar_operandos()
        if self.operando2 == 0:
            raise ZeroDivisionError("No se puede dividir entre cero.")
        return self.operando1 / self.operando2

