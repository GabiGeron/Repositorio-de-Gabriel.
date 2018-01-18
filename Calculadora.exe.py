calculo_elegido = input("Que operacion quieres realizar ? ((*) / (/)  (+) o  (-)")

resultado = 0

primer_numero = int(input("Dime un primer  numero(0,1,2,3,4,5,6,7,8,9"))
segundo_numero = int(input ("Dime un segundo numero(0,1,2,3,4,5,6,7,8,9"))
if calculo_elegido  == "*":
    resultado = primer_numero * segundo_numero
elif calculo_elegido == "/":
    resultado = primer_numero / segundo_numero
elif calculo_elegido =="+":
    resultado = primer_numero + segundo_numero
elif calculo_elegido == "-":
    resultado = primer_numero - segundo_numero
print(resultado)
