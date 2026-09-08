vogais=0
cons=0

for i in range(10):

    letra=input("digite uma letra").lower()

    if letra in "aeiou":
        vogais=vogais+1
    else:
        cons=cons+1

print("quantidade de vogais",vogais)
print ("quantidae de consoantes",cons)
