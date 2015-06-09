def cuadrado(n):
    """Devuelve el cuadrado de un numero."""
    squared = n**2
    print "%d al cuadrado es %d." % (n, squared)
    return cuadrado
    
#¡Llamá a la función cuadrado en la línea 9! Asegurate de
#incluir el número 10 entre paréntesis.
cuadrado(10)
