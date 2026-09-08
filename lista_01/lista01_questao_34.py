a= float(input("digite valor de a"))
b= float(input("digite valor de b"))
c= float(input("digite valor de c"))
delta= (b ** 2) - (4 * a * c)

print("valor de delta eh", delta)

if delta < 0:
    print ("nao tem raizes reais")

elif delta == 0:

    x= -b / (2 * a)
    print("raiz real eh", x)

else:

    x1= (-b + delta ** 0.5) / (2 * a)
    x2= (-b - delta ** 0.5) / (2 * a)

    print ("primeira raiz eh", x1)

    print("segunda raiz eh", x2)
