# Autor : Kevin Oswaldo Palacios Jimenez
# Fecha de creacion: 16/09/19  

# Se imprimira la pregunta para saber el valor que nos proporcionar 
# Determinaremos el numero del 1 al 9
numero=input("Dame un numero del 1 al 9: ") 
numeo=int(numero)
# Se creo una liga de la lista o seria de numero que determinamos 
# dependiendo de numero que hayamos propocionado 
# en range no se incluira la lista de los valores, 1 al 10 
for i in range(1,11): 
    # La i variara en cada iteracion
    salida="¨{} x {} = {}"
    print(salida.format(numero,i,i*numero))  
    