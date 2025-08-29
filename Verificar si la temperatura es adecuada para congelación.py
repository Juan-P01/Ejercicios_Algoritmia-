#Programa: que da la temperatura 

#Entredas 
#Variable Entrada
#temperatura

#Variable Salida
#temperatura,congelacion

#define si el triandulo es equilatero, isosceles o escaleno

def congelacion():
    temperatura = float(input("Ingrese la temperatura: "))
    if temperatura <= 0:
        print("La temperatura es adecuada para congelación")
    else:
        print("No es adecuada para congelación")
congelacion ()