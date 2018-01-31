






salida = False
agenda = dict()

while not salida:
    accion = input("Que quieres hacer? [Anadir numero[A] / Consultar numero [C]] / Salir [S]:")
    #accion anadir
    if accion == "A":
        print("Vamos a anadir un numero de telefono:")
        print("---------------------:")
        nombre = input("Nombre:")
        numero = input("Numero:")
        agenda[nombre] = numero

        # Accion consultar
    elif accion == "C":
        print("Consultar numero:")
        print("---------------------:")
        nombre = input("De quien quieres saber el numero:")
        print(agenda[nombre])


    # accion salir
    elif accion == "S":
        salida = True


