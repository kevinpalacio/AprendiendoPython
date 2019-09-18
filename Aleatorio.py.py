# Autor : Kevin Oswaldo Palacios Jimenez
# Fecha de creacion: 16/09/19 

# Python tendra varios modulos(module), estos modulos son
# librerias que tiene python 
# Se necesita in modulo para un programa, 
# import, es la primera instruccion que debera estan presente 
# en la consola 
import random 

# Definimos una variable float con un valor asignado
numero1=float(10.5)

# Debemos usar una funcion ya que estan cuentan 
# con cumplir con un objetivo en especial
# despues de la funcion se mostrara en la pantalla
# lo que sera parte de la funcion siempre y cuando
# este dentro de ella de esa manera se cumplira
def miFuncion():
    # random.randrange lo que hace es tener un numero al azar
    # el cual se convierte en tipo float
    numero2=float(random.randrange(1,10)) 
     
    mensaje="La suma de {} y {} es de {}" 
    print(mensaje.formart(numero1,numero2.numero1+numero2)) 

# Al terminar la funcion con la cual tengamos las indicaciones 
# correctas esta definira el codigo 
miFuncion()     