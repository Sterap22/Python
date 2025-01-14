# Creacion de condicionales  si x es mayor a 5 imprime el siguiente texto
# de lo contrario imprime todo lo que se encuentra dentro del else
x =  10
if x > 5: # SI
    print("X es mayor a 5")
elif x  == 5: # Este condicional es un sino 
    print("X  es igual a 5")
else: # entonces
    print("X es menor a 5 o no cumple con la condición")
print("Fin de la operracion")


# se puede ralizar validaciones complejas ya sea de 2 elementos o mas
x = 15
y  = 20

if  x > 10  and y < 50: # Condicionale con Y
    print("X es mayoy a 10 y Y es menor a 50")
elif x == 15 or y != 20: # Condicional donde se hace uso de O en caso que se cumpla cualquiera de las  2 condiciones esta estara en un estado verdadero
    print("X es igual a 15 O Y es diferente a 20") # Condicional de 3 parametros 
elif ((x == 15 and y == 0) or y > 10 ):
    print("Validacion de 3 parametros")