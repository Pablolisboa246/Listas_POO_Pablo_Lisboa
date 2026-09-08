x = float(input("digite coordenada x"))
y = float(input("digite coordenada y"))

if x > 0 and y > 0:
    print("primeiro quadrate")

elif x < 0 and y > 0:

    print("segundo quadrate")
elif x < 0 and y < 0:

    print ("terceiro quadrate")

elif x > 0 and y < 0:
    print("quarto quadrate")

else:

    print("ponto ta no eixo ou na origem")
