print("Es tiempo de elegir a tu candidato")

personas_a_votar = 5
cristian = 0
julio = 0
isabel = 0

while personas_a_votar > 0:
    print("Estos son tu candidatos: ")
    print("1. Cristian")
    print("2. Julio")
    print("3. Isabel")
    print("Ingresa el numero del candidato: ")

    voto = int(input())

    if voto == 1:
        cristian += 1
        personas_a_votar -= 1
    elif voto == 2:
        julio += 1
        personas_a_votar -= 1
    elif voto == 3:
        isabel += 1
        personas_a_votar -= 1
    else:
        print("Ingresa un numero valido nuevamente")


print("Y los resultados son:")
print("Cristian total de votos: ", cristian)
print("Julio total de votos: ", julio)
print("Isabel total de votos: ", isabel)

if cristian > julio and cristian > isabel:
    print("El ganador es: Cristian") 

elif julio > cristian and julio > isabel:
    print("El ganador es: Julio")
elif isabel > julio and isabel > cristian:
    print("EL ganador es: Isabel")