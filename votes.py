inicio = int(input("Ingrese el numero de inicio: "))
final = int(input("Ingrese el numero final: "))

if inicio < final:
    num = inicio
    for i in range(final):
        print(num)
        num += 1
else:
    num = inicio
    for i in range(inicio):
        print(num)
        num -= 1
