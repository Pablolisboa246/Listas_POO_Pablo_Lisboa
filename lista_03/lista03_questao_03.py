latencias=[]
ok=0
acima = 0

for i in range(10):

    valor=float(input("digite a latencia em ms"))
    latencias.append(valor)

    if valor <= 100:
        ok=ok+1
    else:
        acima=acima+1

med=sum(latencias)/len(latencias)
maior_lat=max(latencias)

print("testes ate 100ms",ok)
print ("testes acima de 100ms",acima)
print("media das latencias",med)
print("maior latencia",maior_lat)
