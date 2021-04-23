print("----EJERCICIO NO.1------")
pass_1 = str(input("Ingrese la contraseña: "))
print("-------------------------")
pass_2 = str(input("Confirme la contraseña: "))

if pass_1.lower() == pass_2.lower():
    print("\n¡Contraseña correcta!")
else:
    print("\n¡Las contraseñas no coinciden!")

print("\n>>>FIN DEL EJERCICIO 1<<<")

'''
Inicio del ejercicio 2

'''

print("\n------EJERCICIO NO.2------")
initial = "ABCDEFGHIJKLM"
name = str(input("Ingrese su nombre: "))
genero = str(input("Ingrese su sexo (M ó F): "))

clase = False
for i in initial:
    if name[0].upper() == i:
        if genero.lower() == 'f':
            clase = True

for i in 'NOPQRSTUVWXYZ':
    if name[0].upper() == i:
        if genero.lower() == 'm':
            clase = True

if clase:
    print("\n___________________________")
    print(name," Estas en la clase A")
else:
    print("\n___________________________")
    print(name," Estas en la clase B")

print("Fin del programa")