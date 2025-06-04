# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=5665

### Operadores Aritméticos ###

# Operaciones con enteros
print(2 + 2)
print(2 - 2)
print(2* 2)
print(2 / 2)
print(10 % 2)
print(10 // 2)
print(2 ** 2)
print(2 ** 2 + 2 - 3 / 4// 4)

# Operaciones con cadenas de texto
print("Buenas " + "Python " + "¿Cómo estas?")
print("Buenas" + str(2))

# Operaciones mixtas
print("Buenas " * 2)
print("Buenas" * (2 ** 2))

my_float = 2.5 * 2
print("Buenas " * int(my_float))

### Operadores Comparativos ###

# Operaciones con enteros
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(4 <= 4)
print(3 == 4)
print(3 != 4)

# Operaciones con cadenas de texto
print("Buenas" > "Python")
print("Buenas" < "Python")
print("aaaa" >= "abaa")  # Ordenación alfabética por ASCII
print(len("aaaa") >= len("abaa"))  # Cuenta caracteres
print("Buenas" <= "Python")
print("Buenas" == "Buenas")
print("Buenas" != "Python")

### Operadores Lógicos ###

# Basada en el Álgebra de Boole https://es.wikipedia.org/wiki/%C3%81lgebra_de_Boole
print(3 > 4 and "Buenas" > "Python")
print(3 > 4 or "Buenas" > "Python")
print(3 < 4 and "Buenas" < "Python")
print(3 < 4 or "Buenas" > "Python")
print(3 < 4 or ("Buenas" > "Python" and 4 == 4))
print(not (3 > 4))
