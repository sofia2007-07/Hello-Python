# Clase en video:
# https://youtu.be/Kp4Mvapo5kc?t=8643

### Strings ###

my_string = "Hola Mundo"
my_other_string = 'Python es genial'

print(len(my_string))
print(len(my_other_string))
print(my_string + " - " + my_other_string)

my_new_line_string = "Primera línea\nSegunda línea"
print(my_new_line_string)

my_tab_string = "\tEste es un ejemplo con tabulación"
print(my_tab_string)

my_scape_string = "\\Este texto tiene un caracter escapado\nNueva línea"
print(my_scape_string)

# Formateo

name, surname, age = "Juan", "Pérez", 20
print("Mi nombre es {} {} y tengo {} años".format(name, surname, age))
print("Me llamo %s %s y tengo %d años" % (name, surname, age))
print("Nombre: " + name + " " + surname + ", Edad: " + str(age))
print(f"Soy {name} {surname} y tengo {age} años")

# Desempaquetado de caracteres

language = "python"
a, b, c, d, e, f = language
print(a)
print(f)

# División

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:4:2]
print(language_slice)

# Reverse

reversed_language = language[::-1]
print(reversed_language)

# Funciones del lenguaje

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("123".isnumeric())
print(language.lower())
print(language.lower().isupper())
print(language.startswith("py"))
print("PY" == "py")  # Comparación normal
