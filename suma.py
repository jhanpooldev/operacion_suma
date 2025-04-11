# suma.py

class Suma:
    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2

    def calcularSuma(self):
        if not isinstance(self.operando1, (int, float)) or not isinstance(self.operando2, (int, float)):
            raise ValueError("Los operandos deben ser números (int o float).")
        return self.operando1 + self.operando2
