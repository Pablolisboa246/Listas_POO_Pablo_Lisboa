primeiro = int(input("digite primeiro identificador"))
ultimo=int(input("digite ultimo identificador"))
soma=0
qtd=0

if primeiro <= ultimo:

    for numero in range(primeiro,ultimo+1):
        soma=soma+numero
        qtd=qtd+1

else:

    for numero in range(ultimo,primeiro+1):
        soma=soma+numero
        qtd=qtd+1

med=soma/qtd

print("media dos numeros",med)
