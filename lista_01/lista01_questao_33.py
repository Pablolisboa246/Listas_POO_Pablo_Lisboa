tempo1=float(input("digite tempo do servidor 1"))
tempo2=float(input("digite tempo do servidor 2"))
tempo3=float(input("digite tempo do servidor 3"))
tempo4=float(input("digite tempo do servidor 4"))

menor=tempo1
if tempo2 < menor:

    menor=tempo2

if tempo3 < menor:
    menor=tempo3

if tempo4 < menor:

    menor=tempo4
print ("menor tempo de resposta foi",menor,"milissegundos")
