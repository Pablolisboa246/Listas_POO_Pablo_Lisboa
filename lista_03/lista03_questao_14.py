numero =int(input("digite um numero inteiro nao negativo"))

if numero < 0:
    print ("numero invaldo")

else:
    fatorial=1

    for i in range(1,numero+1):
        fatorial=fatorial*i

    print("fatorial eh",fatorial)
