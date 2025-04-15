suma_total = 0
const = 3
rut = 0

for i in range(8):
    rut = int(input("Ingrese su rut")) 
    suma_total += rut * const
    if const > 2:
        const -= 1
    else:
        const = 7
    

numero_verificador = suma_total % 1
if numero_verificador == 0:
    print(numero_verificador)
elif numero_verificador == 10:
    print("K")
else:
    numero_verificador = 11 - numero_verificador
    print(numero_verificador)