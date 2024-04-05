from os import system
from time import sleep


#### Funcion verificadora de numero binario
def verificar_binario (numBinario):
    es_binario = True
    largo = True
    numBin = False
    if len(numBinario) > 16:
        largo = False

    if largo == True:
        for digit in numBinario:
            if digit not in ('0', '1'):
                es_binario = False

    if largo == False:
        mensaje = "El número ingresado no cumple los 16 bits maximos."
    elif es_binario == False:
        mensaje = "El número ingresado no es binario"
    elif largo == True and largo == True:
        mensaje = "El número ingresado es binario y cumple los 16 bits de largo."
        numBin = True
    
    return mensaje,numBin


#### Funcion para convertir en decimal
def convertir_decimal(numBinario):
    numBinario = numBinario[::-1]
    acum = 0
    cont = 1
    cont1 = 1
    for i in numBinario:
        if i == "0":
            acum += cont *0
            cont = cont * 2
            cont1 += 1
        elif i == "1":
            acum += cont
            cont = cont * 2
            cont1 += 1
    return acum


#### Funcion para convertir binario a octal
def convertir_octal (numBinario):
    numBinario = numBinario[::-1]

    # Inicializamos una lista para almacenar los conjuntos de tres caracteres
    conjuntos = []

    # Iteramos sobre el numero binario (numBinario) tomando grupos de tres caracteres
    for i in range(0, len(numBinario), 3):
        conjunto = numBinario[i:i+3]  # Tomamos un conjunto de tres caracteres
        conjuntos.append(conjunto)  # Agregamos el conjunto a la lista

    # Aca convertimos a decimal y en cada iteracion de la lista conjuntos convertimos a decimal y lo agregamos a una nueva lista

    decimal = []

    for num in conjuntos:
        acum = 0
        cont = 1
        cont1 = 1
        for i in num:
            if i == "0":
                acum += cont *0
                cont = cont * 2
                cont1 += 1
            elif i == "1":
                acum += cont
                cont = cont * 2
                cont1 += 1

        decimal.append(acum)

    # Invertir la lista
    lista_invertida = list(reversed(decimal))

    # Concatenar las cadenas
    cadena_concatenada = ''.join(str(x) for x in lista_invertida)

    return cadena_concatenada


#### FUNCION PARA CONVERTIR BINARIO A HEXADECIMAL
def convertir_hexa(numBinario):
    numBinario = numBinario[::-1]

    # Inicializamos una lista para almacenar los conjuntos de tres caracteres
    conjuntos = []

    # Iteramos sobre el numero binario (numBinario) tomando grupos de tres caracteres
    for i in range(0, len(numBinario), 4):
        conjunto = numBinario[i:i+4]  # Tomamos un conjunto de cuatro caracteres
        conjuntos.append(conjunto)  # Agregamos el conjunto a la lista

    # Aca convertimos a decimal y en cada iteracion de la lista conjuntos convertimos a decimal y lo agregamos a una nueva lista

    hexa = []

    for num in conjuntos:
        acum = 0
        cont = 1
        cont1 = 1
        for i in num:
            if i == "0":
                acum += cont *0
                cont = cont * 2
                cont1 += 1
            elif i == "1":
                acum += cont
                cont = cont * 2
                cont1 += 1

        hexa.append(acum)
    numhexa = []
    # Invertir la lista
    lista_invertida = list(reversed(hexa))

    for i in lista_invertida:
        if i <= 9:
            numhexa.append(i)
        elif i == 10:
            numhexa.append("A")
        elif i == 11:
            numhexa.append("B")
        elif i == 12:
            numhexa.append("C")
        elif i == 13:
            numhexa.append("D")
        elif i == 14:
            numhexa.append("E")
        elif  i == 15:
            numhexa.append("F")

    # Concatenar las cadenas
    cadena_concatenada = ''.join(str(x) for x in numhexa)
  
    return cadena_concatenada


#### FUNCION PARA INGRESAR UN NUMERO BINARIO
def ingresar_binario():
    numBin = False
    while numBin == False:
        numBinario = str(input("\nIngrese el número binario a convertir: ")) 
        system ("cls")
        # Comprobar que el número es correcto. Si no lo es mostrar mensaje de error e intentarlo nuevamente.

        mensaje, numBin = verificar_binario (numBinario)
        print (f"\n{mensaje}\n")

    # Convertir Binario a Decimal

    numDecimal = convertir_decimal(numBinario)

    # Convertir Binario a Octal
    numOctal = convertir_octal(numBinario)

    # Convertir Binario a Hexadecimal
    numHexa = convertir_hexa(numBinario)

    # Mostrando los resultados juntos
    print (f"El número en binario ingresado es: {numBinario}\n"
        f"El número convertido a decimal con la funcion es: {numDecimal}\n"
        f"El número convertido a octal con la funcion es: {numOctal}\n"
            f"El número convertido a hexadecimal con la funcion es: {numHexa}\n")


def instrucciones():
    print (f"\nEste programa te permitirá convertir un numero binario de 16bits, "
       f"a su representación en decimal, octal y hexadecimal.")
    print (f"\nPara ello usted debe ingresar el número binario de 16 bits máximo (un máximo de 16 caracteres)") 


###$$$  PROGRAMA PRINCIPAL

system ("cls")
print (f"\t\tBienvenido al Programa de intercambio de sistemas númericos.")
instrucciones()
sleep (6)
system ("cls")

while True:
    print (f"\t\tPrograma de intercambio de sistemas númericos.")
    print ("Menu de opciones:\n"
           "1 Para ver las indicaciones nuevamente.\n"
           "2 Para ingresar un número binario y realizar los calculos de conversion.\n"
           "3 Para salir del programa.\n"
           )
    try:
        opcion = int(input("Ingrese una opcion: "))
        
        if opcion == 1:
            system ("cls")
            print (f"\t\tPrograma de intercambio de sistemas númericos.")
            instrucciones()
            sleep (6)
            system ("cls")
        elif opcion == 2:
            system ("cls")
            print (f"\t\tPrograma de intercambio de sistemas númericos.")
            ingresar_binario()
            enter = str(input("\nPara continuar presione enter.\n"))
            system ("cls")
        elif opcion == 3:
            system ("cls")
            print (f"\t\tPrograma de intercambio de sistemas númericos.")
            print ("Saliendo del programa\n"
                "Muchas Gracias")
            sleep (4)
            system ("cls")
            break
            
        else:
            print ("Opción incorrecta. Por  favor seleccione una opción válida.")
            system ("cls") 
            sleep (4)
    except ValueError: 
        print ("Solo puede ingresar números")
        sleep (4)
        system ("cls") 
        