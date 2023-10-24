numero = int(input("ingrese numero entre 1 y 10;"))
#verificar si el numero esta dentro del valor permitido 
if numero < 1 or numero > 10: 
    print("El numero ingresado no esta dentro del rango permitivo")
else:
    #Recorre los numeros del 10 al 1
    for i in range(1,11):
     resultado = i * numero
     print(f"{i} x {numero} = {resultado}")
 