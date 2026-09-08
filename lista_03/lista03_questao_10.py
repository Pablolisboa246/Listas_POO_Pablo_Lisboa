latencias=[]

for i in range(10):
    valor=float(input("digite a latencia"))
    latencias.append(valor)

menor = min(latencias)

print ("menor latencia foi",menor)
