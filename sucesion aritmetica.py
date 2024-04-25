# Usar RECURSION para programar. 
# El usuario ingresa dos elementos de la sucesion, las posiciones que ocupan dichos numeros en la sucesion(tener en cuenta que se pueden ingresar valores que no sean consecutivos.) Ademas el usuario debe ingresar cuantos términos de la sucesion desea generar n
# Mostrar por pantalla los datos generados de izquierda a derecha y de derecha a izquierda


# Función recursiva para generar la secuencia
def generar_secuencia(nrInicio, nrFin, n, posActual, listaSecuencia):
    if posActual >= n:
        return listaSecuencia  # Base de la recursión, cuando se ha alcanzado el número de términos deseados

    # Calcular la diferencia entre términos
    diferencia = (nrFin - nrInicio) / (n - 1)
    
    # Agregar el siguiente término a la secuencia
    nrSiguiente = nrInicio + posActual * diferencia
    listaSecuencia.append(round(nrSiguiente,1))
    
    # Llamada recursiva para el siguiente término
    return generar_secuencia(nrInicio, nrFin, n, posActual + 1, listaSecuencia)

# Entrada del usuario
print("Ingrese el primer y último número de la sucesión:")
nrInicio = float(input("Primer número: "))
nrFin = float(input("Último número: "))
print ("")
print("Ingrese el número total de términos de la sucesión:")
n = int(input("Número total de términos: "))

# Inicializar la lista para la secuencia
listaSecuencia = []

# Llamar a la función recursiva para generar la secuencia
generar_secuencia(nrInicio, nrFin, n, 0, listaSecuencia)

# Mostrar la secuencia generada
print("Secuencia generada:\n"f"{listaSecuencia}")

