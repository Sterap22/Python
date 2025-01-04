# Variables en Python
# Una variable es  un especacio en memoria que almacena un valor
# El nombre de una variable puede contener letras, numeros y guiones bajos

my_string_variable = 'Hola! soy tu variable' # Variable y asignacion de valor de tipo string
print(my_string_variable)

my_int_variable = 4 # Variable y asignacion de valor de tipo int
print(my_int_variable)

my_bool_variable = False # Variable y asignacion de valor de tipo boolean
print(my_bool_variable)

my_int_to_str_variable = str(my_int_variable) # Variable de tipo string con valor numerico convertido a string
print(type(my_int_to_str_variable))

# Algunas funciones precargadas del sistema
print(len(my_string_variable))

# Variables en una sola  linea
# Declaracion y asignacion de valores poco usadas
name, surname, alias,  age = 'Brain', 'Meg', 'BrainMeg', 3
print('Me llamo:', name, surname, '. Mi edad es:', age, 'y me dicen:',  alias)

# Inputs
# Solicitar datos al usuario
first_name = input('¿Cuál es tu  nombre? ') # Solicita al usuario que ingrese el nombre
age = input('¿Cuál es tu edad? ') # Solicita al usuario que ingrese su edad

print('Hola,',first_name,'tienes', age,'años')

