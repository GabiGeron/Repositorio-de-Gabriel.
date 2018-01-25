
primero = input("Dime un primer numero")
segundo = input("Dime un segundo numero")
tercero = input("Dime un tercer numero")

if (primero > segundo and primero > tercero):
    print("El numero mayor es {}".format(primero))
else:
    if (segundo > primero and segundo > tercero):
        print("El numero mayor es {}").format(segundo)
    else:
        if (tercero > primero and tercero > segundo):
            print("El numero mayor es {}").format(tercero)
