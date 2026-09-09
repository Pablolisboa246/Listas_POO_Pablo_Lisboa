iniciointervalo=int(input("digite o inicio do intervalo "))
finalintervalo=int(input("digite o final do intervalo "))
cont=0

for numero in range (iniciointervalo, finalintervalo+1):
 if numero % 7 ==0:
  cont = cont+1

print(" a quantidade de numeros multiplos de 7 eh igual ah", cont)