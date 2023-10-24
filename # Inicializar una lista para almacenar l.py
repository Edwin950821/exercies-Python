 # Inicializar una lista para almacenar los números menores o iguales a 25
numeros_menores_25 = []

# Solicitar al usuario ingresar 20 números
for i in range(20):
    numero = float(input(f"Ingrese el número {i + 1}: "))
    
    # Comprobar si el número es menor o igual a 25 y agregarlo a la lista
    if numero <= 25:
        numeros_menores_25.append(numero)

# Mostrar los números menores o iguales a 25
print("Números menores o iguales a 25:")
for numero in numeros_menores_25:
    print(numero)
