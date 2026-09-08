opcao = int(input("digite 1 pra hipotenusa ou 2 pra cateto"))

if opcao == 1:

    cateto1 = float(input("digite primeiro cateto"))
    cateto2 = float(input("digite segundo cateto"))
    hipotenusa = (cateto1 ** 2 + cateto2 ** 2) ** 0.5
    print("valor da hipotenusa eh", hipotenusa)

elif opcao == 2:
    hipotenusa = float(input("digite a hipotenusa"))
    cateto = float(input("digite o outro cateto"))
    cateto_calculado = (hipotenusa ** 2 - cateto ** 2) ** 0.5
    print("o valor do cateto eh",cateto_calculado)

else:
    print ("opcao invalda")
