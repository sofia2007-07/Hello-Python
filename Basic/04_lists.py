# Clase en video:
# https://youtu.be/Kp4Mvapo5kc?t=10872

### Lists ###

# Definición

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [10, 20, 30, 40, 50]
print(my_list)
print(len(my_list))

my_other_list = [1.65, 60, "Sofi", "Gómez"]
print(type(my_list))
print(type(my_other_list))

# Acceso a elementos y búsqueda

print(my_other_list[0])
print(my_other_list[2])
print(my_other_list[-1])
print(my_other_list.count("Sofi"))
print(my_other_list.index("Sofi"))

# Desempaquetado

height, weight, name, surname = my_other_list
print(name)

# Concatenación

print(my_list + my_other_list)
print(my_list * 2)

# Creación, inserción, actualización y eliminación

my_other_list.append("Estudiante")
print(my_other_list)

my_other_list.insert(1, "Rojo")
print(my_other_list)

my_other_list[2] = "Azul"
print(my_other_list)

my_other_list.remove("Azul")
print(my_other_list)

my_list.remove(30)
print(my_list)

my_pop_element = my_list.pop(1)
print(my_pop_element)
print(my_list)

del my_list[0]
print(my_list)

# Operaciones con listas

my_new_list = my_list.copy()
my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

# Sublistas

print(my_new_list[1:3])

# Cambio de tipo

my_list = "Programando en Python"
print(my_list)
print(type(my_list))
