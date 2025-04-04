segundos = 0
minutos = 0
horas = 0

while horas < 24:
    while minutos < 60:
        while segundos < 59:            
            segundos += 1
            print(f'{horas}: {minutos} : {segundos}')
        minutos += 1 
        segundos = 0

    horas += 1 
    minutos = 0

