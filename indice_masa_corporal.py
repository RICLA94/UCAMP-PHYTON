print('Calculadora de índice de masa corporal (IMC)')
personas = int(input('Por favor ingresa el numero de personas que desean conocer su IMC:'))
if personas == 0:
    print ("Vuelve cuando requieras consultar el indice de masa corporal.")

while personas > 0:

#NOMBRE Y APPELLIDOS

    nombre = str(input('Ingresa tu nombre por favor: '))
    while len(nombre)==0:
        nombre=str(input('Olvidaste tu nombre, por favor ingresalo: '))

    apellido_paterno = str(input('Ingresa tu apellido paterno por favor: '))
    while len(apellido_paterno)==0:
        apellido_paterno=str(input('Olvidaste tu apellido paterno, por favor ingresalo: '))

    apellido_materno = str(input('Ingresa tu apellido materno por favor: '))
    while len(apellido_materno)==0:
        apellido_materno=str(input('Olvidaste tu apellido materno, por favor ingresalo: '))
#EDAD
    while True:
        edad = input('Ingresa tu edad en años: ')
        try:
            edad = int(edad)
            if edad > 0:
                break
            elif edad == 0:
                print ('*La edad no puede ser igual a 0')
        except ValueError:
            print ('Usa solo numeros| No dejes vacio el campo.')

#PESO
    while True:
        peso = input('Ingresa tu peso en Kg: ')
        try:
            peso = float(peso) 
            if peso > 0:
                break
            elif peso == 0:
                print ('*El peso no puede ser igual a 0')
        except ValueError:
            print ('Usa solo numeros| No dejes vacio el campo.')
#ALTURA
    while True:
        altura = input('Ingresa tu altura en metros: ')
        try:
            altura = float(altura)
            if altura > 0:
                break
            elif altura == 0:
                print ('*La altura no puede ser igual a 0')
        except ValueError:
            print ('Usa solo numeros| No dejes vacio el campo.')

#CALCULO DE IMC
    indice_masa_corporal = (peso / altura**2)

#EVALUACIÓN DE IMC
    if indice_masa_corporal >= 0 and indice_masa_corporal <= 15.99 :
        evaluacion = 'Delgadez severa'
    elif indice_masa_corporal >= 16.00 and indice_masa_corporal <= 16.99 :
        evaluacion= "Delgadez moderada"
    elif indice_masa_corporal >= 17.00 and indice_masa_corporal <= 18.49:
        evaluacion ="Delgadez leve"
    elif indice_masa_corporal >= 18.50 and indice_masa_corporal <= 24.99 :
        evaluacion = "Normal"
    elif indice_masa_corporal >= 25.00 and indice_masa_corporal <= 29.99:
        evaluacion= "Sobrepeso"
    elif indice_masa_corporal >= 30.00 and indice_masa_corporal <= 34.99:
        evaluacion="Obesidad leve"
    elif indice_masa_corporal >= 35.00 and indice_masa_corporal <= 39.00:
        evaluacion="Obesidad media"
    elif indice_masa_corporal >= 40.00:
        evaluacion="Obesidad morbida"

#IMPRESION DE RESULTADOS        
    if edad >= 18:
        print (f'¡Muchas gracias por los datos! {nombre}, tu eres mayor de edad y tu IMC es: {indice_masa_corporal:.2f}')
    else:
        print (f'¡Muchas gracias por los datos! {nombre}, tu eres menor de edad y tu IMC es: {indice_masa_corporal:.2f}.')
    print (f'''
        ---------------------RESUMEN DE DATOS INGRESADOS---------------------
      Nombre:{nombre} {apellido_paterno} {apellido_materno}.
      Edad: {edad} años.
      Altura: {altura} metros.
      peso: {peso} kilos.
        -------------------------------RESULTADO-----------------------------
      Tu indice de masa corporal nos indica que puedes presentar: {evaluacion}.
      Por favor revisa con tu medico los resultados para un diagnostico mas acertado.''')
#CONTADOR DE PERSONAS MENOS 1
    personas = personas-1

    if personas == 0:
        print ('Muchas gracias por usar la calculadora de IMC, vuelve pronto.')
