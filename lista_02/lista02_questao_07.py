notas=[]
qtd = int(input("quantas notas vai colocar"))

for i in range(qtd):
    nota=float(input("digite uma nota"))
    notas.append(nota)

try:
    med=sum(notas)/len(notas)
    print ("media das notas eh",med)

except ZeroDivisionError:
    print("nao tem nota pra calcular a media")
