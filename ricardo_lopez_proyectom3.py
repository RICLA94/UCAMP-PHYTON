#Programa para simulación de una maquina de Galton y su graficación.
#Lo primero es importar matplotlib & random para poder utilizarlas en nuestro programa. 
import matplotlib.pyplot as plot
import random

#Ahora se define la funcion que se va encargar de simular el lanzamiento de las canicas con argumentos muestra, inicio y rango

def lanzamiento_canicas (muestra,inicio,rango):
#Se establece una variable que va guardar una lista donde se van a guardar los datos generados
    num = []
#Se genera un ciclo for para que simulemos la cantidas de 3000 muestras o canicas
    for i in range (muestra):
#Ahora se establece la variable lista que es la que nos va a servir a determinar la posición de la canica, como vamos a iniciar en el centro de un rango de 12. Se establece 6 como base.
        lista = inicio
# Despues de crea un nuevo ciclo for para poder ir haciendo la simulación de la caida de las canicas, donde establecemos un rango de 12 ya que son el numero de obstaculos
        for i in range (rango):
#Para poder diferenciar debemos crear una variable que tendra valores aleatorios entre 0 y 1 los cuales nos van a sumar o restar a la base de 6 para determinar la posicion.
            b=(random.randint(0,1))
            if b==1:
                lista = lista+1
            else:
                lista = lista-1
#Ya que se tiene la posición determinada, se procede a guardar los datos en la lista llamada num.
        num.append(lista)

#Ahora para poder utilizar los valores de la lista num, tenemos que usar la funcion return para que no llamemos una lista vacia.
    return num

#Ahora para poder usar la funcion de lanzamiento de canicas vamos a guardar sus datos en una variable llamada canicas.Al momento de llamar la funcion podemos 
#Definir los valores que queremos para simular en la maquina de Galton, para efectos del proyecto se colocaron 3000, 6 y 12
canicas =lanzamiento_canicas(3000,6,12)
#Y para poder ayudarnos a determinar los intervalos de los valores vamos a usar la funcion min y max para sacar los limites y los guardamos en una variable.
intervalos = range (min(canicas),max(canicas))

#Se denine una nueva funcion que nos va a ayudar a graficar
def graficar():
#Se definen los valores a graficar en el histograma, que en este caso son las variables que guardan los valores de la funcion de lanzamiento de canicas
    plot.hist(x = canicas, bins =intervalos, color='navy')
#Se colocan los nombres de los ejes y el titulo de la grafica
    plot.title ('Histograma Maquina de Galton - Ricardo Lopez M3')
    
    plot.xlabel('Intervalo')
    plot.ylabel('Frecuencia')
#Se llama la funcion show para poder visualizar el histograma.
    plot.show()
    
#Solo para efectos visuales se manda imprimir la variable canicas la cual guarda la lista de los valores obtenidos.
print(f'Los valores generados para la lista son los siguientes: {canicas}')
#Finalmente se llama a ejecutar la función graficar la cual nos va a mostrar el histograma de la simulación realizada.
graficar()



