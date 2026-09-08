soma=0
quantidade=0

while quantidade < 10:

    numero=int(input("digite um numero divisivel por 3"))

    if numero % 3 == 0:
        soma=soma+numero
        quantidade=quantidade+1

    else:
        print ("numero nao serve")

print("soma dos valor",soma)
