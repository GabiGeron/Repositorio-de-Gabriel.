





numeros_usuario = []
numero_del_usuario = ""
while len(numeros_usuario) < 10:
    while not numero_del_usuario.isdigit():
        numero_del_usuario = input("Dime un numero: ")
    numeros_usuario.append(numero_del_usuario)
    numero_del_usuario = ""
    print("Numero anadido!")

numero_pequeno = numeros_usuario[0]

for numero in  numeros_usuario:
    if numero < numero_pequeno:
        numero_pequeno = numero
print("El numero mas pequeno es {}".format(numero_pequeno))