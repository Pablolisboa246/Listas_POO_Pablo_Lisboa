notas=[]

while len(notas) < 5:

    try:
        nota = float(input("digite a nota"))
        notas.append(nota)

    except ValueError:
        print ("valor invaldo, digite um numero")

print("notas",notas)

med = sum(notas)/len(notas)

print("media",med)
print ("maior nota",max(notas))
print("menor nota",min(notas))
