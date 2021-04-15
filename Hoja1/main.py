print("------BIENVENIDO------")
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en mt: "))

imc = round((peso)/altura**2, 2)

print("Su indice de de masa corporal es" ,imc)