#crea un codigo con python que cumpla con la siguiente consigna "Calcular el mayor de dos números ingresados por teclado usando un operador ternario"

numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))

mayor = numero1 if numero1 > numero2 else numero2

print(f"El número mayor es: {mayor}")


#Buscar una palabra en una lista ingresada por teclado usando args y un operador ternario

def buscar_palabra(palabra_buscar, *args):
  return palabra_buscar in args

if __name__ == "__main__":
  palabra = input("Ingresa la palabra que deseas buscar: ")
  entrada_lista = input("Ingresa las palabras de la lista separadas por espacios: ")
  lista_palabras = entrada_lista.split()

  encontrada = buscar_palabra(palabra, *lista_palabras)

  resultado = "La palabra SI se encuentra en la lista." if encontrada else "La palabra NO se encuentra en la lista."
  print(resultado)

#Determinar si un número es par o impar
def par_o_impar(*args, **kwargs):
    for num in args:
        resultado = "par" if num % 2 == 0 else "impar"
        print(f"El número {num} es {resultado}.")
  
    for clave, valor in kwargs.items():
        resultado = "par" if valor % 2 == 0 else "impar"
        print(f"{clave}: El número {valor} es {resultado}.")

par_o_impar(2, 3, 7, 10, numero_extra=5, otro_numero=8)


#Calcular el promedio de una lista de números usando args y un operador ternario
def calcular_promedio(*args, **kwargs):
    promedio = sum(args) / len(args) if args else "No se ingresaron números"
    return promedio

entrada = input("Ingresa una lista de números separados por espacios: ")

try:
    numeros = [float(num) for num in entrada.split()]
except ValueError:
    print("Por favor, ingresa solo números válidos.")
    exit()

resultado = calcular_promedio(*numeros)

print(f"El promedio es: {resultado}")

#Imprimir un mensaje de error si no se pasan suficientes argumentos
def verificar_argumentos(*args, **kwargs):
    print("Verificando argumentos...")
    mensaje = (
        "Error: No se pasaron suficientes argumentos."
        if len(args) < 2
        else f"Argumentos válidos: {args}"
    )
    print(mensaje)

verificar_argumentos(5)    
verificar_argumentos(5, 10) 
verificar_argumentos(1, 2, 3)