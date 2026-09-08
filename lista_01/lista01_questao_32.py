peso = float(input("digite peso em kg"))
altura = float(input("digite altura em metros"))

imc = peso / (altura ** 2)

print("imc eh", imc)
if imc < 18.5:

    print ("abaixo do peso")

elif imc < 25:
    print("peso normal")

elif imc < 30:

    print("sobrepeso")
else:

    print("obesidade")
