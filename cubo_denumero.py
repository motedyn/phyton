def cubo(numero):
    resultado=numero**3
    print resultado
    return resultado
    
def por_tres(numero):
    residuo=numero%3
    if (residuo==0):
        print numero
        return cubo(numero)
    else:
        return False
        
        
cubo(7)
