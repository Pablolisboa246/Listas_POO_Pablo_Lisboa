medida1 = float(input("digite primeira medicao"))
medida2 = float(input("digite segunda medicao"))
medida3 = float(input("digite terceira medicao"))
medida4 = float(input("digite quarta medicao"))
medida5 = float(input("digite quinta medicao"))
soma = 0
quantidade = 0

if medida1 > 0 and medida1 < 1000:

    soma = soma + medida1
    quantidade = quantidade + 1

if medida2 > 0 and medida2 < 1000:

    soma = soma + medida2
    quantidade = quantidade + 1

if medida3 > 0 and medida3 < 1000:
    soma = soma + medida3
    quantidade = quantidade + 1
if medida4 > 0 and medida4 < 1000:

    soma = soma + medida4
    quantidade = quantidade + 1

if medida5 > 0 and medida5 < 1000:

    soma = soma + medida5
    quantidade = quantidade + 1

if quantidade > 0:
    media = soma / quantidade

    print ("media das medicoes validas eh",media)

else:
    print ("nenhuma medicao valida informada")
