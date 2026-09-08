numero=int(input("digite um numero de 1 a 10"))

if numero >= 1 and numero <= 10:

    for i in range(1,11):
        print(numero,"x",i,"=",numero*i)

else:
    print("numero invaldo")
