#1) Escribe un programa que intente dividir dos números. Si el segundo número es cero,captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario.

def dividir_numeros():
    try:
        numerador = float(input("Introduce el numerador: "))
        denominador = float(input("Introduce el denominador: "))
        resultado = numerador / denominador
        print(f"El resultado de la división es: {resultado}")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
    except ValueError:
        print("Error: Debes introducir un número válido.")

dividir_numeros()


#2) Escribe un programa que intente sumar un número y una cadena. Si se produce un error de tipo, captura la excepción TypeError y muestra un mensaje de error al usuario.

def sumar_numero_y_cadena():
    numero = 10
    cadena = "texto"
    
    try:
        resultado = numero + cadena
        print(f"El resultado es: {resultado}")
    except TypeError:
        print("Error: No se puede sumar un número y una cadena (TypeError).")

sumar_numero_y_cadena()


#3) Escribe un programa que intente acceder a una clave que no existe en un diccionario. Si se produce una excepción KeyError, captura la excepción y muestra

mi_diccionario = {
    'nombre': 'Juan',
    'edad': 30,
    'ciudad': 'CABA'
}

clave_a_buscar = 'pais'

try:
    valor = mi_diccionario[clave_a_buscar]
    print(f"El valor de '{clave_a_buscar}' es: {valor}")
except KeyError:
    print(f"La clave '{clave_a_buscar}' no existe en el diccionario.")


#4) Escribe un programa que intente abrir un archivo que no existe. Si se produce una excepciónFileNotFoundError, captura la excepción y muestra un mensaje de error al usuario. Sin embargo, también intenta crear el archivo si no existe

try:
    archivo = open("archivo_inexistente.txt", "r")
    contenido = archivo.read()
    archivo.close()
except FileNotFoundError:
    print("Error: El archivo no existe.")
    print("Creando el archivo...")
    archivo = open("archivo_inexistente.txt", "w")
    archivo.write("Este es un archivo recién creado.\n")
    archivo.close()
    print("El archivo ha sido creado exitosamente.")


#5) Escribe un programa que intente dividir dos números. Si el segundo número es cero, captura la excepción ZeroDivisionError. Si el primer número es un número no válido, captura la excepción ValueError. En cualquier caso, muestra un mensaje de error al usuario.
def dividir_numeros():
    try:
        num1_str = input("Ingrese el primer número: ")
        num1 = float(num1_str)
        num2_str = input("Ingrese el segundo número: ")
        num2 = float(num2_str)
        resultado = num1 / num2
        print(f"El resultado de {num1} dividido por {num2} es: {resultado}")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    except ValueError:
        print("Error: Uno de los valores ingresados no es un número válido.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

dividir_numeros()