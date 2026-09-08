soma=0
qtd =0

for numero in range(1,20):

    if numero % 2 == 0 and numero > 0:
        soma=soma+numero
        qtd=qtd+1

med=soma/qtd

print ("quantidade que atende",qtd)
print("media",med)
