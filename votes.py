def verificarSiElRutEsCorrecto(rut):
    #Funcion para verificar si el rut ingresado es valido
    es_correcto = [False, 1, 1]
    rut_sin_codigo = ''
    verificador = ''
    try:
        #Captura la excepcion de buscar el guion en el ingreso del rut
        rut_separado = rut.split("-")
        rut_sin_codigo = rut_separado[0]
        verificador = rut_separado[1]

        #Captura la excepcion de si el usuario ingresa valores alfanumericos
        
        nuevo_rut_separado = int(rut_sin_codigo)
        es_correcto[1] = str(nuevo_rut_separado)
        es_correcto[2] = int(verificador)
        
    except:
        return es_correcto
    
    
    #Verifica si la longitud del rut es correcta 
    if not (len(rut_sin_codigo) <= 8 and len(rut_sin_codigo) >= 7) or (len(verificador) != 1):
        return es_correcto
    else:
        es_correcto[0] = True

    return es_correcto

def obtenerNumeroVerificador(rut_sin_numero_verficador):
    suma_total = 0
    const = [3,2,7,6,5,4,3,2,7,6,5,4,3,2]
    for i in range(len(rut_sin_numero_verficador)):
        suma_total += int(rut_sin_numero_verficador[i]) * const[i]


    numero_verificador = suma_total % 11    
    numero_verificador = 11 - numero_verificador

    if numero_verificador == 11:
        return 0
    elif numero_verificador == 10:
        return 'K'
    else:
        return numero_verificador

print("Verificador de rut")
rut = input("Ingrese su rut: ")
procesando = verificarSiElRutEsCorrecto(rut)
intentos = 0

while not procesando[0]:
    print("El rut ingreso no es valido")
    rut = input("Ingrese su rut: ")
    procesando = verificarSiElRutEsCorrecto(rut)
    intentos += 1
    if intentos > 2:
        print("Recuerda que el formato del rut es de 8 a 9 digitos separados por guion y el numero verificador.")

print("El rut ingresado es valido!!")





