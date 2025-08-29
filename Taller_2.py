#Programa que define si es bisiesto  

#Entredas 
#Variable Entrada
#año

#Variable Salida
#año

#define si el año ingresado es bisiesto 

año = int(input("Ingresa un año: "))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"El año {año} es bisiesto")
else:
    print(f"El año {año} NO es bisiesto")
