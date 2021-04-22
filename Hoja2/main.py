print("----EJERCICIO NO.1------")
i = int(input("Ingrese un número entero: "))

j=0

a= ''
b='*'
while j<i:
    a+=b   
    print(a)
    j+=1

print("----EJERCICIO NO.2------")

primo=True

i = int(input("Ingrese un número entero: "))
if i<2:
    print("El numero :",i," no es primo")
else:
    for j in range(2,i):
        if i%j==0:
            primo = False
            break
    if primo:
        print("El numero :",i," es primo") 
    else:
        print("El numero :",i," no es primo") 