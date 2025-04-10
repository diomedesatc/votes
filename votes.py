input("Vamos a sacar los angulos: ")
a = int(input("El angulo de A: "))
b = int(input("El angulo de B: "))
c = int(input("El angulo de C: "))

if a + b + c == 180:
    if (a == b) or (b == c) or (a == c):
        print("El triangulo es ISOSELES")
    else:
        print("El triangulo no es ISOSELES")

else:
    print("Los valores ingresados no son validos.")
