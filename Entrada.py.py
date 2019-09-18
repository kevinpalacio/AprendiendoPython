# Autor : Kevin Oswaldo Palacios Jimenez
# Fecha de creacion: 16/09/19 

entrada=input() 
print(type(entrada)) 
# Una variable de tipo booleana confirmara el digito capturando siempre 
# y cuando cuenta con un numero decimal que se
# float, no debera de retornar -1 si se encontro lo buscado
# Indicara que es True cuando sea esEntero
esEntero=(entrada.isdigit() and entrada.find (".")==-1)
if(esEntero): 
    # Se cumplira siempre y cuando la condicion es verdadera (True) 
    print("Dato entero. ¡Muy bien!") 
else: 
    # No se cumplira ya que la condicion es falsa (False) 
    print("Dato no es entero. vuelve a intentar.") 