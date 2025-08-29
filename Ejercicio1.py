#Programa que da el nombre y las iniciales en mayusculas 

#Entredas 
#Variable Entrada
#Variable Salida

#Pedir Mombre y Apellido 

nombre = input("ingrese su nombre: ")
apellido= input("ingrese su apellido: ")

#Tomar la primera letra de cada uno, mostrarla en mayusculas

iniciales= nombre[0].upper() + apellido[0].upper()

#Mostrar resultados

print("tus iniciales son", iniciales)
print("tus nombres completos son", nombre.upper(),apellido.upper())
       