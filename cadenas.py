texto_variado = "Palabra 1234 !%$$%"
print(type(texto_variado))
#Uso de comillas triples
print ('''
Funcionamiento de tripe comilla
nos sirve para que podamos imprimir 
los strings de la misma manera en la que 
se escribe en el codigo:
    1.- Ejemplo 1
        2.- Ejemplo n
''')
#Uso de diagonal invertida
print ('''
La diagonal invertida nos sirve \
para imprimir el siguiente string \
justo entrente de la linea en la \
que fue esada
''')

#El indice de los strings comienza desde el 0
texto = 'EJEMPLO'
#Podemos mandar imprimir cada index usando el nombre de la variable + []
print (texto [0])
print (texto [1])
print (texto [2])
print (texto [3])
print (texto [4])
print (texto [5])
print (texto [6])


# --------------Slicing o substringing------------

texto_2 = 'PHYTON'

print (texto_2[0:3]) #Se mandan a imprimir ese rango de indices -1, osea 0, 1 y 2
print (texto_2[0:-3])
print (texto_2[3:]) #Cuando quieres imprimir hasta el final se debera dejar vacio el numero de la derecha.
print (texto_2[:3]) #Cuando quieres imprimir desde el principio se debera dejar vacio el numero de la izquierda.

#---------------Cadenas y formatos-----------------

texto_3 = " HoLa MuNdO! Buenastardes"
print (texto_3.lower()) # Esto cambia las letras todas a minusculas
print (texto_3.upper()) # Esto cambia las letras todas a mayusculas 
print (texto_3.capitalize()) #Hace que la primer letra de toda la cadena salga en mayuscula y las otras miniscula. 
print (texto_3.title()) # Hace que la letra incial de cada palabra sea mayuscula.
print (texto_3.swapcase()) # Se intercambian las mayusculas por minusculas y minusculas por mayusculas

print ('{} + {} = {}'.format(2,3, 2+3))


#join split
frase = 'Hola,Mundo,Hoy,Es,Miercoles'
print (frase.split(","))




#find rfind


#replace
frase_nueva='Yo soy el mas poderoso y fuerte, ademas del mas listo'
print (frase_nueva.replace('fuerte','debil'))
print(frase_nueva.replace('mas','menos',1))
frase_modificada = frase_nueva.replace('Yo soy','Tu eres')
print (frase_modificada)


#lstrip, rstrip, strip
