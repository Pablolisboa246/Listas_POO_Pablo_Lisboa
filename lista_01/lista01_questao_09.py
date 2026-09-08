l1=float(input("digite primeiro lado"))
l2=float(input("digite segundo lado"))
l3=float(input("digite terceiro lado"))

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print ("os valor formam um triangulo")

    if l1 == l2 and l2 == l3:
        print ("o triangulo eh equilatero")

    elif l1 != l2 and l1 != l3 and l2 != l3:
        print ("o triangulo eh escaleno")

else:
    print ("os valor nao formam um triangulo")
