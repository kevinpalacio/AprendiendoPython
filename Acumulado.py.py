# Autor : Kevin Oswaldo Palacios Jimenez
# Fecha de creacion: 16/09/19   

# Al tener int podremos introducir un valor pasado
# para convertir en un entero 
acumulado=int(0) 
numero=str("") 

# Se usara true como condicion de while, se formara 
# un ciclo el cual no se dejara de generar hasta que
# utilicemos break 
while True: 
    numero=input("Dame un numero entero: ") 
    if numero=="": 
       # Al tener un numero vacio nos notificara si lo es
       print("Vacio. Salida del programa") 
       break 
    else: 
        # Proporcion de un valor acumulado = acumulado + numero
        # Al utilizar la suma con el calculo (+=) 
        acumulado+=int(numero) 
        salida="Monto acumulado: {}"
        print(salida.format(acumulado))   
        