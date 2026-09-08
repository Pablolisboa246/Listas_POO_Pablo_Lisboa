def calcular(valor1,valor2):

    produto=valor1*valor2

    if produto <= 1000:
        return produto
    else:
        return valor1+valor2

numero1 = int(input("digite primeiro valor"))
numero2=int(input("digite segundo valor"))
resutado=calcular(numero1,numero2)

print ("resultado",resutado)
