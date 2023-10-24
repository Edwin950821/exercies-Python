def prod_digitos_suma(n):
    # Inicializamos las variables s para la suma y p para el producto.
    s = 0
    p = 1

    # Calculamos la suma de los números del 1 a n.
    for i in range(1, n + 1):
        s += i

    # Convertimos la suma en una cadena para procesar los dígitos.
    s_str = str(s)

    # Calculamos el producto de los dígitos distintos de cero.
    for numero in s_str:
        if numero != "0":
            p *= int(numero)

    print("La suma de 1 hasta", n, "es", s)
    print("El producto de sus dígitos distintos de 0 es", p)

# Ejemplo de uso de la función con n = 5
prod_digitos_suma(5)
