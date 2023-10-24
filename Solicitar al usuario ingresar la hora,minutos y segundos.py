# Solicitar al usuario ingresar la hora, los minutos y los segundos
hora = int(input("Ingrese la hora (0-23): "))
minutos = int(input("Ingrese los minutos (0-59): "))
segundos = int(input("Ingrese los segundos (0-59): "))

# Verificar si los valores ingresados son válidos
if 0 <= hora <= 23 and 0 <= minutos <= 59 and 0 <= segundos <= 59:
    # Calcular el tiempo total en segundos
    tiempo_total_segundos = hora * 3600 + minutos * 60 + segundos

    # Calcular la hora siguiente en segundos
    hora_siguiente_segundos = tiempo_total_segundos + 1

    # Calcular la nueva hora, minutos y segundos
    nueva_hora = hora_siguiente_segundos // 3600
    nueva_minutos = (hora_siguiente_segundos % 3600) // 60
    nuevos_segundos = hora_siguiente_segundos % 60

    # Mostrar la hora siguiente
    print(f"La hora siguiente es: {nueva_hora:02d}:{nueva_minutos:02d}:{nuevos_segundos:02d}")
else:
    print("Por favor, ingrese valores de tiempo válidos.")
