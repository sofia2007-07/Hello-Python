# Clase en video:
# https://youtu.be/Kp4Mvapo5kc?t=10872

### Listas ###

# Definición

lista_uno = list()
otra_lista = []

print(len(lista_uno))

lista_uno = [12, 45, 62, 90, 30, 14, 7]
print(lista_uno)

otra_lista = [99, 3.14, "Ana", "García"]
print(type(lista_uno))
print(type(otra_lista))

# Acceso a elementos y búsqueda

print(otra_lista[0])
print(otra_lista[1])
print(otra_lista[-1])
print(lista_uno.count(30))
print(otra_lista.index("Ana"))

# Desempaquetado de elementos
num, decimal, nombre, apellido = otra_lista
print(nombre)

# unir listas
print(lista_uno + otra_lista)

# Modificación, inserción y borrado

otra_lista.append("Python")
print(otra_lista)

otra_lista.insert(1, "Verde")
print(otra_lista)

otra_lista[1] = "Celeste"
