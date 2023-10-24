# Tasa de cambio de dólares a pesos colombianos
tasa_de_cambio = 3800  # Puedes ajustar este valor según la tasa actual

# Inicializar la variable para el total de la venta en dólares
total_dolares = 0

# Solicitar al usuario los precios de las camisas en dólares
num_camisas = int(input("Ingrese la cantidad de camisas: "))

for i in range(num_camisas):
    precio_camisa_dolares = float(input(f"Ingrese el precio de la camisa {i + 1} en dólares: $"))                 
    total_dolares += precio_camisa_dolares

# Calcular el total en pesos colombianos
total_pesos_colombianos = total_dolares * tasa_de_cambio

# Mostrar el total de la venta en dólares y pesos colombianos
print(f"El total de la venta en dólares es: ${total_dolares:.2f}")
print(f"El total de la venta en pesos colombianos es: ${total_pesos_colombianos:,.2f}")