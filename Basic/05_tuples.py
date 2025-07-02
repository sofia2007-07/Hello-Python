# Clase en video: https://youtu.be/Kp4Mvapo5kc?t=14711

### Tuplas ###

# Crear tuplas

tupla_1 = tuple()
otra_tupla = ()

tupla_1 = (25, 1.70, "Lucas", "Pérez", "Lucas")
otra_tupla = (10, 20, 30)

print(tupla_1)
print(type(tupla_1))

# Ver elementos y buscar datos

print(tupla_1[0])
print(tupla_1[-1])
# print(tupla_1[5]) → Error
# print(tupla_1[-6]) → Error

print(tupla_1.count("Lucas"))
print(tupla_1.index("Pérez"))
print(tupla_1.index("Lucas"))

# tupla_1[1] = 1.75 → Error: no se puede cambiar una tupla

# Unir tuplas

tupla_total = tupla_1 + otra_tupla
print(tupla_total)

# Parte de una tupla

print(tupla_total[2:5])

# Convertir a lista para modificar

tupla_1 = list(tupla_1)
print(type(tupla_1))

tupla_1[4] = "DevTeam"
tupla_1.insert(1, "Celeste")
tupla_1 = tuple(tupla_1)
print(tupla_1)
print(type(tupla_1))

# Borrar tupla entera
9
# del tupla_1[2] → Error: no se pueden borrar partes

del tupla_1
# print(tupla_1) → Error: ya no existe la tupla
