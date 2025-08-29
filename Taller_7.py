#Programa que define que tipo de figura es el triangulo

#Entredas 
#Variable Entrada
#num1,num2,num3

#Variable Salida
#num1,num2,num3

#define si el triandulo es equilatero, isosceles o escaleno

num1 = int(input("Ingrese su primer número: "))
num2 = int(input("Ingrese su segundo número: "))
num3 = int(input("Ingrese su tercer número: "))

if num1 == num2 == num3:
    print("Su triángulo es EQUILÁTERO")
elif num1 == num2 or num1 == num3 or num2 == num3:
    print("Su triángulo es ISÓSCELES")
else:
    print("Su triángulo es ESCALENO")
