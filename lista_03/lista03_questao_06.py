numero1=int(input("digite primeiro numero"))
numero2=int(input("digite segundo numero"))

if numero1 <= numero2:

    for numero in range(numero1,numero2+1):
        print(numero)

else:

    for numero in range(numero2,numero1+1):
        print(numero)
