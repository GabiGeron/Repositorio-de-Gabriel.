"""
Crea un programa que sea capaz de guardar los nombres de tus amigos y sus anos de nacimiento
"""
salida = False
agenda = dict()
while not salida:
    datos_amigos = input("Ano de nacimento y nombre de tus amigos{A] / Consultar numero [C]] / Salir [S]:")
    if datos_amigos == "A":
        print("Vamos anaadir datos sobre tus amigos!")
        nombre = input("Nombre de tu amigo")
        numero = input("Dime el ano y dia de nacimiento de tu amigo")
        agenda[nombre] = numero

    elif datos_amigos == "C":
        print("Consultar datos")
        print("---------------------:")
        nombre = input("De quien quieres saber datos?")
        print(agenda[nombre])
    elif datos_amigos == "S":
        salida = True
