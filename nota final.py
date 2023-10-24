
# Solicitar al estudiante ingresar las calificaciones de los dos talleres y el quiz
taller1 = float(input("Ingrese la calificación del primer taller (0-5 puntos): "))
taller2 = float(input("Ingrese la calificación del segundo taller (0-5 puntos): "))
quiz = float(input("Ingrese la calificación del quiz (0-5 puntos): "))

# Verificar que las calificaciones estén dentro del rango permitido
if 0 <= taller1 <= 5 and 0 <= taller2 <= 5 and 0 <= quiz <= 5:
    # Calcular la nota del 30% correspondiente a los talleres y el quiz
    nota_talleres_quiz = (taller1 + taller2 + quiz) / 3

    # Solicitar al estudiante ingresar la calificación del examen parcial
    examen_parcial = float(input("Ingrese la calificación del examen parcial (0-5 puntos): "))

    # Verificar que la calificación del examen parcial esté dentro del rango permitido
    if 0 <= examen_parcial <= 5:
        # Calcular la nota final del 70% correspondiente al examen parcial
        nota_examen_parcial = examen_parcial

        # Calcular la nota final del semestre considerando el peso de los componentes
        nota_final = (0.3 * nota_talleres_quiz) + (0.7 * nota_examen_parcial)

        # Mostrar la nota final al estudiante
        print(f"La nota final del semestre es: {nota_final:.2f}")
    else:
        print("La calificación del examen parcial debe estar en el rango de 0 a 5 puntos.")
else:
    print("Las calificaciones de los talleres y el quiz deben estar en el rango de 0 a 5 puntos.")

