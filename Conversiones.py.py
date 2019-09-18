# Autor : Kevin Oswaldo Palacios Jimenez
# Fecha de creacion: 16/09/19 

# Declara variable tipo str con una cadena los cuales digitos son los siguiente 
numero="1234"
# Imprimira el tipo de dato que es la variable 
# type() es un dato type no str  
print(type(numero)) 
# La equivalencia de la cadena sera ahora int. 
numero=int(numero) 
# Mostrara su nuevo tipo ya que ah cambiado, sin embargo 
# seguimos teniendo la misma variable.
print(type(numero)) 
# Las posiciones donde deberan de ir los valores se declaran 
# como str usanndo format. 
salida="El numero utilizado es {}" 
# Imprime resultado en los {}, es la ubicacion de los valores de 
# los numeros
print(salida.format(numero)) 
