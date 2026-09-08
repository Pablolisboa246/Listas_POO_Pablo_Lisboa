inicio=int(input("digite inicio do intervalo"))
fim=int(input("digite fim do intervalo"))
qtd=0

if inicio <= fim:

    for numero in range(inicio,fim+1):

        if numero % 7 == 0:
            qtd=qtd+1

else:

    for numero in range(fim,inicio+1):

        if numero % 7 == 0:
            qtd=qtd+1

print("quantidae de multiplos de 7",qtd)
