soma=0
quantidade=0

while quantidade < 10:
    numero=int(input("digite um numero divisivel por 6"))

    if numero % 6 == 0:
        soma=soma+numero
        quantidade=quantidade+1
    else:
        print("esse numero nao eh divisivel por 6")

print ("soma dos numeros eh",soma)
