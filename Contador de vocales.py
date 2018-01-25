texto_del_usuario  = input("Hola, me podrias decir alguna informacion acerca de ti?")
vocales = {"a", "e", "i", "o", "u"}
n_vocales = 0
for letra in texto_del_usuario:
    if letra in vocales:
        n_vocales += 1
print("El numero de vocales que contien tu frase es de {}".format(n_vocales))
