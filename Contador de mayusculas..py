frase_del_usuario = input("Dime una frase y te dire las mayusculas que has usado en dicha frase: ")
mayusculas = 0

for letra in frase_del_usuario:
     if letra.isupper():
        mayusculas += 1
print("El numero de mayusculas que coniene tu frase es de {}".format(mayusculas))