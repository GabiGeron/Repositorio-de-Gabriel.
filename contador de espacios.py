frase_del_usuario = input("Dime una frase, para que te pueda decir un dato interesante")
espacio = [" "]
comas = [","]
puntos = ["."]
n_espacios = 0
n_de_comas = 0
n_de_puntos = 0



for letra in frase_del_usuario:
    if letra in espacio:
     n_espacios += 1
    elif letra in comas:
        n_de_comas += 1
    elif letra in puntos:
        n_de_puntos += 1
print("El numero de espacios que hay en esta frase es de{}".format(n_espacios))
print("El numero de comas que hay en esta frase es de{}".format(n_de_comas))
print("El numero de puntos que hay en esta frase es de{}".format(n_de_puntos))
