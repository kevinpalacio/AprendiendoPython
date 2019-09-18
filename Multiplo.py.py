# Autor : Kevin Oswaldo Palacios Jimenez
# Fecha de creacion: 16/09/19   

# Utilizamos int para los valores convertirlos 
# de pasado a entero
numero=int(input("Dame un numero entero: ")) 
# Los valores seran booleanos para calificarlos 
# Cuando el residuo sera cero sera que el numero es multiplo
esMultiplo3=((numero%3)==0) 
esMultiplo5=((numero%5)==0)
esMultiplo7=((numero%7)==0) 
# Utilizaremos and para que las incognitas sean verdaderas
# Utilizaremos or para cuando una sola de las incognitas sean verdadera
# Con los parentesis tendremos bien identificados las condiciones 
# para python y dejaremos la ultima de manera independiente
if ((esMultiplo3 and esMultiplo5)or es esMultiplo7): 
    print("Correcto.") 
else: 
    print("Incorrecto.") 
    
