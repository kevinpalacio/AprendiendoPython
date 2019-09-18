# Autor : Kevin Oswaldo Palacios Jimenez
# Fecha de creacion: 16/09/19   

# Se genera un bucle con for 
# al no tener argumento print no genera ningun cambio 
# mas que continuar a la siguiente linea
for i in range (1,11): 
    encabezado="Tabla del {}"  
    print(encabezado.format(i))

    print() 
    # Usaremos un for dentro de otro generando un bucle mas
    for j in range(1,11): 
        # en donde i tendremos la base 
        # con j tendriamos el elemento
        salida="{} x {} = {}" 
        print(salida.format(i,j,i*j)) 
    else: 
       # con el bucle teniendo su proceso iterativo 
       # se saltaran las linea pero ejecutando el codigo 
        print() 