#Informacion personal
#Direccion

print("Tupla numero 1")
nombre = input("Escriba su nombre: ")
edad = input("Escriba su edad: ")
altura = input("Ingrese su altura: ")
direccion = input("Ingrese su direccion: ")
ciudad = input("Ingrese la ciudad donde vive: ")
religion = input("Ingrese su religion, si no tiene ingrese NO: ")

informacion = tuple((nombre, edad, altura, direccion, ciudad, religion))
print(informacion[0::1])