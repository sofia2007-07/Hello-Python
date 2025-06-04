# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=2938

### Variables ###

my_string_variable = "quiero una hamburguesa"
print(hamburguesa)

my_int_variable = 42
print(numero)

número_como_texto = str(numero)
print(numero_como_texto)
print(type(numero_como_texto))

tengo_sueño= True
print(tengo_sueño)

# Concatenación de variables en un print
print(quiero una hamburguesa, numero_como_texto, tengo_sueño)
print("¿tenes sueño?:", tengo_sueño)

# Algunas funciones del sistema
print(len(numero))

# Variables en una sola línea. ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Sofia", "Loprete", 'Lopretesofi', 17
print("Me llamo:", name, surname, ". Mi edad es:",
      age, ". Y mi alias es:", alias)

# Inputs
name = input('¿Cuál es tu nombre? ')
age = input('¿Cuántos años tienes? ')
print(name)
print(age)

# Cambiamos su tipo
name = 17
age = "Sofia"
print(name)
print(age)

# ¿Forzamos el tipo?
address: str = "Mi dirección"
address = True
address = 5
address = 1.2
print(type(address))
