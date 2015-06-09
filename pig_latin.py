pyg = 'ay'

original = raw_input('Escribi una palabra:') #entrada por teclado
palabra=original.lower() #convierte la entrada a minusculas
if len(palabra) > 0 and palabra.isalpha(): #condiciona si la entrada es mayor a 0 y son caracteres, entonces 
	print palabra # muestra en pantalla la entrada.
else:
	print 'vacio' #sino se cumple, muestra vacío.

primera=palabra[0] # asigna a la variable primera, la primera letra de la palabra ingresada
nueva_palabra=palabra+primera+pyg #concatena y la guarda en una nueva variable
nueva_palabra= nueva_palabra[1:len(nueva_palabra)] # recorta la palabra para que se muestra solo a partir de la primera letra

print nueva_palabra #imprime el resultado
