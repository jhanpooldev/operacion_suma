# 🧮 Aplicación: Operación Suma

## 📄 Descripción

Este script en Python realiza la **suma de dos números**, validando previamente que los operandos ingresados sean valores numéricos (`int` o `float`). Es una aplicación sencilla, útil para practicar validaciones básicas y estructuras condicionales en Python.

---

## ✅ Funcionalidades

- 🔢 Realiza la suma de dos operandos.
- ✔️ Verifica que los operandos ingresados sean valores numéricos (`int` o `float`).
- ⚠️ Muestra mensajes de error si los datos ingresados no son válidos.
- 🧪 Fácil de extender a más operaciones aritméticas si se desea.

---

## 🛠️ Requisitos

- Python 3.6 o superior instalado en tu sistema.
- Editor de código (VSCode, PyCharm, Sublime Text, etc.) – opcional.
- Terminal o consola para ejecutar el script.

---

       [Repositorio Git hub]
       (https://github.com/jhanpooldev/operacion_suma/edit/main/README.md)
  ![Logo de python ](https://cdn.computerhoy.com/sites/navi.axelspringer.es/public/media/image/2023/04/raspberry-lanza-editor-codigo-aprender-python-lenguaje-ia-3008158.jpg?tf=3840x)


### Equipo de desarrollo 
| Apellidos y nombres | ROL |
|-------------------- | --- |
|Flores Torres Jhanpool | Lider |
|Inciso Aguilar Elizabeth | Colaboradora |

## 🚀 ¿Cómo ejecutar el script?

1. Clona este repositorio o descarga el archivo `suma_valida.py`.
2. Abre una terminal en la ubicación del archivo.
3. Ejecuta el siguiente comando:

```bash
python suma_valida.py

Ingrese el primer número: 12
Ingrese el segundo número: 8.5
Resultado: 20.5
Ingrese el primer número: hola
Error: Entrada inválida. Por favor, ingrese un número válido.
## 🧪 Código fuente (suma_valida.py)
def es_numero(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

def suma_numeros(a, b):
    return float(a) + float(b)

if __name__ == "__main__":
    a = input("Ingrese el primer número: ")
    b = input("Ingrese el segundo número: ")

    if es_numero(a) and es_numero(b):
        resultado = suma_numeros(a, b)
        print(f"Resultado: {resultado}")
    else:
        print("Error: Entrada inválida. Por favor, ingrese un número válido.")

---

¿Quieres que te genere también el archivo `LICENSE`, el `.gitignore` o incluso una versión del script que acepte argumentos desde la línea de comandos?

