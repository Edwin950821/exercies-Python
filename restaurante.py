# Inicializamos una variable para el total de los pagos
total_pagos = 0

# Loop para registrar el consumo de 5 clientes
for i in range(1, 6):
    print(f"Registro del cliente {i}:")
    consumo = float(input("Ingrese el monto de consumo del cliente: $"))
    
    # Aplicar descuento del 20% si el consumo es mayor a $50,000
    if consumo > 50000:
        descuento = consumo * 0.20
    else:
        descuento = 0

    # Calcular el monto a pagar por el cliente
    monto_a_pagar = consumo - descuento

    # Mostrar el monto a pagar del cliente
    print(f"El cliente {i} debe pagar: ${monto_a_pagar:.2f}\n")

    # Actualizar el total de los pagos
    total_pagos += monto_a_pagar

# Mostrar el total de los pagos de todos los clientes
print(f"El total de los pagos de los 5 clientes es: ${total_pagos:.2f}")
