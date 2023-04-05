#PROGRAMA 1 VERIFICACIÓN DE UNA FRASE:
#Primero vamos a imprimir un mensaje con las instrucciones.
print ("****PROGRAMA 1 VALIDACIÓN DE LONGITUG DE UNA FRASE:****\n")
print("""Por favor ingresa una frase, consideraciones previas:
                - Entre 4 y 8 letras unicamente.
                - El programa va solicitar la frase hasta que sea correcta.""")
#Ahora vamos a comenzar con un ciclo while el cual nos va servir para volver a solcitar la frase
#en caso de que no se cumplan las condiciones:
while True:
#Ahora se define una variable para guardar la frase a evaluar
    frase = str(input("Por favor ingresa la frase: "))
#Se establece un if para evaluar si la frase cumple con los requisitos de minimo 4 letras y maximo 8.
    if len(frase) >= 4 and len(frase) <= 8:
# Si la frase cumple con el requisito se va imprimir el mensaje de frase correcta y finaliza el ciclo while.
        print (f"""La frase es correcta y cumple con los requisitos.
                        Longitud de la frase = {len(frase)}
                   Muchas gracias por usar este programa.\n""")
        break

#Ahora se establece un elif para evaluar si la frase es menor a 4 letras.
    elif len(frase) < 4:
#En caso de que la frase cumpla con la condicion de ser menor de 4 letras se manda un mensaje para volver a intentar y que el usuario
#Pueda saber cuantas letras le hicieron falta y se repite el ciclo hasta que se cumpla con los requerimientos.
        print (f"La frase es muy corta ya que tiene solo {len(frase)} letras (le faltan {4- len(frase)} letras), por favor intenta nuevamente.")

#Ahora se establece un elif para evaluar si la frase es mayor a 8 letras.
    elif len(frase) > 8:
#En caso de que la frase cumpla con la condicion de ser mayor a 4 letras de manda un mensaje para volver a intentar y que el usuario
#Pueda saber cuantas letras le sobraron y se repite el ciclo hasta que se cumpla con los requerimientos.
        print (f"La frase es muy larga ya que tiene {len(frase)} letras (le sobran {len(frase)-8} letras). Por favor intenta de nuevo.")

print ("****PROGRAMA 2 IDENTIFICACIÓN DE CUADRANTES:****\n")

#PROGRAMA 2 IDENTIFICACIÓN DE CUADRANTES
#Primero vamos a declarar las variables para las X y Y
#Para que las variables guarden el dato que ingrese el usuario, se agrega input
x=float(input("Ingresa la coordenada del eje X: "))
y=float(input("Ingresa la coordenada del eje Y: "))
#Ahora se colocan las condiciones que nos van a indicar el cuadrante que corresponda en base a los datos:

#Esta condición de if nos va a evaluar numeros positivos de x y y para el cuandrante I.
if x > 0 and y >0:
    print (f"El punto para las coordenadas {x,y}, se encuentra en el cuadrante I.")
#Esta condición de if nos va a evaluar numeros negativos de X y positivos de Y para el cuandrante II.
if x < 0 and y >0:
    print (f"El punto para las coordenadas {x,y}, se encuentra en el cuadrante II.")
#Esta condición de if nos va a evaluar numeros negativos de x y y para el cuandrante III.
if x < 0 and y <0:
    print (f"El punto para las coordenadas {x,y}, se encuentra en el cuadrante III.")
#Esta condición de if nos va a evaluar numeros positivos de X y negativos de Y para el cuandrante IV.
if x > 0 and y <0:
    print (f"El punto para las coordenadas {x,y}, se encuentra en el cuadrante IV.")
#En este caso esta condicion if va a evaluar si X y Y son cero, lo cual indica que es el origen.
if x==0 and y==0: 
    print (f"Tus coordenadas {x, y} corresponden al origen.")
#Esta condición de elif nos va evaluar si el punto queda sobre alguno de los ejes.
elif x==0 or y==0:
    print (f"El punto para tus coordenadas {x,y} van sobre alguno de los ejes.")
