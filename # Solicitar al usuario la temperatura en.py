# Solicitar al usuario la temperatura en grados Celsius
temperatura_celsius = float(input("Ingrese la temperatura en grados Celsius: "))

# Aplicar la fórmula para convertir a grados Fahrenheit
temperatura_fahrenheit = (9/5) * temperatura_celsius + 32

# Mostrar el resultado
print(f"{temperatura_celsius} grados Celsius equivalen a {temperatura_fahrenheit} grados Fahrenheit.")
