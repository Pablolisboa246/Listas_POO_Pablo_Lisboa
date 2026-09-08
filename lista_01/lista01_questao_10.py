valor=float(input("digite valor financiado"))
taxa=float(input("digite a taxa de juros mesal"))
meses=int(input("digite a quantidae de meses"))
juros=valor *(taxa/100)*meses
montante=valor+juros

print("valor dos juros eh",juros)
print("total a pagar",montante)
