valor1 =float(input("digite primeiro valor"))
valor2 =float(input("digite segundo valor"))
operacao =input("digite +,-,* ou /")

if operacao == "+":
    resutado =valor1 + valor2

    print("resutado",resutado)

elif operacao == "-":
    resutado =valor1 - valor2

    print ("resutado",resutado)

elif operacao == "*":
    resutado =valor1 * valor2

    print("resutado",resutado)

elif operacao == "/":
    if valor2 != 0:

        resutado =valor1 / valor2

        print ("resutado",resutado)
    else:

        print("nao da pra dividir por zero")

else:
    print("operacao invalda")
