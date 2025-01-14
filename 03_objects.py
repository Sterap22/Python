# Creacion de matriz y asignacion de valores
matrix  = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
print(matrix[2][1])

# creacion de variable tipo tuple las cuales son inmutables
number = (1,2,3,4,5)
print(type(number))

# Diccionario de datos

diccionary = {
    1: "Hola",
    2: "Mundo",
    3: "Estoy",
    4: "Vivo"
    }
print(diccionary)

informations = {
    "nombre": "Sterap",
    "Apellido": "dev",
    "Altura": 1.60,
    "Edad": 59
}

print(informations)
del informations["Edad"] #Eliminacion de item en el diccionario
print(informations)

keys_cus = informations.keys() # Extraer solo las claves del objecto
print(keys_cus)
print(type(keys_cus)) 

values_cus = informations.values()  # Extraer solo los valores del objeto
print(values_cus)
print(type(values_cus))

# Creacion de  diccionario tridimensional 
contacts = {
    "Sterap":{
        "nombre": "Sterap",
        "Apellido": "dev",
        "Altura": 1.70,
        "Edad": 59
    },
    "Carla":{
        "nombre": "Carla",
        "Apellido": "Ramirez",
        "Altura": 1.60,
        "Edad": 59
    },
}

print(contacts)

# Creacion de arreglo y asignacion de datos
squares = [ x**2 for x in range(1,11)]
print(squares)

celsius = [ 0, 10, 20, 30, 40]
fahrenheit = [(temp * 9/5) *32 for temp in celsius] # Conversion de C a F
print("Temperatura de F: ", fahrenheit)

# Numeros pares 
envens = [ x for  x in range(1,21) if x%2 == 0 ] # Utilizamos el modulo 2 de x para optener los numeros pares de 1 a 20
print(envens)

# Llenado de arreglo mediante append con for anidados
transposed = []
for i in range(len(matrix[0])):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)
