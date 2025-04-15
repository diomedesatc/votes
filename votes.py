inicio = int(input("Ingrese el numero de inicio: "))
final = int(input("Ingrese el numero final: "))

if inicio < final:
    num = inicio + 1
    for i in range(final - 2):
        print(num)
        num += 1
elif inicio == final:
    print("El inicio y el final son iguales :) ")
else:
    num = inicio - 1
    for i in range(inicio - 2):
        print(num)
        num -= 1
