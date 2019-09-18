# Autor : Kevin Oswaldo Palacios Jimenez
# Fecha de creacion: 16/09/19   

# Se usara input para que podamos introducir 
# datos de cualquier tipo
numero1=input("Numero1:") 
numero2=input("Numero2:") 
salida="Numeros proporcionados: {} y {}. {}." 
# Al usar if comprobaremos que la prueba sea verdadero
if (numero1==numero2): 
    # Al tener lo numeros iguales se mostraran aqui 
    print(salida.format(numero1, numero2,"Los numero son iguales")) 
else: 
    # usaremos otro if para la comprobacion de falso o verdaro
    if numero1>numero2: 
        # Notificara si el primer numero es mayor al segundo
        print(salida.format(numero1, numero2, "El mayor es el primero)) 
    else: 
        # De igual manera nos notificara si es lo contrario
        # el mayor es el segundo y no el primero
        print(salida.format(numero1,numero2,"El mayor es el segundo)) 
        